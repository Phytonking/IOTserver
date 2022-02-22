import hashlib
import random


def to_binary(password):
    number = 0
    for x in range(0, len(password)):
        binary_list = []
        binary_list.append(ord(x))
    for n in binary_list:
        number += n

    return bin(number)
        


def password_hash(password):
    m = hashlib.sha512()
    m.update(to_binary(password))
    return m.digest()




def create_user_id():
    user_id = ""
    for x in range(0,275):
        user_id += chr(random.randint(33,126))
    print(user_id)
    return user_id    