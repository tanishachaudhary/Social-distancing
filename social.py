def main(N,P):
	lst = []
	lst.append(1)
	lst.append(N)
	if(P==1):
		print(1)
	elif(P==2):
		print(N)
	else:
		start = 1
		end = N
		i = 3
		while(True):
			mid = int((start+end)/2)
			if(i==P):
				print(mid)
				break
			m = lst.index(start)
			lst.insert(m+1,mid)
			sut = []
			for j in range(len(lst)-1):
				l = lst[j+1]-lst[j]
				sut.append(l)
				maxi = max(sut)
				s = sut.index(maxi)
				start = lst[s]
				end = lst[s+1]
			i+=1
n = int(input("Enter the no. of seats:"))
p = int(input("Enter the no. of person entering:"))
if(p>n):
	print("All seats full!!!")
else:
	print("This person should be seated on seat no.:",end = " ")
	main(n,p)
