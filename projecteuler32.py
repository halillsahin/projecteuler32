import itertools
rakamlar=[1,2,3,4,5,6,7,8,9]
a=0
z=set()
permutasyon=list(itertools.permutations(rakamlar,9))
for sayı in permutasyon :
    sayı1=sayı[0]*10+sayı[1]
    sayı2=sayı[2]*100+sayı[3]*10+sayı[4]
    sayı3=sayı[5]*1000+sayı[6]*100+sayı[7]*10+sayı[8]
    if sayı3==sayı1*sayı2:
        z.add(sayı3)
for i in permutasyon:
    b=i[0]
    c=i[1]*1000+i[2]*100+i[3]*10+i[4]
    d=i[5]*1000+i[6]*100+i[7]*10+i[8]
    if d ==b*c :
        z.add(d)







print(sum(z))        
        

    