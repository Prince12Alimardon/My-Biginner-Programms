import math
print("EKUK va EKUB ni hisoblash uchun '1' ni bosing.")
print("Faktorialni hisoblash uchun '2' ni bosing.")
print("Logarifmni hisoblash uchun '3' ni bosing.")
print("2 sonni qo'shish,ayirish,ko'paytirish va bo'lish uchun '4' ni bosing.")
print("Sonning darajasini hisoblash uchun '5' ni bosing")
print("Sonning cosinus ini hisoblash uchun '6' ni bosing")
print("Sonning sinus ini hisoblash uchun '7' ni bosing")
print("Sonning tanginusini  ini hisoblash uchun '8' ni bosing")
print("To'g'ri to'rtburchakni perimetri va yuzini hisoblash uchun '9' ni bosing")
print("Kvadratning perimetri va yuzini hisoblash uchun '10' ni bosing")
# print("Ushbu dasturni @Alimardon_Boqijonov yaratgan")
a = int(input("O'zingizga kerakli bo'lgan sonni kiriting 1,2,3,4,5,6,7,8,9 va 10 sonlaridan birini sonlaridan birini:"))

if a==1:
    a = int(input("EKUK va EKUB ni hisoblash uchun 1-sonni kiriting:"))
    b = int(input("EKUK va EKUB ni hisoblash uchun 2-sonni kiriting:"))
    print("EKUB:", math.gcd(a, b))
    print("EKUK:", a * b / math.gcd(a, b))
    c = int(input("Mana javobi"))
if a==2:
    a = int(input("Faktorialni hisoblash uchun sonni kiriting:"))
    print(print("Faktorial:", math.factorial(a)))
    c = int(input("Mana javobi"))
if a==3:
    x = int(input("Logarifm asosini kiriting:"))
    y = int(input("Sonni kiriting:"))
    print("Logarifm:", math.log(y, x))
    c = int(input("Mana javobi"))
if a==4:
    a=int(input("1-sonni kiriting:"))
    b=int(input("2-sonni kiriting:"))
    print("Yig'indi:", a+b)
    print("Ayirma:", a-b)
    print("Ko'paytma:", a*b)
    print("Bo'linma:", a/b)
    c=int(input("Mana natija"))
if a==5:
    a=int(input("Qaysi sonning darajasini hisoblamoqchisiz?:"))
    b=int(input("Sonning nechanchi darajasini hisoblamoqchisiz?:"))
    print("Sonning darajasi:", math.pow(a,b) , "ga teng")
    c=int(input("Mana natija"))
if a==6:
    a=int(input("Qaysi soning cosinus ini hisoblamoqchisiz?:"))
    print("cosinus", math.cos(a), "ga teng")
    c=int(input("Mana natija"))
if a==7:
    a=int(input("Qaysi sonning sinus ini hisoblamoqchisiz?:"))
    print("sinus", math.sin(a), "ga teng")
    c=int(input("Mana natija"))
if a==8:
    a=int(input("Qaysi sonning tanginus ini hisoblamoqchisiz?:"))
    print("tanginus", math.tan(a), "ga teng")
    c=int(input("Mana natija"))
if a==9:
    a=int(input("To'g'ri to'rtburchakning 1-tomonining uzunligini kiriting:"))
    b=int(input("To'g'ri to'rtburchakning 2-tomonining uzunligini kiriting:"))
    print("Perimetri:", (a+b)*2, "ga teng")
    print(("Yuzi:"), a*b,"ga teng")
    print("Mana natija")
if a==10:
    a=int(input("Kvadratning tomonining uzunligini kiriting:"))
    print("Kvadratning perimetri:",4*a, "ga teng")
    print("Kvadratning yuzi",a*a, "ga teng")
    c=int(input("Mana natija"))
