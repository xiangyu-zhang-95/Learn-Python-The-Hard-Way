import sys

def foo_1():
	print("run foo_1")
	sys.exit(0)

def foo_2():
	print("run foo_2")
	return

def main_1():
	foo_1()
	print("run main_1")

def main_2():
	foo_2()
	print("run main_2")

def foo_3():
	print("run foo_3")
	sys.exit(1)

def main_3():
	foo_3()

def main_4():
	exit(4)

if __name__ == "__main__":
	if sys.argv[1] == "1":
		# main_1() should print out "run foo_1"
		main_1()
	
	if sys.argv[1] == "2":
		# main_2() should print out "run foo_2" and "run main_2"
		main_2()
	
	if sys.argv[1] == "3":
		# main_3 print out "run foo_3", the exit code is 1.
		main_3()
	
	if sys.argv[1] == "4":
		# main_4 print out nothing, the exit code is 4.
		main_4()

