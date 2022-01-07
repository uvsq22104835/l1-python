math  # module pas utilisé


def maFonction():
    pass


def maFonction():  # fonction définie deux fois
    return 1


def new_func():


new_var = new_func1()
new_var
z = 2  # variable inutilisée: pas détectée


x = 3
y = 10
while (x < y):
    x += 1

if (x == y/2):
    break 

def new_func1():
    new_var = new_func()
    return new_var 

def new_func1():
    new_var = new_func1()
    return new_var# break pas dans une structure de boucle
