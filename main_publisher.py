from main.publishers.publisher import Publisher
import time

def textEditor():
    name = input("Digite seu nome: ")
    Publisher.sendToTextEditorTopic(name)

def fileEditor():
    text = input("Digite o texto à ser adicionado no arquivo: ")
    Publisher.sendToFileEditorTopic(text)

def calculate():
    firstValue = input("Digite o primeiro valor a ser calculado: ")
    secondValue = input("Digite o segundo valor a ser calculado: ")
    payload = {
        "first_value": firstValue,
        "second_value": secondValue,
    }
    Publisher.sendToCalculateTopic(payload)

opcao = None
while(opcao != 0):
    time.sleep(0.001)
    print("0 - Finalizar\n1 - Editar texto\n2 - Editar arquivo\n3 - Realizar calculo\n")
    opcao = int(input('Digite a opção: '))
    if(opcao == 1):
        textEditor()
    if (opcao == 2):
        fileEditor()
    if (opcao == 3):
        calculate()
print('Até mais camarada!')
