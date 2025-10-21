import random
aiueon = random.randint (1,10000)
print("数を当てろ！！！")
for i in range(11):
    pa = int(input("1/10000!!!"))
    if pa == aiueon:
       print("もっとあいつはBIG...でもないな、正解。いい感じの絵文字をやるよ('ω'◦[ここに文字を入れる]◦ (｀ω´◦[ここに文字を入れる]◦ (⚆`ε´⚆◦[私はおこっています]◦")
       print(i, "回目で正解したようだな")
       break
    elif pa < aiueon:
        print("あいつはもっとBIG")
    else:
        print("あいつはもっと気の小さい奴だ ")