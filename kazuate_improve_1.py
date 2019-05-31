import random
a1=random.randint(0,9)
a2=random.randint(0,9)
a3=random.randint(0,9)
a4=random.randint(0,9)
a=str(a1)+str(a2)+str(a3)+str(a4)
print(a)
b=input("4桁の数字を入力してください:")
if b[0]<"0" or b[0]>"9":
   b=input("数字を入力してください:")
while len(b)!=4 :
  b=input("４桁の数字を入力してください:")
  if b[0]<"0" or b[0]>"9":
    b=input("数字を入力してください:")
while a!=b:
  print("はずれです")
  b=(input("正しい答えを入力してください："))
if b[0]<"0" or b[0]>"9":
  b=input("数字を入力してください:")
print("答えは"+str(a)+"でした。お見事！")
