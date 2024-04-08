# Seminário MQTT - XRSC09 SISTEMAS DISTRIBÚIDOS

**Projeto para a disciplina XRSC09 - SISTEMAS DISTRIBÚIDOS ministrada pelo professor Rafael de Magalhães Dias Frinhani**

**Alunos:**

- Breno Sampaio dos Santos

## Instalando dependências

*Para permitir o funcionamento da aplicação será necessário seguir alguns passos, selecione de acordo com seu sistema operacional para conseguir executar a funcionalidade*

### Windows

#### Instalando Python

- Acessar o [Site oficial](https://www.python.org/downloads/) e fazer o download da versão mais recente

#### Instalando o pip

- Caso o pip não venha instalado com o python, deve seguir os deve se seguir os passos segundo a [Documentação do pip](https://pip.pypa.io/en/stable/installation/)

### Linux

#### Instalando Python

Executar o seguinte comando no terminal:
```sh
sudo apt update
sudo apt-get install python
```

#### Instalando o pip

Caso o pip não venha instalado com o python, deve se seguir os passos:

```sh
wget https://bootstrap.pypa.io/get-pip.py
python3 ./get-pip.py
```

Para mais informações acesse a [Documentação do pip](https://pip.pypa.io/en/stable/installation/)

### Instalando bibliotecas com o pip

Executar o seguinte comando:

```sh
python3 pip -m install paho-mqtt
```

## Broker Mosquitto

*Adicionar informações do broker*

## Execução

- Para Iniciar a aplicação basta executar o comando:

*Obs: Deve ser executado na pasta raíz*

```sh
python3 main.py
```