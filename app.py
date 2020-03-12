from flask import Flask, render_template, request

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
    
            if not email is None and not password is None:
                return f"Email: {email} / password: {password}"

            return "Os dados precisam ser inseridos"
    
        return render_template("login.html")

    return app