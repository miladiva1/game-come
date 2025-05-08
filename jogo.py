import random

print("Bem-vindo ao Jogo da Adivinhação!")
print(" ")
print("Você terá 10 tentativas para acertar o numero secreto!")
print("A partir da quinta tentativa o jogo irá de ajudar com dicas")
print(" ")
jogar_novamente = 1

while jogar_novamente == 1:
    codigo_secreto = random.randint(1000, 9999)
    tentativas = 0
    acertou = 0

    c1 = codigo_secreto // 1000
    c2 = (codigo_secreto % 1000) // 100
    c3 = (codigo_secreto % 100) // 10
    c4 = codigo_secreto % 10

    fixo1 = -1
    fixo2 = -1
    fixo3 = -1
    fixo4 = -1

    while tentativas < 10 and acertou == 0:
        print(f"Tentativa {tentativas + 1} de 10")

        
        if fixo1 == -1:
            print("_", end=" ")
        else:
            print(fixo1, end=" ")
        if fixo2 == -1:
            print("_", end=" ")
        else:
            print(fixo2, end=" ")
        if fixo3 == -1:
            print("_", end=" ")
        else:
            print(fixo3, end=" ")
        if fixo4 == -1:
            print("_")
        else:
            print(fixo4)

        palpite = int(input("Digite um número de 4 dígitos: "))

        if palpite < 1000 or palpite > 9999:
            print("Número inválido! Tente novamente.")
        else:
            tentativas += 1

            p1 = palpite // 1000
            p2 = (palpite % 1000) // 100
            p3 = (palpite % 100) // 10
            p4 = palpite % 10

            corretos = 0
            errados = 0

            
            if p1 == c1:
                corretos += 1
                fixo1 = c1
            else:
                if p1 == c2 or p1 == c3 or p1 == c4:
                    errados += 1
                fixo1 = -1  

            if p2 == c2:
                corretos += 1
                fixo2 = c2
            else:
                if p2 == c1 or p2 == c3 or p2 == c4:
                    errados += 1
                fixo2 = -1

            if p3 == c3:
                corretos += 1
                fixo3 = c3
            else:
                if p3 == c1 or p3 == c2 or p3 == c4:
                    errados += 1
                fixo3 = -1

            if p4 == c4:
                corretos += 1
                fixo4 = c4
            else:
                if p4 == c1 or p4 == c2 or p4 == c3:
                    errados += 1
                fixo4 = -1

            print(f"Números na posição correta: {corretos}")
            print(f"Números na posição errada: {errados}")

            if corretos == 4:
                acertou = 1
                print(f"Parabéns! Você acertou o código secreto {codigo_secreto} em {tentativas} tentativas.")
            else:
                if tentativas == 5:
                    print("As dicas começarão a partir da próxima tentativa.")
                elif tentativas == 6:
                    if c1 % 2 == 0:
                        print("Dica: O primeiro dígito é par.")
                    else:
                        print("Dica: O primeiro dígito é ímpar.")
                elif tentativas == 7:
                    if c2 >= 5:
                        print("Dica: O segundo dígito é maior ou igual a 5.")
                    else:
                        print("Dica: O segundo dígito é menor que 5.")
                elif tentativas == 8:
                    if c3 % 2 == 0:
                        print("Dica: O terceiro dígito é par.")
                    else:
                        print("Dica: O terceiro dígito é ímpar.")
                elif tentativas == 9:
                    if c4 >= 5:
                        print("Dica: O quarto dígito é maior ou igual a 5.")
                    else:
                        print("Dica: O quarto dígito é menor que 5.")

    if acertou == 0:
        print(f"Que pena! Você não acertou o código secreto {codigo_secreto} em 10 tentativas.")

    jogar_novamente = int(input("Deseja jogar novamente? (1 - Sim / 0 - Não): "))

print("Obrigado por jogar!")