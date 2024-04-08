from main.subscribers.subscriber import Subscriber
from main.publishers.publisher import Publisher

def textEditor():
    name = input("Digite seu nome: ")
    Publisher.sendToTextEditorTopic(name)

opcao = None
while(opcao != 0):
    print("0 - Finalizar\n1 - Editar texto\n2 - Editar arquivo\n3- Realizar calculo\n")
    opcao = int(input('Digite a opção: '))
    if(opcao == 1):
        textEditor()
print('Até mais camarada!')
