from flask import Flask,redirect,render_template,request
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

@app.route('/submitmq/<float:idx>',methods = ['GET','POST'])
def submitmq(idx):
    with open("gta_sandshores_hackathon/data.json", "r") as f:
            data = json.load(f)

    quiz_res = data['john4smith']['answers']
    data["john4smith"]["happyidx"][str(date.today())] = idx

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    return render_template("dashboard.html",hi=idx)

@app.route('/game')
def game():
    return render_template("flappy_bird.html")

@app.route('/joke')
def joke():
    return render_template('joke.html')

@app.route('/be')
def be():
    return render_template('be.html')

@app.route('/music')
def music():
    return render_template("music.html")
@app.route('/quit_joke',methods = ['GET','POST'])
def quit_joke():
    with open("gta_sandshores_hackathon/data.json", "r") as f:
        data = json.load(f)

    act_idx = 0
    review = int(request.form.get("feedback"))
    data["john4smith"]["total-freq"][act_idx] += 1
    data["john4smith"]["success-freq"][act_idx] += review

    effectiveness = data["john4smith"]["success-freq"][act_idx] / data["john4smith"]["total-freq"][act_idx]
    today = str(date.today())
    oldHappyIdx = data["john4smith"]["happyidx"][today]
    inc = 0.2 if review else 0.1
    data["john4smith"]["happyidx"][today] = min(round(oldHappyIdx * (1 + inc * effectiveness), 2), 10)

    with open("gta_sandshores_hackathon/data.json", "w") as f:
        json.dump(data, f, indent=4)

    return render_template('dashboard.html', hi=data['john4smith']['happyidx'][today])

@app.route('/quit_be',methods = ['GET','POST'])
def quit_be():
    with open("gta_sandshores_hackathon/data.json", "r") as f:
        data = json.load(f)

    act_idx = 1
    review = 1
    data["john4smith"]["total-freq"][act_idx] += 1
    data["john4smith"]["success-freq"][act_idx] += review

    effectiveness = data["john4smith"]["success-freq"][act_idx] / data["john4smith"]["total-freq"][act_idx]
    today = str(date.today())
    oldHappyIdx = data["john4smith"]["happyidx"][today]
    inc = 0.15 if review else 0.05
    data["john4smith"]["happyidx"][today] = min(round(oldHappyIdx * (1 + inc * effectiveness), 2), 10)

    with open("gta_sandshores_hackathon/data.json", "w") as f:
        json.dump(data, f, indent=4)

    return render_template('dashboard.html', hi=data['john4smith']['happyidx'][today])

if __name__ == "__main__":
    app.run(debug=True)
