import sys

_, file_name = sys.argv

f = open(file_name)
print(f.readlines())
