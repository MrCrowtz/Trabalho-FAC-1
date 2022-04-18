def leitura():
    with open('entrada.txt','r') as ler:
        valores=[]
        for linha in open('entrada.txt').readlines():
            valores.append(ler.readlines())
    pares=[]
    for i in range(0,len(valores),2):
        pares.append(valores[i:i+2])
    return (pares)
pares=leitura()
print(len(pares))
