mapa_legal_sup = ''.join([obj.aparencia() for obj in mapa_sup])
mapa_legal = ''.join([obj.aparencia() for obj in mapa_terreno])

def imprimir_mapa(mapa_sup, mapa_terreno):
    print(mapa_sup)
    print(mapa_terreno)
    print()

imprimir_mapa(mapa_legal_sup, mapa_legal)

while True:
    resposta = int(input("Digite um número: "))

    match resposta:
        case 1:
            mapa_legal_sup = dino.passo(mapa_legal_sup, maca, mob)
            pos = mapa_legal_sup.find(dino.aparencia())
            if mapa_legal[pos] == lava.aparencia():
                dino.vida -= lava.atacar()
                print(f"Você pulou na lava, sua vida agora é {dino.vida}")         
        case 2:
            continue

    imprimir_mapa(mapa_legal_sup, mapa_legal)