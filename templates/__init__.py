from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)


    app = Flask(__name__)
    app.config['SECRET_KEY'] = "decapitatedSquirrelButt4201337"
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    db = SQLAlchemy(app)


    class usernameandpassworddemo(db.Users):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(255))
        password = db.Column(db.String(255))

    class SignupForm(FlaskForm):
        username = StringField('Username:', validators=[DataRequired()])
        password = StringField('Password:', validators=[DataRequired()])

    @app.route('/add_User', method['GET', 'PUSH'])
    def add_User():
        form = SignupForm()
        if form.validate_on_submit():
            userInfo = usernameandpassworddemo(username=form.username.data, password=form.password.data)
            db.session.add(userInfo)
            db.session.commit()


    return app

