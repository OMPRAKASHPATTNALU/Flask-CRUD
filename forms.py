from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField, HiddenField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class RegistrationForm(FlaskForm):
    username=StringField(label='username',validators=[DataRequired(),Length(min=3,max=30)])
    email= StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password=PasswordField(label='confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='signup')

class LoginForm(FlaskForm):
    email= StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=16)])
    submit=SubmitField(label='Login')

class SearchForm(FlaskForm):
    name=StringField(label='Name',validators=[DataRequired(),Length(min=3,max=30)])
    subject=StringField(label='Subjects',validators=[DataRequired(),Length(min=3,max=30)])
    mark=IntegerField(label='Mark',validators=[DataRequired()])
    submit=SubmitField(label='Add Details')    

class EditForm(FlaskForm):
    id = HiddenField()
    name=StringField(label='Name',validators=[DataRequired(),Length(min=3,max=30)])
    subject=StringField(label='Subjects',validators=[DataRequired(),Length(min=3,max=30)])
    mark=IntegerField(label='Mark',validators=[DataRequired()])
    submit=SubmitField(label='Edit Details')     