import os
import secrets
from PIL import Image
from flask import Flask,render_template,url_for,flash,redirect,request,abort
from flaskblog import app,db,bcrypt,mail
from flaskblog.forms import RegistrationForm,LoginForm,UpdateAccountForm,PostForm,RequestResetForm,ResetPasswordForm
from flaskblog.models import User,Post
from flask_login import login_user,current_user, logout_user, login_required
from flask_mail import Message

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


