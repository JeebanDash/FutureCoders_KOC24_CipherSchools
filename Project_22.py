n=int(input('How many student??: '))
print()
dict1={}

for i in range(n):
    name=input('Enter name of student: ')
    marks=int(input('Enter marks of student'))
    dict1[name]=marks
    print()


sorted_dict={k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
inrank=n
rankdict={}

for i in sorted_dict:
    rankdict[i]=inrank
    inrank=inrank-1

update_dict={}
for i in sorted_dict:
    a=int(input('Enter marks to added for {}: '.format(i)))
    update_dict[i]=a+sorted_dict.get(i)

update_dict={k: v for k, v in sorted(update_dict.items(), key=lambda item: item[1])}

larank=n
rankdictnew={}

for i in update_dict:


    
    rankdictnew[i]=larank
    larank=larank-1

print()

print('**********************************************************************************************************')

for i in rankdictnew:
    print('rank {}, Name: {}, Jump: {}'.format(rankdictnew.get(i),i,(rankdict.get(i))-(rankdictnew.get(i))))
    print()
print('**********************************************************************************************************')
