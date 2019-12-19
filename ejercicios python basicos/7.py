import datetime

while True:
    try:
        min = int(input('ingrese minutos: '))
        break
    except:
        print("dato invalido ingrese dato nuevamente")


time = datetime.timedelta(minutes=min)



print('el tiempo expresado es:')
print(time)