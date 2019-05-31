import random
a1=random.randint(0,9) #2~6行でランダムな４桁の数字を生成する。0000~9999　それを文字列としてaに入れる。
a2=random.randint(0,9)
a3=random.randint(0,9)
a4=random.randint(0,9)
a=str(a1)+str(a2)+str(a3)+str(a4)
print(a)　　　　　　　　#試すためにaは一応表示している。実際運用する際はこの行を削除
b=input("4桁の数字を入力してください:")
if b[0]<"0" or b[0]>"9":　　　　　　#９～１６行でbにしっかりと文字ではなく数字が入力されているかどうかを検知
      b=input("数字を入力してください:")
elif b[1]<"0" or b[1]>"9":
      b=input("数字を入力してください")
elif b[2]<"0" or b[2]>"9":
      b=input("数字を入力してください")
elif b[3]<"0" or b[2]>"9":
      b=input("数字を入力してください")
while len(b)!=4 :　　#４桁の数字を入力させたいので文字が４桁になっていない場合聞きなおす。
  b=input("４桁の数字を入力してください:")
while a!=b:　　　　　#正解するまで入力させる。
  print("はずれです")
  b=(input("正しい答えを入力してください："))
print("答えは"+str(a)+"でした。お見事！")
