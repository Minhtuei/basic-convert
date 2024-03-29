hihi='Times'
hehe='Hong'
huhu='2'
with open('setting.txt','w+') as fw:
    fw.write(f'Font: {hihi}\nBG: {hehe}\nTP: {huhu}')


with open('setting.txt','r') as fr:
    hehe=fr.readlines()
    print(hehe)
for i in hehe:
    if 'Font' in i:
        print(i[6:None].replace('\n',''))
    if 'BG' in i:
        print(i[4:None].replace('\n',''))
    if 'TP' in i:
        print(i[4:5])