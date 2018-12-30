import random
'''
Answer the question Game in Sbeam 
Programmed by python
By Velocity
'''

def main():
	a = random.randint(1, 99)
	b = random.randint(1, 99)
	print("Welcome to answer the question. See how many points you can get! ")
	print("To quit just press enter before you answer a question. ")

	point = 0
	print("Question %d + %d =? " % (a, b), end="")
	ans = input()
	while ans.isdigit():
		if a + b == int(ans):
			point += 1
			print("You are right. You have %d point" % point)
		else:
			print("You are wrong. You have %d point" % point)
		a = random.randint(1, 99)
		b = random.randint(1, 99)
		print("Question %d + %d =? " % (a, b), end="")
		ans = input()
		
	print("Finally, you have %d point" % point)
	input()

if __name__ == "__main__":
	main()