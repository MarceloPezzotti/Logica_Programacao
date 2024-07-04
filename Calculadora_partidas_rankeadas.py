def calculadora_partidas_rankeada(nome, vitorias, derrotas, saldo_vitorias):
    saldo_vitorias = vitorias - derrotas
    
    if saldo_vitorias <= 10:
        nivel = "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro" 
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante" 
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"     
    else: # vitorias >100
        nivel = "imortal"     
    
    
    return f"O heroi {nome} tem saldo de vitorias {saldo_vitorias} esta no nivel de {nivel} "

nome_heroi = input (" Digite o nome do jogador ")
vitorias_heroi = int(input(" Digite numero de vitorias do jogador "))
derrotas_heroi = int(input(" Digite numero de derrotas do jogador "))
saldo_vitorias = vitorias_heroi - derrotas_heroi
    
resultado = calculadora_partidas_rankeada(nome_heroi,vitorias_heroi,derrotas_heroi,saldo_vitorias)
print(resultado)