import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%)": "Make a class named %%% that is-a %%%",
	"class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ taking self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** taking self and @@@ as paramters.",
	"*** = %%%()": "set *** to an instance of class %%%",
	"***.***(@@@)": "From *** get the *** function, and call it with parameter self and @@@",
	"***.*** = '***'": "From *** get the *** attribute and set it to '***'"
}


