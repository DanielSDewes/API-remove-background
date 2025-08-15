# API Remove Background

## Descrição

Este projeto fornece uma API para remoção de fundo de imagens usando FastAPI e a biblioteca `rembg`. O backend deve ser executado com **Python 3.11 ou anterior**, pois a versão 3.12 apresenta conflitos de compatibilidade.

## Requisitos

* Python 3.11 ou anterior
* Virtualenv (opcional, mas recomendado)

### Dependências

Execute o comando:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter pelo menos:

```
fastapi
uvicorn
rembg
python-multipart
```

## Configuração do Ambiente

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# No Windows PowerShell:
.\.venv\Scripts\activate.ps1
# No Windows CMD:
.\.venv\Scripts\activate.bat
# No Linux/Mac:
source .venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a API

```bash
python -m uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## Endpoints

* `POST /remove-background` - Recebe uma imagem e retorna a imagem sem fundo.

## Observações

* Certifique-se de estar usando **Python 3.11 ou anterior** para evitar erros de compatibilidade com `pymatting` e `numba`.
* O pacote `python-multipart` é necessário para o upload de arquivos via formulário.

## Estrutura do Projeto

```
api-remove-background/
│
├─ app/
│  ├─ main.py
│  ├─ utils.py
│  └─ ...
├─ requirements.txt
└─ README.md
```

## Exemplo de código consumindo a API:

```bash
import requests

# Abra a imagem que você quer enviar (pinscher.png)
# A imagem deve estar no mesmo diretório desse script que pode ser executado diretamente pelo cmd.

with open("pinscher.png", "rb") as f:
    files = {"file": f}

    # Envia para o endpoint da API
    response = requests.post(
        "http://127.0.0.1:8000/remove-background/",
        files=files
    )

# Salva a imagem com o fundo já removido
if response.status_code == 200:
    with open("pinscher_sem_fundo.png", "wb") as out:
        out.write(response.content)
    print("Imagem sem fundo salva como pinscher_sem_fundo.png")
else:
    print("Erro:", response.status_code)
```

## Licença

Este projeto é open-source, use como desejar.
