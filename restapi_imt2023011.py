from flask import Flask, request, jsonify

# restapi_imt2023011.py

"""
Product Inventory REST API
Implements CRUD operations for managing products using Flask.
Endpoints:
- GET /products: List all products
- GET /products/<product_id>: Get a product by ID
- POST /products: Add a new product
- POST /products/<product_id>: Update a product by ID
- DELETE /products/<product_id>: Delete a product by ID
All data is exchanged in JSON format.
"""


app = Flask(__name__)

# In-memory product store (id, name, price, quantity)
products = {}
next_id = 1

# GET endpoint: List all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Returns a list of all products in the inventory.
    """
    return jsonify(list(products.values())), 200

# GET endpoint: Get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Returns a product by its ID.
    """
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# POST endpoint: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Adds a new product to the inventory.
    Expects JSON: { "name": str, "price": float, "quantity": int }
    """
    global next_id
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "price", "quantity")):
        return jsonify({"error": "Missing product fields"}), 400
    product = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    products[next_id] = product
    next_id += 1
    return jsonify(product), 201

# POST endpoint: Update a product by ID
@app.route('/products/<int:product_id>', methods=['POST'])
def update_product(product_id):
    """
    Updates an existing product in the inventory by its ID.
    Expects JSON: { "name": str, "price": float, "quantity": int }
    """
    data = request.get_json()
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404
    if not data or not any(k in data for k in ("name", "price", "quantity")):
        return jsonify({"error": "No fields to update"}), 400
    
    product = products[product_id]
    product.update({k: data[k] for k in ("name", "price", "quantity") if k in data})
    
    return jsonify(product), 200

# DELETE endpoint: Remove a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Deletes a product from the inventory by its ID.
    """
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404
    del products[product_id]
    return jsonify({"message": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)