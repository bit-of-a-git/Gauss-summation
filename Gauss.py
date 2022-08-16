def printgauss():
	print("I will add up all the numbers from 0 to any number you enter. Please enter a number.")
	i = input()
	total = 0
	for number in range(int(i) + 1):
		total = total + number
	print("The total from 0 to " + str(i) + " is equal to " + str(total) + ".")

printgauss()
