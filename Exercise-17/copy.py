import os
import sys

_, from_f, to_f = sys.argv

if not os.path.exists(from_f):
	raise Exception(f"{from_f} is not found.")

f_1, f_2 = open(from_f), open(to_f, 'w')
f_2.write(f_1.read())
f_1.close()
f_2.close()



