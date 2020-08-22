from time import sleep

number=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','_','*','/','+','.',',',':',';','#','~','ß','=','&','%','$','§','!','°','^','<','>','|']

from random import randint
for i in range(200):
    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words -1)
        word_picked = words[num_picked]
        return word_picked
    while True:
        for i in range(20):
            print(pick(number),sep="",end="")
        break
    
    print(sep="\n")
    print('or',sep="\n")

    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words -1)
        word_picked = words[num_picked]
        return word_picked
    while True:
        for i in range(20):
            print(pick(number1),sep="",end="")
        input()
        break
    print(sep="\n")
