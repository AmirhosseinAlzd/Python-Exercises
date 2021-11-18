import random
Boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
Girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
Couples = []
while len(Boys) != 0 :
    Couple = []
    boy = random.choice(Boys)
    Couple.append(boy)
    girl = random.choice(Girls)
    Couple.append(girl)
    Boys.pop(Boys.index(boy))
    Girls.pop(Girls.index(girl))
    Couples.append(Couple)

print(Couples)