class Objeto:
    def __init__(self, quantidade: int):
        self.quantidade = quantidade
        self.emoji = ''


class Melancia(Objeto):
    def __init__(self):
        self.emoji = '🍉'

    def som(self):
        print("Dino pegou o vazio")

    def aparencia(self):
       return self.emoji 

class Vazio(Objeto):
    def __init__(self, emoji='🟦'):
        self.emoji = emoji

    def som(self):
        print("Dino pegou a maçã")

    def aparencia(self):
       return self.emoji 

class Maca(Objeto):
    def __init__(self, emoji='🍎'):
        self.emoji = emoji
        self.estamina = 5
        self.vida = 1

    def regenerar(self):
        return self.vida, self.estamina

    def som(self):
        print("Dino pegou a maçã")

    def aparencia(self):
       return self.emoji

class Bloco(Objeto):
    def __init__(self, emoji='🟫'):
        self.emoji = emoji

    def som(self):
        print("Dino passou o bloco")

    def aparencia(self):
        return self.emoji
    
class Lava(Objeto):
    def __init__(self, emoji='🔥'):
        self.emoji = emoji
        self.dano = 3

    def atacar(self, dino, mapa_atual):
        dino.vida -= self.dano
        mapa_final = mapa_atual
        if (dino.vida <= 0):
            mapa_final = dino.morte(mapa_atual)
        else:
            print(f"Você pulou na lava, sua vida agora é {dino.vida}")  

        return mapa_final

    def som(self):
        print("Dino pulou a lava")

    def aparencia(self):
        return self.emoji

class Moeda(Objeto):
    def __init__(self, emoji='🪙 '):
        self.emoji = emoji
    def som(self):
        print("Dino pegou a moeda")

    def aparencia(self):
        return self.emoji


class Cacto(Objeto):
    def __init__(self, emoji='🌵'):
        self.emoji = emoji

    def som(self):
        print("Dino pulou o cacto")

    def aparencia(self):
        return self.emoji

class Pessoa(Objeto):
    def __init__(self, nivel, emoji='👺'):
        self.nivel = nivel
        self.dano = 1
        self.vida = 5
        self.emoji = emoji

    def aparencia(self):
        return self.emoji

    def lvl(self):
        if nivel > 3:
            self.dano = 4

        elif nivel > 5:
            self.dano = 8

        elif nivel > 8:
            self.dano = 11

        elif nivel > 12:
            self.dano = 15

    def atacar(self):
        return self.dano 

    def regenera(self):
        self.vida += 5

    def som(self):
        print("Dino bateu na pessoa")

class Bandeira(Objeto):
    def __init__(self, emoji= '🎈'):
        self.emoji = emoji

    def aparencia (self):
        return self.emoji
