from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------- HOME --------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple demo logic
        if username == "admin" and password == "1234":
            return f"Welcome {username}!"
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Demo response (no database)
        return f"User {username} registered successfully!"

    return render_template("register.html")


# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    return redirect(url_for("home"))


# -------------------- MAIN --------------------
if __name__ == "__main__":
    app.run(debug=True)