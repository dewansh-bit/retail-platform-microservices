from flask import Flask, jsonify

app = Flask(__name__)

inventory = [
    {"product_id": 1, "stock": 25, "warehouse": "Pune"},
    {"product_id": 2, "stock": 80, "warehouse": "Mumbai"},
    {"product_id": 3, "stock": 150, "warehouse": "Bangalore"}
]

@app.route("/")
def home():
    return "Inventory Service is running successfully!"

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

@app.route("/inventory/<int:product_id>", methods=["GET"])
def get_inventory_by_product(product_id):
    item = next((i for i in inventory if i["product_id"] == product_id), None)

    if item:
        return jsonify(item)

    return jsonify({"error": "Inventory not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)