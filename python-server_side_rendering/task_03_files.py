from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_csv():
    products = []
    with open('products.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products
def read_json():
    with open('products.json') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)  
            items_list = data.get('items', []) 
    except FileNotFoundError:
        return "<h1>Error: items.json file not found</h1>"
    except json.JSONDecodeError:
        return "<h1>Error: Failed to decode JSON</h1>"
    
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source. Please use 'json' or 'csv'.")
    
    if source == 'json':
        products = read_json()
    else:
        products = read_csv()

    if product_id:
        products = [product for product in products if product['id'] == product_id]

    if not products:
        return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)