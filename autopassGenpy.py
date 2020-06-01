
"""
Author: Umar Farooq

Why to create strong password?

Because it makes the chances of hackers bruteforcing your password to almost 0%

Simply to not get hacked!

"""



import random

import string



# Password level is Strong!

# Creates a alphanumeric password of `n` chars 

def create_password(n):

    allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

    passphrase = []

    for i in range(n):

        tmp = random.choice(allChars)

        passphrase.append(tmp)

    

    res = "".join(passphrase)

    return res

print(("-" * 30) + "\n auto Password Generator (8,16,32,64)\n" +"\n by UMAR FAROOQ\n" + ("-" * 30))   

# Test 0
test0 = create_password(8)

print("password with length 8\n",test0, "\n")

# Test 1
test1 = create_password(16)

print("password with length 16\n",test1, "\n")



# Test 2 

test2 = create_password(32)

print("password with length 32\n",test2, "\n")


# Test 3 

test3 = create_password(64)

print("password with length 64\n",test3, "\n")

