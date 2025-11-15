#level 1
import random , string
def random_user_id():
    s = string.ascii_letters + string.digits
    id = ''
    for i in range(6):
        id += random.choice(s)
    return id

print(random_user_id())

def id_gen_by_user():
    char = int(input('Enter number of characters: '))
    num = int(input('Enter number of IDs: '))
    s = string.ascii_letters + string.digits
    
    for i in range(num):
        id = ''
        for i in range(char):
            id += random.choice(s)
        print(id)

id_gen_by_user()

def rgp_color_gen():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    return f"rgb({r},{g},{b})"
print(rgp_color_gen())

#level 3
def randomNumber():
    s = set()
    array = []
    while True:
        if len(s)==7:
            array = s
            return array
        num = random.randint(0,10)
        s.add(num)

print(randomNumber())
