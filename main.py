import os
import matplotlib.pyplot as plt
import numpy as np


def menu_principal():
    print("\nBem-vindo(a) a Biblioteca de Raciocínio Matemático!\n")
    print("--> Selecione uma das opções abaixo:\n")
    print("Função do segundo grau  [1]")
    print("Funções exponenciais    [2]")
    print("Matrizes                [3]")
    print("Encerrar o programa     [0]")

    opcao_escolhida = validar_escolha()

    if opcao_escolhida == 1:
        os.system('cls')
        funcao_segundo_grau()
    elif opcao_escolhida == 2:
        os.system('cls')
        funcao_exponencial()
    elif opcao_escolhida == 3:
        os.system('cls')
        matrizes()
    else:
        os.system('cls')
        print("O programa foi encerrado.")


def funcao_segundo_grau():
    print("\nFunção do segundo grau")
    a, b, c = obter_funcao_segundo_grau()
    delta = calcular_delta(a, b, c)

    print("--> Selecione uma das opções abaixo:\n")
    print("Calcular raízes           [1]")
    print("Calcular função           [2]")
    print("Calcular vértice          [3]")
    print("Gerar gráfico             [4]")
    print("Voltar ao menu principal  [0]")

    opcao_escolhida = int(input("\nOpção escolhida: "))

    while opcao_escolhida < 0 or opcao_escolhida > 4:
        print("Opção inválida, tente novamente.")
        opcao_escolhida = int(input("\nOpção escolhida: "))

    if opcao_escolhida == 1:
        os.system('cls')
        calcular_raizes(a, b, c)
    elif opcao_escolhida == 2:
        os.system('cls')
        calcular_funcao_segundo_grau(a, b, c)
    elif opcao_escolhida == 3:
        os.system('cls')
        calcular_vertice(delta, a, b, c)
    elif opcao_escolhida == 4:
        os.system('cls')
        imprimir_grafico_funcao_segundo_grau(a, b, c)
    else:
        os.system('cls')
        menu_principal()


def funcao_exponencial():
    print("\nFunções exponenciais\n")

    base, expoente = obter_funcao_exponencial()

    print("--> Selecione uma das opções abaixo:\n")
    print("Crescente ou decrescente  [1]")
    print("Calcular função           [2]")
    print("Gerar gráfico             [3]")
    print("Voltar ao menu principal  [0]")

    opcao_escolhida = validar_escolha()

    if opcao_escolhida == 1:
        os.system('cls')
        obter_ordem_funcao_exponencial(base)
    elif opcao_escolhida == 2:
        os.system('cls')
        calcular_funcao_exponencial(base, expoente)
    elif opcao_escolhida == 3:
        os.system('cls')
        imprimir_grafico_funcao_exponencial(base, expoente)
    else:
        os.system('cls')
        menu_principal()


def matrizes():
    print("\nMatrizes\n")

    matriz, linha, coluna = obter_matriz()

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Determinante              [1]")
    print("Multiplicação             [2]")
    print("Matriz transposta         [3]")
    print("Voltar ao menu principal  [0]")

    opcao_escolhida = validar_escolha()

    if opcao_escolhida == 1:
        os.system('cls')
        calcular_determinante(matriz, linha, coluna)
    elif opcao_escolhida == 2:
        os.system('cls')
        multiplicar_matrizes(matriz, linha, coluna)
    elif opcao_escolhida == 3:
        os.system('cls')
        obter_matriz_transposta(matriz, linha, coluna)
    else:
        os.system('cls')
        menu_principal()


def validar_escolha():
    escolha = int(input("\nOpção escolhida: "))

    while escolha < 0 or escolha > 3:
        print("Opção inválida, tente novamente.")
        escolha = int(input("\nOpção escolhida: "))

    return escolha


def validar_escolha_menu_secundario():
    escolha_secundaria = int(input("\nOpção escolhida: "))

    while escolha_secundaria < 1 or escolha_secundaria > 2:
        print("Opção inválida, tente novamente.")
        escolha_secundaria = int(input("\nOpção escolhida: "))

    return escolha_secundaria


