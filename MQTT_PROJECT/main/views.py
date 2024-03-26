import json
from .publishers.publisher import Publisher

# Create your views here.

def enviaMensagem(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    nome = body_data.get('nome', None)
    Publisher.sendToTextEditorResponseTopic(nome)
