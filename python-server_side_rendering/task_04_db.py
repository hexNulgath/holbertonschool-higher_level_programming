from flask import Flask, render_template, request
import sqlite3
import json
import csv

app = Flask(__name__)

# Database setup function
def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert initial data
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()

# Read from JSON file
def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return "Error: Failed to decode JSON"

# Read from CSV file
def read_csv():
    products = []
    try:
        with open('products.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)
    return products

# Fetch products from SQLite database
def get_products_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    
    conn.close()
    return products

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

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source. Please use 'json', 'csv', or 'sql'.")
    
    if source == 'json':
        products = read_json()
        if products is None:
            return render_template('product_display.html', error="JSON file not found.")
        elif isinstance(products, str):  # Error message from JSON decoding
            return render_template('product_display.html', error=products)
    elif source == 'csv':
        products = read_csv()
        if products is None:
            return render_template('product_display.html', error="CSV file not found.")
        elif isinstance(products, str):  # Error message from CSV reading
            return render_template('product_display.html', error=products)
    elif source == 'sql':
        products = get_products_from_sql()

    if product_id:
        products = [product for product in products if product['id'] == product_id]

    if not products:
        return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
