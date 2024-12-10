import string
import random
def randomString(lenght:int):
    return "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lenght))


# print(randomString(9))