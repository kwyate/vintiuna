import random
valor = ""
fig = ""
usuario = []


def list_cartas():
    cartas = ["A","2","3","4","5","6","7","8","9","10", "J","Q","K"]
    figura = ["c","d","p","t"]
    valor = random.choice(cartas)
    fig = random.choice(figura)
    return valor, fig

def random_cartas():
    
    #valor2 = random(0,4)
    v = list_cartas()
    return v

def repartir(turno):
    
    #usuario = []
    if turno == 0:
        usuario.append(list_cartas())
        usuario.append(list_cartas())
        print("pase")
        
    else:
        usuario.append(list_cartas())
        print("pase2")
        turno +=1
        
    return usuario

def suma_cartas():
    for i in range(0, len(repartir(0))):
        val1 = repartir(0)[i][0]
        val2 = repartir(0)[i][0]
        print (val1, val2)
        if val1 == "A" :
            val1 = 11
        elif val2 == "A":
            val2 = 11
        elif val1 in ["J", "Q", "K" ]:
            val1 = 10
        elif val2 in ["J", "Q", "K"]:
            val2 = 10
    
        
    print (val1, val2)    
    
    return int(val1) + int(val2)
    
def jugar():
    #print (repartir(0))
    print (sumar_cartas(0))
    while True:
        
        desicion = input("Desea otra carta ? ")
        if desicion == "si":
            print(repartir(1))
        else:
            pass
    
#jugar()

print(len(repartir(0)))




