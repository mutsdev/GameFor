from dinossauro import Dinossauro
from objetos import *
from time import sleep


# ajusar o limite de pulo no final
# Melhorar sistema de combate

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
            if dino.estamina - 3 >= 0:
                mapa_legal_sup = dino.pula(mapa_legal_sup, maca, mob, fim)
                pos = mapa_legal_sup.find(dino.aparencia())
                if mapa_legal[pos] == lava.aparencia():
                    mapa_legal_sup = lava.atacar(dino, mapa_legal_sup)   
            else:
                print(f"{dino.nome} não tem estamina suficiente para pular")
                mapa_legal_sup = dino.passo(mapa_legal_sup, maca, mob, fim)

        case 22:
            if dino.estamina - 7 >= 0:
                mapa_legal_sup = dino.pula_pula(mapa_legal_sup, maca, mob, fim)
                pos = mapa_legal_sup.find(dino.aparencia())
                
                if mapa_legal[pos] == lava.aparencia():
                    mapa_legal_sup = lava.atacar(dino, mapa_legal_sup)  
            else:
                if dino.estamina < 3:
                    mapa_legal_sup = dino.passo(mapa_legal_sup, maca, mob, fim)
                else:
                    nova_resposta = int(input(f"O dino {dino.nome} tem apenas {dino.estamina} de estamina, deseja pular ou dar um passo? "))
                    if nova_resposta == 2:
                        mapa_legal_sup = dino.pula(mapa_legal_sup, maca, mob, fim)
                    else:
                        print(f"{dino.nome} não tem estamina suficiente para pular")
                        mapa_legal_sup = dino.passo(mapa_legal_sup, maca, mob, fim)

    imprimir_mapa(mapa_legal_sup, mapa_legal)




