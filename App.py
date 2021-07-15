from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('main.html')

@app.route('/Camisas')
def Camisas():
    return render_template('camisas.html')

@app.route('/Hoodies')
def Hoodies():
    return render_template('Hoodies.html')

if __name__ == "__main__":
    app.run(debug = True)