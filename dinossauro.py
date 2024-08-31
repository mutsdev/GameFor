class Dinossauro:
    def __init__(self, xp=15, nome="Mutz", emoji='🦖'):
        self.nome = nome

        self.vida = 10
        self.estamina = 30
        self.ataque = 3
        self.moedas = 0

        self.xp = xp
        self.emoji = emoji
        
    def pega(self):
        self.estamina -= 1
        print("Pega")
    
    def passo(self, mapa_atual, maca, mob):
        pos = mapa_atual.find(self.emoji)

        prox = mapa_atual[pos + 1]
        current = mapa_atual[pos]
        if (prox == maca.aparencia()):
            print("\033[32mVida regenedara\033[0m")
            life, energery = maca.regenerar()
            self.estamina += energery
            self.vida += life

        elif (prox == mob.aparencia()):
            print(f"\033[31mMonento da Luta | Vida atual: {self.vida}\033[0m")
        
            while self.vida > 0 and mob.vida > 0:
                mob.vida -= self.bate()
                self.vida -= mob.atacar()

            if self.vida <= 0:
                self.morte()
                mapa_atual = mapa_atual.replace(current, "☠️ ", 1)
                return mapa_atual

            self.xp += 5
            self.moedas += 2

            mob.regenera()
        else:
            print(f"\033[36m{self.nome} deu um passo \033[0m")

        mapa_atual = mapa_atual.replace(prox, current, 1)

        mapa_atual = mapa_atual.replace(current, "🌌", 1)

        return mapa_atual
        
    def pula(self):
        self.estamina -= 3
        

    def morte(self):
        print("\033[31mVocê morreu!\033[0m")
        print(f"\033[41mOs resultados do dino {self.nome} foram: \033[0m")
        print(f"\033[44mEstamina -> {self.estamina} \033[0m")
        print(f"\033[47mXP -> {self.xp} \033[0m")
        print(f"\033[43mMoedas -> {self.moedas} \033[0m")

    def bate(self):
        self.estamina -= 4
        return self.ataque

    def aparencia(self):
        return self.emoji