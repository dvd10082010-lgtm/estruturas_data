

def find_minor(lista):
    minor = lista[0]
    for i in lista:
        if minor > i :
            minor = i
    return minor

def find_major(lista):
    major = lista[0]
    for i in lista:
        if major < i: 
            major = i
    return major
