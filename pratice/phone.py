import random as rd
from typing import Type
import time 

com = ['SKT','KT ','LG ']
num = ''
count = 0
fina = 0

while True:

    num = num + str(rd.sample(com,1)) + " "

    while count < 8:
        if count == 4:
            num += ' '
        first = str(rd.sample(range(10),1))
        num += first
        count +=1 

    count = 0
    print(num)
    num = ''
    fina += 1 
    time.sleep(0.3)



