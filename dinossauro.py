class Dinossauro:
    def __init__(self, xp=15, nome="Mutz", emoji='🦖'):
        self.nome = nome

        self.vida = 20
        self.estamina = 20
        self.ataque = 3
        self.moedas = 0

        self.xp = xp
        self.emoji = emoji
        
    def pega(self):
        self.estamina -= 1
        print("Pega")
    
    def passo(self, mapa_atual, maca, mob, fim):
        pos = mapa_atual.find(self.emoji)

        prox = mapa_atual[pos + 1]
        current = mapa_atual[pos]

        if (prox == fim.aparencia()):
            mapa_atual = self.win(mapa_atual, fim)
            return mapa_atual

        elif (prox == maca.aparencia()):
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
            
                return self.morte(mapa_atual)

            self.xp += 5
            self.moedas += 2

            mob.regenera()
        else:
            print(f"\033[36m{self.nome} deu um passo \033[0m")

        
        mapa_atual = mapa_atual.replace(prox, current, 1)

        mapa_atual = mapa_atual.replace(current, "🌌", 1)

        return mapa_atual
        
    def pula(self, mapa_atual, maca, mob, fim):
        self.estamina -= 3

        pos = mapa_atual.find(self.emoji)
        p1 = mapa_atual[pos + 1]
        p2 = mapa_atual[pos + 2]

        if (p1 == fim.aparencia() or p2 == fim.aparencia()):
            mapa_atual = self.win(mapa_atual, fim)
            return mapa_atual

        elif (p2 == maca.aparencia()):
            print("\033[32mVida regenedara\033[0m")
            life, energery = maca.regenerar()
            self.estamina += energery
            self.vida += life

        elif (p2 == mob.aparencia()):
            print(f"\033[31mMonento da Luta | Vida atual: {self.vida}\033[0m")
        
            while self.vida > 0 and mob.vida > 0:
                mob.vida -= self.bate()
                self.vida -= mob.atacar()

            if self.vida <= 0:
                return self.morte(mapa_atual)

            self.xp += 5
            self.moedas += 2

            mob.regenera()
        else:
            print(f"\033[36m{self.nome} deu um passo \033[0m")

        mapa_atual = mapa_atual.replace(p1, "🌌", 1)
        mapa_atual = mapa_atual.replace(self.emoji, "🌌", 1)
        mapa_atual = mapa_atual.replace(p2, self.emoji, 1)

        return mapa_atual

    def pula_pula(self, mapa_atual, maca, mob, fim):
        self.estamina -= 7

        pos = mapa_atual.find(self.emoji)
        p1 = mapa_atual[pos + 1]
        p2 = mapa_atual[pos + 2]
        p3 = mapa_atual[pos + 3]
        final = fim.aparencia() 

        if p1 == final or p2 == final or p3 == final:
            mapa_atual = self.win(mapa_atual, fim)
            return mapa_atual
        
        elif (p3 == maca.aparencia()):
            print("\033[32mVida regenedara\033[0m")
            life, energery = maca.regenerar()
            self.estamina += energery
            self.vida += life

        elif (p3 == mob.aparencia()):
            print(f"\033[31mMonento da Luta | Vida atual: {self.vida}\033[0m")
        
            while self.vida > 0 and mob.vida > 0:
                mob.vida -= self.bate()
                self.vida -= mob.atacar()

            if self.vida <= 0:
                self.morte(mapa_atual)
                
                return mapa_atual

            self.xp += 5
            self.moedas += 2

            mob.regenera()
        else:
            print(f"\033[36m{self.nome} deu um passo \033[0m")

        print(f"\033[36m{self.nome} deu um salto duplo, agora sua estamina é {self.estamina}\033[0m")
        mapa_atual = mapa_atual.replace(p2, "🌌", 1)
        mapa_atual = mapa_atual.replace(p1, "🌌", 1)
        mapa_atual = mapa_atual.replace(p3, self.emoji, 1)
        mapa_atual = mapa_atual.replace(self.emoji, "🌌", 1)

        return mapa_atual

    def morte(self, mapa_atual):
        print("\033[31mVocê morreu!\033[0m")
        print(f"\033[41mOs resultados do dino {self.nome} foram: \033[0m")
        print(f"\033[44mEstamina -> {self.estamina} \033[0m")
        print(f"\033[47mXP -> {self.xp} \033[0m")
        print(f"\033[43mMoedas -> {self.moedas} \033[0m")
        mapa_atual = mapa_atual.replace(self.emoji, "☠️ ", 1)

        return mapa_atual

    def win(self, mapa_atual, fim):
        print("\033[31mVocê ganahou!\033[0m")
        print(f"\033[41mOs resultados finais do dino {self.nome} foram: \033[0m")
        print(f"\033[33mVida -> {self.vida} \033[0m")
        print(f"\033[44mEstamina -> {self.estamina} \033[0m")
        print(f"\033[47mXP -> {self.xp} \033[0m")
        print(f"\033[43mMoedas -> {self.moedas} \033[0m")
        mapa_atual = mapa_atual.replace(fim.aparencia(), "🎖️ ", 1)
        mapa_atual = mapa_atual.replace(self.emoji, "🌌", 1)

        return mapa_atual

    def bate(self):
        self.estamina -= 4
        return self.ataque

    def aparencia(self):
        return self.emoji