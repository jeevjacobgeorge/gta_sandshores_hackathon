from flask import Flask,redirect,render_template
import json
from functools import reduce
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/mq')
def mq():
    return render_template('mq.html')

@app.route('/submitmq',methods = ['GET','POST'])
def submitmq():
    with open("data.json", "r") as f:
        data = json.load(f)
        
    quiz_res = data['john4smith']['answers']

    idx = float(reduce(lambda acc, val: acc + 5 - val, quiz_res, 0) / 2.5)
    data["john4smith"]["happyidx"][str(date.today())] = idx

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    return render_template("dashboard.html",hi=idx)


if __name__ == "__main__":
    app.run(debug=True)

