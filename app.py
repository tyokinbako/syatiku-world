from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# スケジュールを保存するリスト
schedule_list = []

@app.route("/santa", methods=["GET", "POST"])
def santa():
    return render_template("santa.html")

@app.route("/kani", methods=["GET", "POST"])
def sana():
    return render_template("aiaiaiaiaiai.html")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/riyoukiyaku")
def unti():
    return render_template("riyoukiyaku.html")

@app.route("/aaaa")
def aaaa():
    return render_template("aaaa.html")

@app.route("/momomo")
def aaaaaaaaaw():
    return render_template("sutezerihu.html")

@app.route("/pdf")
def pdf():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    # 日本語フォントを登録（ここでは明朝体 HeiseiMin-W3）
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

    from reportlab.pdfgen import canvas

    from io import BytesIO

    from flask import send_file

    # PDFファイルの保存先
    file_name = "aiueonzzzz.pdf"

    # キャンバスを作成
    buf = BytesIO()

    c = canvas.Canvas(buf)

    c.setFont("HeiseiMin-W3", 20)

    # テキストを描画
    c.drawString(30, 700,"　　　御中")
    c.setFont("HeiseiMin-W3", 50)
    c.drawString(230, 780, "辞任届")
    c.setFont("HeiseiMin-W3", 15)
    c.drawString(30, 670, "氏名 ")
    c.drawString(400, 670, "辞任理由")
    c.drawString(460, 670, "　　　　")
    c.drawString(405, 650, "今までの感謝")
    c.drawString(500, 650, "　　")
    c.setFont("HeiseiMin-W3", 10)
    c.drawString(30, 550, "宛名       　様、ありがとうございました")
    x, y = 30, 430  # 左下の座標
    width, height = 200, 100  # 幅と高さ
    c.rect(x, y, width, height, stroke=1, fill=0)  # stroke=枠線, fill=塗りつぶし
    # PDFを保存
    c.save()

    buf.seek(0)
    response = send_file(
        buf,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=file_name
    )
    response.headers["Cache-Control"] = "no-store"
    return response



if __name__ == "__main__":
    app.run(debug=True)