# --------------------------------------    Função de Segundo Grau  ----------------------------------------

def obter_funcao_segundo_grau():
    print("\nEm uma função f(x) = a(x^2) + b(x) + c, informe os seguintes valores: \n")
    valor_a = float(input("a = "))
    valor_b = float(input("b = "))
    valor_c = float(input("c = "))
    print(f"\nSua função é f(x) = {valor_a}(x^2) + {valor_b}(x) + {valor_c}\n")

    return valor_a, valor_b, valor_c


def calcular_raizes(a, b, c):
    print(f"\nRaízes da função f(x) = {a}(x^2) + {b}(x) + {c}")

    delta = calcular_delta(a, b, c)

    primeira_raiz = (-b + (delta ** (1 / 2))) / (2 * a)
    segunda_raiz = (-b - (delta ** (1 / 2))) / (2 * a)

    print("x' =", primeira_raiz)
    print("x'' =", segunda_raiz)

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função de segundo grau  [1]")
    print("Voltar ao menu principal                  [2]")
    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_segundo_grau()
    else:
        os.system('cls')
        menu_principal()


def calcular_funcao_segundo_grau(a, b, c):
    print(f"\nCálculo da função f(x) = {a}(x^2) + {b}(x) + {c}")
    valor_x = float(input("\nInforme o valor de x: "))

    resultado = (a * (valor_x ** 2)) + (b * valor_x) + c
    print(f"\nf({valor_x}) =", resultado)

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função de segundo grau  [1]")
    print("Voltar ao menu principal                  [2]")

    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_segundo_grau()
    else:
        os.system('cls')
        menu_principal()


def calcular_delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return delta


def calcular_vertice(delta, a, b, c):
    print(f"\nOs vértices da função f(x) = {a}(x^2) + {b}(x) + {c}:")
    x_vertice = -(b / (2 * a))
    y_vertice = -(delta / (4 * a))

    print(f"Xv = {x_vertice}")
    print(f"Yv = {y_vertice}")

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função de segundo grau  [1]")
    print("Voltar ao menu principal                  [2]")
    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_segundo_grau()
    else:
        os.system('cls')
        menu_principal()


def imprimir_grafico_funcao_segundo_grau(a, b, c):
    x = np.arange(-7, 7, 0.1)
    y = (a * (x ** 2)) + (b * x) + c

    fig = plt.figure(figsize=(5, 5))

    plt.plot(x, y, label="Função do Segundo Grau", color='g')
    plt.title(f"f(x) = {a}(x^2) + {b}(x) + {c}")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    fig.savefig('FSG.png')

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função de segundo grau  [1]")
    print("Voltar ao menu principal                  [2]")
    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_segundo_grau()
    else:
        os.system('cls')
        menu_principal()


# --------------------------------------     Função Exponencial    ----------------------------------------

def obter_funcao_exponencial():
    print("Dado a função exponencial f(x) = a^x, insira os seguintes valores: ")
    base = float(input("a = "))
    expoente = float(input("x = "))

    return base, expoente


def obter_ordem_funcao_exponencial(a):
    if a > 1:
        print("A função exponencial é crescente")
    elif a > 0 and a < 1:
        print("A função exponencial é decrescente")
    else:
        print("A função não existe")

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função exponencial  [1]")
    print("Voltar ao menu principal              [2]")
    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_exponencial()
    else:
        os.system('cls')
        menu_principal()


def calcular_funcao_exponencial(base, expoente):
    print(f"Calcular a função exponencial f(x) = {base}^{expoente}\n")

    resultado = base ** expoente
    print(f"f({expoente}) =", resultado)

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função exponencial  [1]")
    print("Voltar ao menu principal              [2]")
    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_exponencial()
    else:
        os.system('cls')
        menu_principal()


