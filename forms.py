from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField, IntegerField, FileField
from wtforms.validators import DataRequired



class RegistrationForm(FlaskForm):

    username = StringField("enter username", validators=[DataRequired()])
    password = PasswordField("enter password", validators=[DataRequired()])
    repeat_password = PasswordField("repeat password", validators=[DataRequired()])
    name = StringField("enter full name", validators =[DataRequired()])
    email = EmailField("enter your E-mail", validators =[DataRequired()])
    number = IntegerField("enter your number", validators =[DataRequired()])
    img = FileField("upload an image", validators =[DataRequired()])

    submit = SubmitField('Submit')


class UploadForm(FlaskForm):

    name = StringField("enter the name of the pet", validators=[DataRequired()])
    breed = StringField("enter the breed of the pet", validators=[DataRequired()])
    description = StringField("describe the pet", validators=[DataRequired()])
    img = FileField("upload an image", validators =[DataRequired()])
    contact = StringField("enter your contact information", validators =[DataRequired()])

    submit = SubmitField('Upload')

class LoginForm(FlaskForm):
    username = StringField("enter username", validators=[DataRequired()])
    email = EmailField("enter your E-Mail", validators=[DataRequired()])
    password = PasswordField("enter password", validators=[DataRequired()])

    submit = SubmitField('Log In')