import datetime
from playsound import playsound
from sympy import Min
Hour = int(input("Enter hour: "))
Minut = int(input("Enter minut: "))
pmam = input("am / pm: ")

if pmam == "pm":
    Hour += 12

while True:
    if Hour==datetime.datetime.now().hour and Minut==datetime.datetime.now().minute:
        print("Playing... ")
        playsound("Amantu_Billahi_Нашид_Мы_Верим_В.mp3")
        break