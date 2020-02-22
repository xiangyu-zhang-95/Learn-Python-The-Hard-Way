# the first arg is: 1
python3 a.py 1


# the first arg is: 1+1
python3 a.py 1+1

# the first arg is: 1
a=1
python3 a.py $a

# the first arg is: 1+1
python3 a.py $a+1

# the first arg is: 2
python3 a.py $(($a+1))

