def calcularTamanhoVetor():
    print("Calculando valor de vetor")

def normalizarVetor():
    print("Calculando valor de vetor")

def somarDoisVetores():
    print("Calculando valor de vetor")

def subtrairDoisVetores():
    print("Calculando valor de vetor")

def multiplicarDoisVetores():
    print("Calculando valor de vetor")

def dividirDoisVetores():
    print("Calculando valor de vetor")

def prodEscalarVetor():
    print("Calculando valor de vetor")

def lerNovoVetor():
    print("Digite abaixo os valores (x,y,z) para um vetor de 3 dimensões:");
    vetorOrigem = [
        float(input("Digite o valor de X: ")),
        float(input("Digite o valor de Y: ")),
        float(input("Digite o valor de Z: "))
    ]

lerNovoVetor()
print("Vetor registrado com sucesso, selecione uma das opções abaixo");

selecaoMenu = 0;

while (True):

    print("1. Calcular o tamanho do vetor;");
    print("2. Normalizar o vetor;");
    print("3. Somar o vetor, lendo os valores x, y e z de um novo vetor;");
    print("4. Subtrair o vetor, lendo os valores x, y e z de um novo vetor;");
    print("5. Multiplicar o vetor, lendo os valores de um vetor esclar;");
    print("6. Dividir o vetor, lendo os valores de um vetor esclar;");
    print("7. Calcular o produto escalar do vetor lido anteriormente por outro vetor;");
    print("8. Sair do algoritimo.");

    selecaoMenu = int(input("Selecione um item do menu: "))

    if selecaoMenu == 1:
        print('Handle option \'Option 1\'')
        calcularTamanhoVetor()

    elif selecaoMenu == 2:
        print('Handle option \'Option 2\'')
        normalizarVetor()

    elif selecaoMenu == 3:
        print('Handle option \'Option 3\'')
        somarDoisVetores()

    elif selecaoMenu == 4:
        print('Handle option \'Option 4\'')
        subtrairDoisVetores()

    elif selecaoMenu == 5:
        print('Handle option \'Option 5\'')
        dividirDoisVetores()

    elif selecaoMenu == 6:
        print('Handle option \'Option 6\'')
        multiplicarDoisVetores()

    elif selecaoMenu == 7:
        print('Handle option \'Option 7\'')
        dividirDoisVetores()

    elif selecaoMenu == 8:
        print('Obrigado por utilizar, tenha um ótimo dia!')
        exit()
    else:
        print('Opção inválida, favor selecionar uma presente no menu.')