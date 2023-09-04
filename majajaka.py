import random
def sifre_uret (uzunluk):
    
    elements = "097654safbrk"
    password = ""
    for i in range(uzunluk):
        password += random.choice(elements)

    return password
