from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# スケジュールを保存するリスト
schedule_list = []

@app.route("/santa", methods=["GET", "POST"])
def santa():
    return render_template("santa.html")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/riyoukiyaku")
def unti():
    return render_template("riyoukiyaku.html")

if __name__ == "__main__":
    app.run(debug=True)
