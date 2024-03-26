import json
from .publishers import publisher

# Create your views here.

def enviaMensagem(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    nome = body_data.get('nome', None)
    publisher.sendToTextEditorResponseTopic(nome)
