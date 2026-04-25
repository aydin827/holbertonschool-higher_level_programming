import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    # 1. Mənbə yoxlaması
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Məlumatın oxunması
    try:
        if source == 'json':
            with open('products.json', 'r') as f:
                products = json.load(f)

        elif source == 'csv':
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products = [row for row in reader]
                # ID-ləri müqayisə üçün rəqəmə çevirək
                for p in products:
                    p['id'] = int(p['id'])

        elif source == 'sql':
            conn = sqlite3.connect('products.db')
            # Məlumatları lüğət (dict) kimi götürmək üçün row_factory istifadə edirik
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            rows = cursor.fetchall()
            # SQL row obyektini Python lüğətinə (dict) çeviririk
            products = [dict(row) for row in rows]
            conn.close()

    except Exception as e:
        error = f"Database or File error: {str(e)}"

    # 3. ID-yə görə filtr (əgər URL-də id varsa)
    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
