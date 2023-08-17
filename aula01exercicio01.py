# import the math module used for the "math.sqrt()" function
import math 

def calcularTamanhoVetor(vetor):
    print(" > Determinando valor do tamanho do vetor V",vetor)
    print("\n >> Vetor possui ",vetor[0], " unidades para X")
    print("\n >> Vetor possui ",vetor[1], " unidades para Y")
    print("\n >> Vetor possui ",vetor[2], " unidades para Z")


# Função que ao informar um vetor, é normalizado e retornado como uma array.
def normalizarVetor(vetor):
    print(" > Normalizando valor do vetor V",vetor)
    # Determina o valor a ser dividido usando a formula sqrt(x², y² e z²)
    fatorDivisao = abs(math.sqrt((vetor[0]*vetor[0])+
                                 (vetor[1]*vetor[1])+
                                 (vetor[2]*vetor[2])))
    
    # Determina o valor do vetor normalizado dividindo o original com o fator.
    vetorNormalizado = [vetor[0]/fatorDivisao,
                        vetor[1]/fatorDivisao,
                        vetor[2]/fatorDivisao]
    
    print(" > Vetores de origem normalizado com sucesso.")
    return vetorNormalizado

# Função que ao informar um vetor, é somado e retornado como um novo vetor resultado.
def somarDoisVetores(vetorA):
    # Declara um vetor de soma e um novo vetor para ser somad
    vetorResultado = []
    vetorB = lerNovoVetor()

    print(" > Calculando adição do vetor original v", vetorA," com vetor lido v",vetorB,".")
    
    # Para cada elemento no vetorA (x,y e z), soma os valores em um novo vetor e retorna como um novo.
    for i in range(len(vetorA)):
        vetorResultado.append(vetorA[i] + vetorB[i])

    print(" > Vetores de origem e soma calculados com sucesso.")    
    return vetorResultado

# Função que ao informar um vetor, é normalizado e retornado como um novo vetor resultado.
def subtrairDoisVetores(vetorA):
    # Declara um vetor de soma e um novo vetor para ser somad
    vetorResultado = []
    vetorB = lerNovoVetor()

    print(" > Calculando subtração do vetor original v", vetorA," com vetor lido v",vetorB,".")
    
    # Para cada elemento no vetorA (x,y e z), subtrai os valores em um novo vetor e retorna como um novo.
    for i in range(len(vetorA)):
        vetorResultado.append(vetorA[i] - vetorB[i])

    print(" > Vetores de origem e subtração calculados com sucesso.")      
    return vetorResultado

# Função que ao informar um vetor e uma escalar, é multiplicado em x vezes como um novo vetor resultado.
def multiplicarVetor(vetor):
    fatorMultiplicador = int(input(" > Digite um valor inteiro para ser usado como fator de multiplicação (ex: 2 para 2x o vetor): "))
    
    vetorResultado = []
    print(" > Calculando valor de vetor original v",vetor," com multiplicação de ",fatorMultiplicador,".")
    
    ## Multiplica cada elemento do vetor pelo valor informado
    for i in range(len(vetor)):
        vetorResultado.append(vetor[i] * fatorMultiplicador)

    print(" > Vetor multiplicado por",fatorMultiplicador,"x com sucesso.")
    return vetorResultado

# Função que ao informar um vetor e uma escalar, é multiplicado em x vezes como um novo vetor resultado.
def dividirVetor(vetor):
    # Pergunta ao usuario qual o valor da escalar para ser dividido.
    fatorEscalar = int(input(" > Digite um valor inteiro para ser usado como escalar (ex: 2 para metade o vetor): "));
    if(fatorEscalar <= 0):
        print(" > ERRO! Não é possível dividir por zero ou negativo, por favor tente usar outra escalar")
        fatorEscalar = 1
        dividirVetor(vetor)
    
    vetorResultado = []
    print(" > Calculando valor de vetor original v",vetor," com divisão de ",fatorEscalar,".")
    
    ## Divide cada elemento do vetor pelo valor informado
    for i in range(len(vetor)):
        vetorResultado.append(vetor[i] / fatorEscalar)

    print(" > Vetor divido por",fatorEscalar,"x com sucesso.")
    return vetorResultado

