from dinossauro import Dinossauro
from objetos import *
from time import sleep


# ajusar o limite de pulo no final
# definir o que acontece quando acaba a estamina // uma boa ideia pode ser não deixar ele fazer o que não tem estamina suficiente


dino = Dinossauro()
block = Bloco()
lava = Lava()
cacto = Cacto()
moeda = Moeda()
vazio = Vazio()
maca = Maca()
mob = Pessoa(1)
fim = Bandeira()

 

mapa_sup = [dino, vazio] + [maca, mob, mob, vazio, vazio, maca, mob, vazio, mob, maca, vazio, mob] * 4 + [fim]
mapa_terreno = [block, block, lava, lava, block, lava, block, lava, block, block,] * 5 + [block]

mapa_legal_sup = ''.join([obj.aparencia() for obj in mapa_sup])
mapa_legal = ''.join([obj.aparencia() for obj in mapa_terreno])

def imprimir_mapa(mapa_sup, mapa_terreno):
    print(mapa_sup)
    print(mapa_terreno)
    print()

imprimir_mapa(mapa_legal_sup, mapa_legal)

while True:
    if '☠️' in mapa_legal_sup or '🎖️' in mapa_legal_sup:
        break
    
    resposta = int(input("Digite um número: "))
    match resposta:
        case 1:
            mapa_legal_sup = dino.passo(mapa_legal_sup, maca, mob, fim)
            pos = mapa_legal_sup.find(dino.aparencia())
            if mapa_legal[pos] == lava.aparencia():
                mapa_legal_sup = lava.atacar(dino, mapa_legal_sup)        
        case 2:
            mapa_legal_sup = dino.pula(mapa_legal_sup, maca, mob, fim)
            pos = mapa_legal_sup.find(dino.aparencia())
            if mapa_legal[pos] == lava.aparencia():
                mapa_legal_sup = lava.atacar(dino, mapa_legal_sup)   
        case 22:
            mapa_legal_sup = dino.pula_pula(mapa_legal_sup, maca, mob, fim)
            pos = mapa_legal_sup.find(dino.aparencia())
            
            if mapa_legal[pos] == lava.aparencia():
                mapa_legal_sup = lava.atacar(dino, mapa_legal_sup)  
            
    imprimir_mapa(mapa_legal_sup, mapa_legal)




