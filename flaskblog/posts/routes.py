from click import command
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post,Comment
from flaskblog.posts.forms import PostForm,AddCommentForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

#
# @posts.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
# @login_required
# def comment_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     posts = Post.query.all()
#     form = AddCommentForm()
#     if request.method == 'POST': # this only gets executed when the form is submitted and not when the page loads
#         if form.validate_on_submit():
#             text = request.form.get('text')
#             comment = Comment(text=text,post_id=post.id)
#             db.session.add(comment)
#             db.session.commit()
#             flash("Your comment has been added to the post", "success")
#             return redirect(request.url)
#     return render_template('comment_post.html', title='Comment Post', form=form, post=post,posts=posts)


# @app.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
# @login_required
# def comment_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     form = AddCommentForm()
#     if form.validate_on_submit():
#         comment = Comment(text=form.text.data,post_id=post.id)
#         db.session.add(comment)
#         print(comment.text)
#         comment_text=comment.text
#         db.session.commit()
#         flash("Your comment has been added to the post", "success")
#         return redirect(url_for("posts.post", post_id=post.id))
#     return render_template("comment_post.html", title="Comment Post", form=form,post_id=post_id)
#
#
#

@posts.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def comment_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    if request.method == 'POST': # this only gets executed when the form is submitted and not when the page loads
        if form.validate_on_submit():
            user_id = current_user.username
            comment = Comment(body=form.body.data,author=user_id, post_id=post.id)
            db.session.add(comment)
            db.session.commit()
            flash("Your comment has been added to the post", "success")
            return redirect(url_for("posts.post", post_id=post.id))
    return render_template("comment_post.html", title="Comment Post", form=form, post_id=post_id)


@posts.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)