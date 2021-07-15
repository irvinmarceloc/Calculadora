from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html', modo='modo1' )

@app.route('/calcula', methods=['POST'])
def calcula():
    a = int (request.form['num1'])
    b = int (request.form['num2'])
    c = request.form['operacion']
    
    if c == 'suma':
        d = suma(a,b)
        e = '+'
    if c == 'resta':
        d = resta(a,b)
        e = '-'
    if c == 'multiplicacion':
        d = multiplica(a,b)
        e = '*'
    if c == 'division':
        d = divide(a,b)
        e = '/'
    
    return render_template('index.html', modo='modo2', resultado = d,signo=e, num1= a, num2= b )

def suma(a,b): 
    c = a + b
    return c
def resta(a,b): 
    c = a - b
    return c
def multiplica(a,b): 
    c = a * b
    return c
def divide(a,b): 
    c = a / b
    return int(c)

if __name__ == '__main__':
    app.run(debug=True)