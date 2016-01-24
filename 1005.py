n = input()
lst = raw_input()
lst = lst.split()
i = 0
while i<n:
    lst[i] = int(lst[i])
    i+=1

def cal(item):
    a=[item]
    while item!=1:
        if item % 2==0:
            item/=2
        else:
            item = (3*item +1)/2
        a.append(item)
    return a
x=[]
i=0
while i<n:
    if i==0:
        x.append(cal(lst[i]))
    elif lst[i] not in x[i-1]:
        x.append(cal(lst[i]))
    i+=1

i=0
while i<n:
    if x[i][0]