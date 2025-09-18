from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        buy_price = float(request.form["buy_price"])
        mrp_price = float(request.form["mrp_price"])
        discount = float(request.form["discount"])
        bottles = int(request.form["bottles"])
        free_bottles = int(request.form["free_bottles"])

        sell_price = mrp_price * (1 - discount / 100)
        total_bottles = bottles + free_bottles
        total_cost = total_bottles * buy_price
        total_revenue = bottles * sell_price
        profit = total_revenue - total_cost
        profit_percent = (profit / total_cost * 100) if total_cost > 0 else 0

        result = {
            "sell_price": round(sell_price, 2),
            "total_revenue": round(total_revenue, 2),
            "total_cost": round(total_cost, 2),
            "profit": round(profit, 2),
            "profit_percent": round(profit_percent, 2)
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
