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
            'price': str(self.price)
        }

def create_database():
    db.create_all()  
    if not Product.query.first():
        products = [
            Product(id=1, name='Laptop', category='Electronics', price=799.99),
            Product(id=2, name='Coffee Mug', category='Home Goods', price=15.99)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

# Read CSV file
def read_csv():
    products = []
    with open('products.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

# Read JSON file
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

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source. Please use 'json', 'csv', or 'sql'.")
    
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = Product.query.all()
        products = [product.to_dict() for product in products]

    if product_id:
        products = [product for product in products if product['id'] == product_id]

    if not products:
        return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

create_database()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
