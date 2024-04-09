from main.subscribers.subscriber import Subscriber
from main.publishers.publisher import Publisher

def textEditor():
    name = input("Digite seu nome: ")
    Publisher.sendToTextEditorTopic(name)

def fileEditor():
    text = input("Digite o texto à ser adicionado no arquivo: ")
    Publisher.sendToFileEditorTopic(text)

opcao = None
while(opcao != 0):
    print("0 - Finalizar\n1 - Editar texto\n2 - Editar arquivo\n3 - Realizar calculo\n")
    opcao = int(input('Digite a opção: '))
    if(opcao == 1):
        textEditor()
    if (opcao == 2):
        fileEditor()
    if (opcao == 3):
        calculate()
print('Até mais camarada!')
