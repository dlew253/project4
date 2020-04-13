from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Home():
   return render_template("Home.js") 

@app.route('/Login')
def Login():
   return render_template("./pages/Login.js")

@app.route('/Signup')
def Signup():
   return render_template("./pages/Signup.js")

@app.route('/Notepad')
def Notepad():
   return render_template("./pages/Notepad.js")


if __name__ == '__main__':
   app.run(debug=True)