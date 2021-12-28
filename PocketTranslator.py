def trans(word):
        for key, value in trl.items():          
            if word in key: 
                return value
            else:
                return word
            

from collections import OrderedDict
x = []
z = []
n = int(input())
trl = OrderedDict()

for i in range(0, n):
    lst = input()
    lst = lst.split()
    for j in range (0, len(lst)):
        lst[j] = str(lst[j]) 
    for item in lst[1:]:
        trl[item] = lst[0]
#    x.append(lst[0])
#    z.append(lst[1:]) 
#    trl[x[0]] = x[1]
#trl = OrderedDict((zip(x,z)))
sntc = input()
words = sntc.split()
trlsen = ''
'''
for word in sntc:
    if word in trl:
        trlsen += trl[word] + ' '
    else:
        trlsen += word + ' '
'''
for word in words:
    trlsen += trl.get(word,word) +' '
print(trlsen)
