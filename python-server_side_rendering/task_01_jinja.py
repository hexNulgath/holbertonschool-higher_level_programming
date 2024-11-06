from flask import Flask, render_template
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)