def imprimir_grafico_funcao_exponencial(base, expoente):
    vetor_x = np.arange(-7, 7, 0.1)
    vetor_y = []

    for expo in vetor_x:
        vetor_y.append(base ** expo)

    fig = plt.figure(figsize=(5, 5))

    plt.plot(vetor_x, vetor_y, label="Função Exponencial", color='g')
    plt.title("f(x) = " + str(base) + " ^ " + str(expoente))
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    fig.savefig('FExp.png')

    print("\n--> Selecione uma das opções abaixo:\n")
    print("Voltar ao menu da função exponencial  [1]")
    print("Voltar ao menu principal              [2]")
    escolha = validar_escolha_menu_secundario()

    if escolha == 1:
        os.system('cls')
        funcao_exponencial()
    else:
        os.system('cls')
        menu_principal()


# --------------------------------------            Matrizes        ----------------------------------------
def obter_matriz():
    quantidade_linha = int(input("Informe o número de linhas da matriz: "))
    quantidade_coluna = int(input("Informe o número de colunas da matriz: "))
    print(" ")

    matriz_vazia = criar_matriz(quantidade_linha, quantidade_coluna)
    matriz_completa = preencher_matriz(matriz_vazia, quantidade_linha, quantidade_coluna)

    print(f"\nMatriz {quantidade_linha}x{quantidade_coluna} criada:\n")
    imprimir_matriz(matriz_completa, quantidade_linha)

    return matriz_completa, quantidade_linha, quantidade_coluna


def criar_matriz(numero_linhas, numero_colunas):
    matriz = [0] * numero_linhas

    for linha in range(numero_linhas):
        matriz[linha] = [0] * numero_colunas

    return matriz


def preencher_matriz(matriz_vazia, numero_linhas, numero_colunas):
    for linha in range(numero_linhas):
        for coluna in range(numero_colunas):
            valor = int(input(f"Informe o valor da posição [{linha}][{coluna}]: "))
            matriz_vazia[linha][coluna] += valor

    return matriz_vazia


def imprimir_matriz(matriz_completa, numero_linhas):
    for linha in range(numero_linhas):
        print(matriz_completa[linha])


def calcular_determinante(matriz_completa, numero_linhas, numero_colunas):
    if numero_linhas == numero_colunas:
        print("\nValidação: a matriz abaixo é quadrada!\n")

        imprimir_matriz(matriz_completa, numero_linhas)

        if numero_linhas == 2:
            diagonal_principal = 1
            diagonal_secundaria = 1

            for linha in range(numero_linhas):
                for coluna in range(1):
                    diagonal_principal *= matriz_completa[linha][linha + coluna]
                    diagonal_secundaria *= matriz_completa[linha][numero_linhas - linha - 1]

            determinante = diagonal_principal - diagonal_secundaria
            print(f"\nDeterminante da matriz = {determinante}")

            print("\n--> Selecione uma das opções abaixo:\n")
            print("Voltar ao menu das matrizes  [1]")
            print("Voltar ao menu principal     [2]")
            escolha = validar_escolha_menu_secundario()

            if escolha == 1:
                os.system('cls')
                matrizes()
            else:
                os.system('cls')
                menu_principal()

        elif numero_linhas == 3:
            nova_matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            # Preenche a matriz
            for a in range(numero_linhas):
                for b in range(numero_colunas):
                    nova_matriz[a][b] += matriz_completa[a][b]
                if a == 2:
                    for i in range(3):
                        for j in range(3, 5):
                            nova_matriz[i][j] += matriz_completa[i][j - 3]

            # Diagonais principais
            dp_1, dp_2, dp_3 = 1, 1, 1

            # Diagonais secundárias
            ds_1, ds_2, ds_3 = 1, 1, 1

            for linha in range(3):
                for coluna in range(1):
                    dp_1 *= nova_matriz[linha][linha + coluna]
                    dp_2 *= nova_matriz[linha][linha + coluna + 1]
                    dp_3 *= nova_matriz[linha][linha + coluna + 2]
                    ds_1 *= nova_matriz[linha][numero_linhas - linha - 1]
                    ds_2 *= nova_matriz[linha - 1][numero_linhas - linha - 1]
                    ds_3 *= nova_matriz[linha - 2][numero_linhas - linha - 1]

            diagonal_principal = dp_1 + dp_2 + dp_3
            diagonal_secundaria = ds_1 + ds_2 + ds_3

            determinante = diagonal_principal - diagonal_secundaria
            print(f"\nDeterminante da matriz = {determinante}")

            print("\n--> Selecione uma das opções abaixo:\n")
            print("Voltar ao menu das matrizes  [1]")
            print("Voltar ao menu principal     [2]")
            escolha = validar_escolha_menu_secundario()

            if escolha == 1:
                os.system('cls')
                matrizes()
            else:
                os.system('cls')
                menu_principal()

        else:
            print("Não está disponível o calculo da determinante para uma matriz maior do que 3x3")

            print("\n--> Selecione uma das opções abaixo:\n")
            print("Voltar ao menu das matrizes  [1]")
            print("Voltar ao menu principal     [2]")
            escolha = validar_escolha_menu_secundario()

            if escolha == 1:
                os.system('cls')
                matrizes()
            else:
                os.system('cls')
                menu_principal()

    else:
        print("\nValidação: a matriz não é quadrada")

        print("\n--> Selecione uma das opções abaixo:\n")
        print("Voltar ao menu das matrizes  [1]")
        print("Voltar ao menu principal     [2]")
        escolha = validar_escolha_menu_secundario()

        if escolha == 1:
            os.system('cls')
            matrizes()
        else:
            os.system('cls')
            menu_principal()


