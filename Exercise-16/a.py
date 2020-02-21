import sys

_, file_name = sys.argv

print(f"""
We're going to erase {file_name}.
If you do not want it, press CTRL-C.
If you do want it, press RETURN.
""")

input("> ")

print("Open the file...")
target = open(file_name, "w+")

print("Truncate the file")
target.truncate()

print("Now input 3 lines")
l_1 = input("Line 1: ")
l_2 = input("Line 2: ")
l_3 = input("Line 3: ")

print(f"Write to file {file_name}")
target.write(l_1 + "\n" + l_2 + "\n" + l_3 + "\n")

target.close()

