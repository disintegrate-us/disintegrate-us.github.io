from wtforms import Form, PasswordField, SubmitField, validators


class LoginPage_LoginForm(Form):
    password = PasswordField(label="Password", validators=[validators.DataRequired()])
    submit = SubmitField(label="Enter")

