import random

n=input('How many games you want?:')
n=int(n)
game=[]
b=0
for i in range(n):
    normal=list(range(1,36))
    pb_list=list(range(1,21))
    b=b+1
    for i in range(7):
        number=random.choice(normal)
        normal.remove(number)
        game.append(number)

    pb=random.choice(pb_list)
    game.append('Powerball')
    game.append(pb)
    gb='Game '+str(b)
    print(gb,game)
    game=[]

print('Good Luck and All the Best~')
input()