def multiplicar_matrizes(primeira_matriz, primeira_matriz_linha, primeira_matriz_coluna):
    segunda_matriz_linha = int(input("Informe o número de linhas da segunda matriz: "))
    segunda_matriz_coluna = int(input("Informe o número de colunas da segunda matriz: "))
    print("")
    segunda_matriz_vazia = criar_matriz(segunda_matriz_linha, segunda_matriz_coluna)
    segunda_matriz = preencher_matriz(segunda_matriz_vazia, segunda_matriz_linha, segunda_matriz_coluna)

    print(f"\nMatriz {primeira_matriz_linha}x{primeira_matriz_coluna} criada:\n")
    imprimir_matriz(primeira_matriz, primeira_matriz_linha)
    print("")

    print(f"\nMatriz {segunda_matriz_linha}x{segunda_matriz_coluna} criada:\n")
    imprimir_matriz(segunda_matriz, segunda_matriz_linha)

    if primeira_matriz_coluna == segunda_matriz_linha:
        print("\nA multiplicação é possível, resultado:")

        resultado = []

        for i in range(primeira_matriz_linha):
            colunas = []
            for j in range(segunda_matriz_coluna):
                colunas.append(0)
            resultado.append(colunas)

        for a in range(primeira_matriz_linha):
            for b in range(segunda_matriz_coluna):
                for c in range(primeira_matriz_coluna):
                    resultado[a][b] += (primeira_matriz[a][c] * segunda_matriz[c][b])

        print("\nAxB = ")
        for coluna in resultado:
            print(coluna)

        print("\n--> Selecione uma das opções abaixo:\n")
        print("Voltar ao menu das matrizes  [1]")
        print("Voltar ao menu principal     [2]")
        escolha = validar_escolha_menu_secundario()

        if escolha == 1:
            os.system('cls')
            matrizes()
        else:
            os.system('cls')
            menu_principal()

    else:
        print("\nA multiplicação não é possível")

        print("\n--> Selecione uma das opções abaixo:\n")
        print("Voltar ao menu das matrizes  [1]")
        print("Voltar ao menu principal     [2]")
        escolha = validar_escolha_menu_secundario()

        if escolha == 1:
            os.system('cls')
            matrizes()
        else:
            os.system('cls')
            menu_principal()


def obter_matriz_transposta(matriz_completa, numero_linhas, numero_colunas):
    transposta = criar_matriz(numero_linhas, numero_colunas)

    for linha in range(numero_linhas):
        for coluna in range(numero_colunas):
            transposta[coluna][linha] = matriz_completa[linha][coluna]

    print(f"\nMatriz {numero_linhas}x{numero_colunas} criada:\n")
    imprimir_matriz(matriz_completa, numero_linhas)

    print("\nMatriz transposta:\n")
    for linha in range(numero_linhas):
        print(transposta[linha])


menu_principal()
