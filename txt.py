# hello world

print("Hello World!")

# hello name

name = raw_input("What is your name? ")
print("Hello, " + name + "!")

# guess the number

num = 17
while True:
	guess = int(raw_input("What is your number? "))

	if guess == num:
		print("You win")
		break
	else:
		print("You lose")