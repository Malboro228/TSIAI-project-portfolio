from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    """Функция для сложения"""
    return x + y

def subtract(x, y):
    """Функция для вычитания"""
    return x - y

def multiply(x, y):
    """Функция для умножения"""
    return x * y

def divide(x, y):
    """Функция для деления"""
    if y == 0:
        return "Ошибка: Деление на ноль!"
    return x / y

@app.route('/')
def home():
    return render_template('index123.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        result = "Неверная операция"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
