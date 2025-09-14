# app.py
from flask import Flask, render_template, request
import model_hf
import automation
import os

app = Flask(__name__)

# Initialize the AI model and automation
ai_model = model_hf.AIModelHF()
automator = automation.Automation(ai_model)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]
        result = automator.run_analysis(data)
        return render_template("index.html", result=result)
    return render_template("index.html", result=None)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5577))
    app.run(debug=True, host='0.0.0.0', port=port)
