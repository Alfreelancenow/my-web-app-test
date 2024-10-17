from flask import Flask, request, render_template
import requests  # Для отправки HTTP-запросов

app = Flask(__name__)

# URL твоего Google Apps Script веб-приложения
api_url = 'https://script.google.com/macros/s/AKfycbzxrff5VxixVOKMRSDBi-a8FcwBiiYyabT905YthURJ2zIBKS8UcySiu-5lEnweja0o/exec'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/check_product', methods=['POST'])
def check_product():
    product_name = request.form['product']  # Получаем название продукта от пользователя

    # Отправляем запрос на Google Apps Script и получаем ответ
    response = requests.get(api_url, params={'product': product_name})
    
    # Извлекаем текстовый ответ от Google Apps Script
    message = response.text
    
    return render_template('result.html', message=message)  # Отображаем результат на странице

if __name__ == '__main__':
    app.run(debug=True)
