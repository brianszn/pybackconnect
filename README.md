# 🐍 Reverse Shell com Python (Conexão Invertida)

Este projeto demonstra como criar uma **reverse shell simples em Python**, utilizando sockets. Ele permite que uma máquina atacante (handler) controle remotamente outra máquina que executa o `server.py`, é um projeto simples com o intuito de estudar sobre a biblioteca Sockets.

> ⚠️ **Aviso:** Este código é apenas para fins educacionais e deve ser utilizado **somente em ambientes controlados**, com total consentimento. O uso indevido pode ser ilegal.

---

## 🧠 Como funciona

- O **`client.py`** funciona como o **handler** (máquina de controle).
- O **`server.py`** deve ser executado na máquina da vítima.
- Assim que o `server.py` é iniciado, ele cria uma **conexão reversa** com o IP/porta definido no `client.py`.
- O `client.py` então permite **enviar comandos remotos**, receber a resposta e navegar no sistema da vítima.

---

## ⚙️ Passo a passo para executar

### 1. Inicie o `client.py` (handler)

```bash
python3 client.py
```

> Este script ficará escutando e aguardando conexões de entrada.

### 2. Execute o `server.py` na máquina alvo

```bash
python3 server.py
```

> Assim que executado, ele tentará se conectar ao handler (`client.py`).

---

## 🖥️ Exemplo de uso

```bash
cmd> whoami
vítima-pc

cmd> dir
Desktop/
Documents/
Downloads/

cmd> cd Desktop
cmd> type senha.txt
```

---

## 📁 Estrutura do Projeto

```
pybackconnect/
├── client.py    # Handler (escuta e envia comandos)
├── server.py    # Cliente reverso (executa os comandos recebidos)
└── README.md
```

---

## ✅ Requisitos

- Python 3.x instalado na máquina do atacante (na máquina alvo, você pode fazer um executável com o pyinstaller ou então instalar o python)
- Rede com acesso entre cliente e servidor (pode usar tunelamento ou NAT se necessário)

---

## 🛑 Importante

Esse projeto **não possui autenticação, criptografia ou segurança**. É uma prova de conceito simples e deve ser usada com responsabilidade.

---

Feito com fins didáticos e para o estudo da biblioteca Socket. 🧠
