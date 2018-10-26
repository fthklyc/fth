list = []


while True:
    n = int(input("Kaç adet sayı gireceksiniz:"))
    if n<=0:
        print("0'dan büyük değerler giriniz...")

    elif n>0:

        for i in range(n):
            x = int(input("Bir sayi giriniz:"))
            list.append(x)

        y = sorted(list,reverse=True) #dizi içini büyükten küçüğe sıralama
        for j in y:
            print('{}'.format(j))

        break

with open("C:/Users/Kullanici/Desktop/dizisiralama.txt","a") as dosya:
    for d in y:
        
        dosya.write('{}\n'.format(str(d)))
