from flask import Flask, render_template, request
app = Flask(__name__)

# Food menu with prices
menu_items = {
"Pizza": 250,
"Burger": 120,
"Sandwich": 100,
"Pasta": 180
}

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Menu page
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Order page
@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        food = request.form.get("food")
        quantity = request.form.get("quantity")

        # Input validation
        if food not in menu_items:
            return "Invalid food selection!"

        try:
            quantity = int(quantity)
            if quantity <= 0:
                return "Please enter a valid quantity!"

        except (ValueError, TypeError):
            return "Please enter a valid quantity!"

        # Calculate bill
        price = menu_items[food]
        total = price * quantity

        return render_template(
            "result.html",
            food=food,
            quantity=quantity,
            price=price,
            total=total
        )
    return render_template("order.html")

if __name__ == "__main__":
    app.run(debug=True)
