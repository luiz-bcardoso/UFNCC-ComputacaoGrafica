# import the math module used for the "math.sqrt()" function
import math 

def calcularTamanhoVetor():
    print("Calculando valor de vetor")

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
    fatorMultiplicador = int(input(" > Digite um valor inteiro para ser usado como fator de multiplicação (ex: 2 para 2x o vetor): "));
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
        print("Não é possível dividir por zero ou negativo, por favor tente usar outra escalar")
        dividirVetor(vetor)
    
    vetorResultado = []
    print(" > Calculando valor de vetor original v",vetor," com divisão de ",fatorEscalar,".")
    
    ## Divide cada elemento do vetor pelo valor informado
    for i in range(len(vetor)):
        vetorResultado.append(vetor[i] / fatorEscalar)

    print(" > Vetor divido por",fatorEscalar,"x com sucesso.")
    return vetorResultado

def prodEscalarVetor():
    print("Calculando valor de vetor")


def lerNovoVetor():
    print("Digite abaixo os valores (x,y,z) para um vetor de 3 dimensões:");
    vetor = [
        float(input("Digite o valor de X: ")),
        float(input("Digite o valor de Y: ")),
        float(input("Digite o valor de Z: "))
    ]
    print("Vetor v", vetor," registrado com sucesso.")
    return vetor