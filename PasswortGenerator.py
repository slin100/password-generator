from time import sleep
import string
zahl=string.ascii_letters
zahl1 = string.ascii_letters + string.digits + string.punctuation
from random import randint
for i in range(200):
    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words -1)
        word_picked = words[num_picked]
        return word_picked
    while True:
        for i in range(20):
            print(pick(zahl),sep="",end="")
        break
    
    print(sep="\n")
    print('oder',sep="\n")

    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words -1)
        word_picked = words[num_picked]
        return word_picked
    while True:
        for i in range(20):
            print(pick(zahl1),sep="",end="")
        input()
        break
    print(sep="\n")
