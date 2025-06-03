day = [int(x) for x in input().split() if x.isdigit()]
hr,mt,sc = [int(x) for x in input().split() if x.isdigit()]
dayf = [int(x) for x in input().split() if x.isdigit()]
hf,mf,sf = [int(x) for x in input().split() if x.isdigit()]

start = (day[0]*86400)+(hr*3600)+(mt*60)+sc
end = (dayf[0]*86400)+(hf*3600)+(mf*60)+sf
event = end-start
time = [(86400,'dia(s)'),(3600,'hora(s)'),(60,'minuto(s)'),(1,'segundo(s)')]
for d, s in time:
    t = event//d
    event %= d
    print(f'{t} {s}')
