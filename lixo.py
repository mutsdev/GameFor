# while True:
#     jogada = input("Digite sua jogada: ")
#     match jogada:
#         case 1:
#             if mapa_terreno[pos] == block:
#                 dino.passo()
#             else:
#                 print("Dino morreu")
#         case 2:
#             if mapa_terreno[pos] == lava or mapa_sup[pos] == cacto:
#                 dino.pula()
#             else:
#                 print("Você gastou estamina atoa")
#         case 3:
#             if mapa_sup[pos] == mob:
#                 while (true):
#                     if (mob.vida() > 0 and dino.vida() > 0):
#                         mob.atacar()
#                         dino.bate()
#                     else:
#                         break 

    # if op == block:
    #     dino.passo()

    # elif op == lava or op == cacto:
    #     dino.pula()

    # elif op == moeda or op == maca:
    #     dino.pega()

    # elif op == mob:
    #     dino.bate()




from dinossauro import Dinossauro
from objetos import *

dino = Dinossauro()
block = Bloco()
lava = Lava()
cacto = Cacto()
moeda = Moeda()
maca = Maça()
mob = Pessoa(1)
vazio = Vazio(1)

mapa_sup = [dino, vazio, vazio, vazio, vazio, vazio, vazio, vazio]
mapa_terreno = [block, block, lava, lava, block, lava, block, block]

mapa_legal = mapa_legal_sup = ''

for op in mapa_terreno:
    mapa_legal +=(op.aparencia())

for op in mapa_sup:
    mapa_legal_sup += op.aparencia()
    

print(mapa_legal_sup)
print(mapa_legal)

print()
print(len(mapa_legal))
for i in range(1, 8):
    atual = mapa_legal_sup[i]
    print(mapa_legal_sup)
    print(mapa_legal)
    mapa_legal_sup = mapa_legal_sup.replace(vazio.aparencia(), dino.aparencia(),1)    
    # if (atual != dino.aparencia()):
    mapa_legal_sup = mapa_legal_sup.replace(dino.aparencia(), vazio.aparencia(),1)

print(mapa_legal_sup)
print(mapa_legal)


for i in range(2, len(mapa_legal)):
    atual = mapa_legal_sup[i]    
    mapa_legal_sup = mapa_legal_sup.replace(maca.aparencia(), dino.aparencia(),1)    
    mapa_legal_sup = mapa_legal_sup.replace(dino.aparencia(), vazio.aparencia(),1)







# for i in range(1, len(mapa_legal_sup)):

#     atual = mapa_legal_sup[i]
#     print(f"A posição atual é {i} e representa -> {atual}")

#     if atual == maca.aparencia():
#         print("Dinossauro pegou a maca!")
#         dino.moedas += 1

#         mapa_legal_sup = mapa_legal_sup.replace("", dino.aparencia(), 1)
        
#     elif atual == vazio.aparencia():
#         mapa_legal_sup = mapa_legal_sup.replace("", dino.aparencia(), 1)

#     mapa_legal_sup = mapa_legal_sup.replace("", "", 1)

#     imprimir_mapa(mapa_legal_sup, mapa_legal)




# lista_alunos = []
# lista_bons_alunos = []

# print("Momento para adicionar o nome dos alunos da sua escola!")
# x = input("Adicione um aluno: (0 para parar): ")

# while x != '0':
#     lista_alunos.append(x)

#     x = input("Adicione um aluno: (0 para parar): ")
    
# print("A lista com os nomes dos alunos da sua escola é", lista_alunos)
# print()
# print("Momento para adicionar o nome dos melhores alunos do mundo!")
# y = input("Adicione um nome (600 para parar): ")

# while y != '600':
#     lista_bons_alunos.append(y)
#     y = input("Adicione um novo nome (600 para parar): ")

# print("A lista com os nomes dos melhores alunos do mundo é ", lista_bons_alunos)
# print()

# # Preciso verificar se tem algum aluno da minha escola na lista 
# # 
# #dos melhores do mundo, poderia me ajudar, sou apenas uma senhorinha sem conhecimentos tecnológicos

# for x in lista_alunos:
#     if x in lista_bons_alunos:
#         print(x,'esta na lista dos melhores do mundo')