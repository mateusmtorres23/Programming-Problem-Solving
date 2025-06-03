num = int(input());print(num)
values = [(100,'100,00'),(50,'50,00'),(20,'20,00'),(10,'10,00'),(5,'5,00'),(2,'2,00'),(1,'1,00')]
for div, note in values:
    print(f'{num//div} nota(s) de R$ {note}')
    num-= (num//div)*div
