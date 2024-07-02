from flask import Flask, render_template,session,redirect,url_for,request

app = Flask(__name__)
app.secret_key= 'ANGEVEGA'
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
        return redirect(url_for('segura.html'))
    return render_template('login.html')

if __name__ == "__main__":
        app.run(debug=True)







if __name__ == "__main__" :
    app.run(debug=True)