from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "HEllo world"

if __name__ == "__main__":
    app.run(debug=True)

