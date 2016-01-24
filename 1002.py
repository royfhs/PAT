a=raw_input()
i=0
s=0
while i<len(a):
	s+=int(a[i])
	i+=1
i=0
d={0:"ling",1:"yi",2:"er",3:"san",4:"si",5:"wu",6:"liu",7:"qi",8:"ba",9:"jiu"}
s=str(s)
while i<len(s):
	print d[int(s[i])],
	i+=1