from datetime import datetime

tugilgan_yil = input("Tug'ilgan yilni kiriting: ")

bugun = datetime.today()
natija = bugun.year - int(tugilgan_yil)

print('Natija: ', natija)
