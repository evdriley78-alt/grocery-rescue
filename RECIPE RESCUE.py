from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Mock data ---
recipes = {
    "chicken stir fry": {
        "ingredients": ["chicken", "soy sauce", "broccoli", "rice"],
        "stores": {
            "Walmart": 12.50,
            "Kroger": 13.20,
            "Target": 14.00
        }
    },
    "spaghetti": {
        "ingredients": ["pasta", "tomato sauce", "ground beef"],
        "stores": {
            "Walmart": 10.75,
            "Kroger": 11.50,
            "Target": 12.00
        }
    }
}

@app.route("/")
def home():
    return render_template("index.html", recipes=recipes)

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"].lower()
    result = recipes.get(query)
    return render_template("result.html", recipe=query, data=result)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"].lower()
        ingredients = request.form["ingredients"].split(",")
        walmart = float(request.form["walmart"])
        kroger = float(request.form["kroger"])
        target = float(request.form["target"])
        recipes[name] = {
            "ingredients": [i.strip() for i in ingredients],
            "stores": {"Walmart": walmart, "Kroger": kroger, "Target": target}
        }
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/delete/<recipe>")
def delete(recipe):
    if recipe in recipes:
        del recipes[recipe]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
