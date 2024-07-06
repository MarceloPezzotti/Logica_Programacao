class Pirata:
    def __init__(self, nome, categorias, recompensa):
        self.nome = nome
        self.categorias = categorias
        self.recompensa = recompensa
        self.ranking = self.definir_ranking(recompensa)
        self.ataque = "Ataque básico de pirata"
        
    def definir_ranking(self, recompensa):
        if recompensa <= 50000:
            return "E"
        elif 50001 <= recompensa <= 100000:
            return "D"
        elif 100001 <= recompensa <= 500000:
            return "C"
        elif 500001 <= recompensa <= 1000000:
            return "B"
        elif 1000001 <= recompensa <= 10000000:
            return "A"
        elif 10000001 <= recompensa <= 100000000:
            return "S"
        else:  # recompensa acima de 100000000
            return "S+"

    def __str__(self):
        return f"Pirata: {self.nome}, Categoria: {self.categorias}, Recompensa: {self.recompensa}, Ranking: {self.ranking}, Ataque: {self.ataque}"

class PirataAkumaNoMi(Pirata):
    def __init__(self, nome, categorias, recompensa, tipo_akuma_no_mi):
        super().__init__(nome, categorias, recompensa)
        self.tipo_akuma_no_mi = tipo_akuma_no_mi
        self.ataque = f"Ataque com a Akuma no Mi do tipo {self.tipo_akuma_no_mi}"

    def __str__(self):
        return super().__str__() + f", Tipo Akuma no Mi: {self.tipo_akuma_no_mi}"

class PirataSpadachim(Pirata):
    def __init__(self, nome, categorias, recompensa, estilo_espada):
        super().__init__(nome, categorias, recompensa)
        self.estilo_espada = estilo_espada
        self.ataque = f"Ataque com o estilo de espada {self.estilo_espada}"

    def __str__(self):
        return super().__str__() + f", Estilo de Espada: {self.estilo_espada}"

class Marinheiro:
    def __init__(self, nome,recompensa):
        self.nome = nome
        self.ranking = self.definir_patente(recompensa) 
        self.recompensa = recompensa
    
    def definir_patente(self, recompensa):
            
        if recompensa <= 50000:
            return "Cabo da Marinha"
        elif 50001 <= recompensa <= 100000:
            return "Tenente da Marinha"
        elif 100001 <= recompensa <= 500000:
            return "vice Captiao da Marinha"
        elif 500001 <= recompensa <= 1000000:
            return "Capitão da Marinha"
        elif 1000001 <= recompensa <= 10000000:
            return "Vice almirante da Marinha"
        elif 10000001 <= recompensa <= 100000000:
            return "Almirante da Marinha"
        else:  # recompensa acima de 100000000
            return "Almirante de Frota da Marinha"
    
 

    def __str__(self):
        return f"Marinheiro: {self.nome}, Patente: {self.ranking}"

# Coletando dados do usuário
nome_pirata = input("Digite o nome do pirata: ")
categorias_pirata = input("Digite a categoria do pirata: ")
recompensa_pirata = int(input("Digite a recompensa do pirata: "))

tipo_akuma_no_mi = input("Digite o tipo de Akuma no Mi do pirata (deixe em branco se não for aplicável): ").strip()
if tipo_akuma_no_mi:
    pirata = PirataAkumaNoMi(nome_pirata, categorias_pirata, recompensa_pirata, tipo_akuma_no_mi)
else:
    estilo_espada = input("Digite o estilo de espada do pirata (deixe em branco se não for aplicável): ").strip()
    if estilo_espada:
        pirata = PirataSpadachim(nome_pirata, categorias_pirata, recompensa_pirata, estilo_espada)
    else:
        pirata = Pirata(nome_pirata, categorias_pirata, recompensa_pirata)

nome_marinheiro = input("Digite o nome do marinheiro: ")
ranking_marinheiro = int(input("Digite a pontuação do marinheiro para verificar a patente: "))
marinheiro = Marinheiro(nome_marinheiro, ranking_marinheiro)

print(pirata)
print(marinheiro)
