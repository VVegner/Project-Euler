#!python3

f,s = 0, 1 
fib = []
flag = 1
evens = 0

while f+s <4000000:
	if flag:
		f = f + s
		fib.append(f)
		print(f)
	else:
		s = f + s
		fib.append(s)
		print(s)
	flag = not flag

for i in fib:
	if not (i%2):
		evens += i
		print(i)

print (evens)