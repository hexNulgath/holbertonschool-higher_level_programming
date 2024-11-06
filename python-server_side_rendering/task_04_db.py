from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
import csv
import sqlite3

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert product instance to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': str(self.price)  # Ensure price is string for consistency
        }

def create_database():
    with app.app_context():  # Ensure the app context is active
        db.create_all()  # Create tables if they do not exist
        if not Product.query.first():
            products = [
                Product(id=1, name='Laptop', category='Electronics', price=799.99),
                Product(id=2, name='Coffee Mug', category='Home Goods', price=15.99)
            ]
            db.session.bulk_save_objects(products)
            db.session.commit()
create_database()


# Read CSV file
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

# Read JSON file
def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return "Error: Failed to decode JSON"

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
        products = Product.query.all()
        products = [product.to_dict() for product in products]

    if product_id:
        products = [product for product in products if product['id'] == product_id]

    if not products:
        return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
