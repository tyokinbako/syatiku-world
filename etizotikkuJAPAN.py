from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
# 日本語フォントを登録（ここでは明朝体 HeiseiMin-W3）
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

from reportlab.pdfgen import canvas

# PDFファイルの保存先
file_name = "aiueon.pdf"

# キャンバスを作成
c = canvas.Canvas(file_name)

c.setFont("HeiseiMin-W3", 20)

# テキストを描画
c.drawString(30, 700, "あいえおん超重要株御中")
c.setFont("HeiseiMin-W3", 50)
c.drawString(230, 780, "請求書")
c.setFont("HeiseiMin-W3", 15)
c.drawString(30, 670, "4283510462")
c.drawString(400, 670, "請求日")
c.drawString(460, 670, "xxxx年xx月9日")
c.drawString(405, 650, "請求書番号")
c.drawString(500, 650, "INV-i")
c.setFont("HeiseiMin-W3", 10)
c.drawString(30, 550, "下記のとおりご請求申し上げます。")
x, y = 30, 430  # 左下の座標
width, height = 200, 100  # 幅と高さ
c.rect(x, y, width, height, stroke=1, fill=0)  # stroke=枠線, fill=塗りつぶし
# PDFを保存
c.save()