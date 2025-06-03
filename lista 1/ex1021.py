num = int(round(float(input())*100))
notes = [(10000,'100'),(5000,'50'),(2000,'20'),(1000,'10'),(500,'5'),(200,'2')]
coins = [(100,'1.00'),(50,'0.50'),(25,'0.25'),(10,'0.10'),(5,'0.05'),(1,'0.01')]
print('NOTAS:')
for div, note in notes:
    print(f'{num//div} nota(s) de R$ {note}.00')
    num -= (num//div)*div
print('MOEDAS:')
for div, coin in coins:
    print(f'{num//div} moeda(s) de R$ {coin}')
    num -= (num//div)*div
