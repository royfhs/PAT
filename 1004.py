n=input()
i=0
a=[]
max_score=0
min_score=100
while i<n:
	a.append(raw_input().split())
	a[i][2]=int(a[i][2])
	if a[i][2] > max_score:
		max_name=a[i]
		max_score=a[i][2]

	if a[i][2] < min_score:
		min_name=a[i]
		min_score=a[i][2]
	i+=1
print max_name[0],
print max_name[1]
print min_name[0],
print min_name[1]
