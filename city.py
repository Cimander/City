from random import randint
def robot(bukv,file):
    slov = []
    for i in file:
        norm = i
        i = i[0]
        if i == bukv:
            slov.append(norm)
    return slov
a = open('cities.txt', 'r', encoding='utf-8')
file = []
for i in a:
    i = str(i)
    i = i.replace('\n','')
    i = i.lower()
    file.append(i)
otvet = input('Ваше слово:')

win = 0
lose = 0
while win == 0 and lose == 0 :
    tg = otvet in file
    if tg == True:
        file.remove(otvet)
    elif tg != True:
        lose +=1
        break
    bukv = otvet[len(otvet)-1]
    ai = robot(bukv,file)
    rand = randint(0,len(ai))
    otvet_ai = ai[rand]
    print(otvet_ai)
    
    tg_ai = otvet_ai in file
    
    if tg_ai == True:
        file.remove(otvet_ai)
    elif tg_ai != True:
        win += 1
        break
    otvet = input('Ваше слово:')
if win == 1:
    print('ВЫ ПОБЕДИЛИ')
else:
    print('Вы проиграли')
