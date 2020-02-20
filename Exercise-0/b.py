def foo():
	print("this is a test")
	print("I am happy auto-indent is achived")
	if True:
		print("I am happy the if condition indentation looks nice")
	
	for i in range(5):
		print(f"This is {i}")

if __name__ == "__main__":
	foo()
	print("auto-indent by 1 is achieved by using the indent in previous line, so next line after [if] and [for] command do not add one indent automatically")
