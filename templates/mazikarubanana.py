list = []
a = input("バナナと言えば")
list.append(a)
for i in range(5):
   list.append(input(f"{list[-1]}といったら？"))
   print(list)