try:
	while True:
		print("in the while loop")
		decision = input("continue? ")
		if decision == "yes":
			continue
except EOFError:
	print("Bye")

