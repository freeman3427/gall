from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class GalleryForm(FlaskForm):
    title = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[
                           DataRequired(), Length(min=3, max=25)])
    passwordOne = PasswordField(
        '비밀번호', validators=[DataRequired(), EqualTo('passwordTwo', '비밀번호가 일치하지 않습니다')])
    passwordTwo = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[
                           DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
