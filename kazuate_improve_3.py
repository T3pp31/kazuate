import random
a1 = random.randint(0, 9)
a2 =random.randint(0, 9)
a3 = random.randint(0, 9)
a4 = random.randint(0, 9)
a = str(a1)+str(a2)+str(a3)+str(a4)
hit=0
print(a)#実際運用する際はこの行を削除。
b = input("4桁の数字を入力してください:")
for i in range(4):
    if b[i]>"9" or b[i]<"0":
        print("数字を入力してください")
    while len(b) != 4:
        b = input("４桁の数字を入力してください:")
    while a != b:
        print("はずれです")
        hit=0
        for f in range(4):
            if a[f]==b[f]:
                hit=hit+1
        print(str(hit)+"個あっています")
        
        b = (input("正しい答えを入力してください："))
print("答えは"+str(a)+"でした。お見事！")
