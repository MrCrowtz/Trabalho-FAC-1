#função de ler o texto e devolver como lista e separando pares se tiver mais de um
def reading():
    with open('entrada.txt','r') as read:
        values=[]
        for line in open('entrada.txt').readlines():
            values.append(read.readlines())
    pairs=[]
    for i in range(0,len(values),2):
        pairs.append(values[i:i+2])
    return (pairs)
pairs=reading()
print(len(pairs))