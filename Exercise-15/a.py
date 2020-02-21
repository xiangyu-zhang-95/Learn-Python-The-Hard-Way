from sys import argv

_, file_name = argv

txt = open(file_name)

print(f"This is your file: {file_name}")
print(txt.read())

print("I' ll ask you some thing: ")
file_again = input(">")

txt_again=open(file_again)
print(txt_again.read())

