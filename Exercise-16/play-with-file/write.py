import sys
import os

# test whether open with mode "w" and "a" will create a file
if os.path.exists("f-1") or os.path.exists("f-2"):
	raise Exception("file already exists")

open("f-1", "w")
open("f-2", "a")

if not os.path.exists("f-1"):
	raise Exception("file does not exist")
if not os.path.exists("f-2"):
	raise Exception("file does not exits")

os.remove("f-1")
os.remove("f-2")

# test whether open with mode "w" will truncate the file.
f_3 = open("f-3", 'w')
f_3.write("this is a new file")
f_3.close()

f_3 = open("f-3", 'r')
if not f_3.read():
	raise Exception("file is empty")
f_3.close()

f_3 = open("f-3", "w")
f_3.close()

f_3 = open("f-3", "r")
if f_3.read():
	raise Exception("file is not empty")
f_3.close()

os.remove("f-3")

# write string in the middle file
f_4 = open("f-4", "r+")
f_4.write("".join([str(i) for i in range(10)]))
f_4.seek(0)
if f_4.read() != "0123456789":
	raise Exception("write-in has error")

f_4.seek(3)
f_4.write("###")
f_4.seek(0)
if f_4.read() != "012###6789":
	raise Exception("error when writing in the middle")
os.remove("f-4")

