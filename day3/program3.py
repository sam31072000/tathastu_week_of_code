a="abcdefghijklmnopqrstuvwxyz "
s=input('Enter the string: ')
r=''
for i in s:
	if i in a:
		a=a.replace(i,'')
		r+=i
print(r)
