
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,session,redirect,url_for,request

#DATABASE = 'C:\Users\gig2024\Desktop\weather_app.v2\db.sqlite'

app = Flask(__name__)
app.secret_key= 'ANGEVEGA'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"


db = SQLAlchemy (app)  


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    nombre = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)

@app.route("/segura")
def segura():
    if session:
        return render_template('segura.html')
    else: 
        return redirect(url_for('login'))

@app.route("/login", methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = str(request.form.get ( 'email'))
        password = request.form.get ('password')
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario: 
            session['name']=usuario.nombre
            return redirect(url_for('segura'))     
    return render_template('login.html')

@app.route("/logout")
def logout ():
    session.clear()
    return redirect_templates((url_for)('login'))
    
    

if __name__ == "__main__":
        app.run(debug=True)


@app.route("/logout")




if __name__ == "__main__" :
    app.run(debug=True)