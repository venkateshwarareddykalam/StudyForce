from flask import Flask, render_template
from routes.study_plan import study_bp

app = Flask(__name__)

app.register_blueprint(study_bp)

@app.route("/")
def index():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
