import sys

def foo():
	print("run foo")
	#sys.exit(0)

def main():
	foo()
	print("run main")
	return

if __name__ == "__main__":
	main()
