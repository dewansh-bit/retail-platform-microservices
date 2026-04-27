from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 75000},
    {"id": 2, "name": "Headphones", "category": "Electronics", "price": 2500},
    {"id": 3, "name": "Coffee Mug", "category": "Home", "price": 499}
]

@app.route("/")
def home():
    return "Product Service is running successfully!"

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = next((p for p in products if p["id"] == product_id), None)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)