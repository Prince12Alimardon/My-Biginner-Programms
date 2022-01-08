password=input()
assert ' ' not in password
finding=''
n=0
k=0
nums='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
try:
	while k<len(password):
		if password==finding:
			break
		else:
			for i in nums:
				for j in password[n]:
					if j is i:
						finding+=j
						print(finding)
						n+=1
						break
					else:
						print(i,'is not in the password')
						continue
	k+=1
except:
	print('Password is',finding)
	print('==============\nACCESS GRANTED\n==============')
