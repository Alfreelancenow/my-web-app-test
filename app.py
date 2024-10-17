from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        product_name = request.form['product_name']
        # Здесь должна быть логика для проверки наличия продукта
        return f'Вы запросили продукт: {product_name}'  # Просто для теста
    return render_template('buy.html')

if __name__ == '__main__':
    app.run(debug=True)