def prodEscalarVetor(vetorA):
    print(" > Para calcular o produto escalar entre dois vetores, insira outro abaixo para continuar. ")
    produtoEscalar = 0
    vetorB = lerNovoVetor()
    print(" > Calculando valor de vetor original v",vetorA," com multiplicação de v",vetorB,".")
    
    for i in range(len(vetorA)):
        vetorResultado = (vetorA[i] * vetorB[i])
        produtoEscalar = produtoEscalar + vetorResultado
        
    return produtoEscalar

def lerNovoVetor():
    print("Digite abaixo os valores do PRIMEIRO PONTO (x,y,z) para um vetor de 3 dimensões:")
    pontoA = [
        float(input("Digite o valor de X: ")),
        float(input("Digite o valor de Y: ")),
        float(input("Digite o valor de Z: "))
    ]
    print("Primeiro ponto P",pontoA," cadastrado com sucesso!")

    print("Digite abaixo os valores do SEGUNDO PONTO (x,y,z) para um vetor de 3 dimensões:")
    pontoB = [
        float(input("Digite o valor de X: ")),
        float(input("Digite o valor de Y: ")),
        float(input("Digite o valor de Z: "))
    ]
    print("Segundo ponto P",pontoB," cadastrado com sucesso!")
    vetorBase = []
    for i in range(len(pontoA)):
        vetorBase.append(pontoB[i] - pontoA[i])
    print("Vetor v", vetorBase," registrado com sucesso.")
    return vetorBase

vetorInicial = lerNovoVetor()
print("\n Vetor registrado com sucesso, selecione uma das opções abaixo: ")

selecaoMenu = 0

while (True):

    print("1. CALCULAR o TAMANHO do vetor;")
    print("2. NORMALIZAR o vetor;")
    print("3. SOMAR o vetor, lendo os valores x, y e z de um novo vetor;")
    print("4. SUBRATIR o vetor, lendo os valores x, y e z de um novo vetor;")
    print("5. MULTIPLICAR o vetor, lendo os valores de um vetor esclar;")
    print("6. DIVIDIR o vetor, lendo os valores de um vetor esclar;")
    print("7. CALCULAR o PRODUTO ESCALAR do vetor lido anteriormente por outro vetor;")
    print("8. SAIR do algoritimo.")

    selecaoMenu = int(input("Selecione um item do menu: "))

    if selecaoMenu == 1:
        print('Selecionado \'Option 1\'')
        calcularTamanhoVetor(vetorInicial)
        print()

    elif selecaoMenu == 2:
        print('Selecionado \'Option 2\'')
        vetorNormal = normalizarVetor(vetorInicial)
        print("\n >> Vetor NORMALIZADO: ", vetorNormal)
        print()

    elif selecaoMenu == 3:
        print('Selecionado \'Option 3\'')
        vetorSoma = somarDoisVetores(vetorInicial)
        print("\n >> Vetor SOMA: ", vetorSoma)
        print()

    elif selecaoMenu == 4:
        print('Selecionado \'Option 4\'')
        vetorSubtracao = subtrairDoisVetores(vetorInicial)
        print("\n >> Vetor SUBTRAÇÃO: ", vetorSubtracao)
        print()

    elif selecaoMenu == 5:
        print('Selecionado \'Option 5\'')
        vetorMultiplicado = multiplicarVetor(vetorInicial)
        print("\n >> Vetor MULTIPLICACÃO: ", vetorMultiplicado)
        print()

    elif selecaoMenu == 6:
        print('Selecionado \'Option 6\'')
        vetorDivisao = dividirVetor(vetorInicial)
        print("\n >> Vetor DIVISAO: ", vetorDivisao)
        print()

    elif selecaoMenu == 7:
        print('Selecionado \'Option 7\'')
        vetorEscalado = prodEscalarVetor(vetorInicial)
        print("\n >> Velor do PRODUTO ESCALADO: ", vetorEscalado)
        print()

    elif selecaoMenu == 8:
        print('\n Obrigado por utilizar, tenha um ótimo dia! \n')
        exit()
    else:
        print('\n ERRO! Opção inválida, favor selecionar uma presente no menu. \n')