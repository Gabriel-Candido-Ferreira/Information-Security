# 🔐 Criptografia RSA aplicada em sistemas bancários

Este projeto demonstra **como a criptografia RSA funciona na prática**, mostrando de forma didática como **mensagens podem ser criptografadas e descriptografadas com segurança**, simulando o que ocorre em **transações bancárias seguras**.

O código foi estruturado em funções e mostra as principais etapas:

1. Geração de chaves RSA (pública e privada);
2. Criptografia de uma mensagem;
3. Salvamento da mensagem criptografada em um arquivo `.txt`;
4. Leitura do conteúdo criptografado e descriptografia;
5. Exibição da mensagem original recuperada.

---

## 📚 Conceito

A **criptografia RSA (Rivest–Shamir–Adleman)** é um dos algoritmos assimétricos mais usados em bancos e sistemas digitais.  
Ela utiliza **duas chaves diferentes**:

- 🔑 **Chave pública**: usada para **criptografar** os dados (pode ser compartilhada).
- 🗝️ **Chave privada**: usada para **descriptografar** (mantida em segredo).

Nos **bancos tradicionais e digitais**, o RSA é aplicado em:

- Autenticação de clientes;
- Transmissão segura de dados entre apps e servidores;
- Tokens e certificados digitais;
- Assinaturas eletrônicas e APIs seguras (como no Open Finance).

---

## ⚙️ Estrutura do projeto

```

📂 RSA/
├── main.py                 # Código principal com funções organizadas
├── mensagem_cripto.txt     # Arquivo gerado contendo a mensagem criptografada (em base64)
└── README.md               # Documentação do projeto

```

---

## 🚀 Como executar o projeto

### 1️⃣ Pré-requisitos

- Python 3.8+
- Biblioteca `cryptography`

Instale com:

```bash
pip install cryptography
```

---

### 2️⃣ Executar o código

Clone o repositório (ou copie o arquivo `.py`) e execute:

```bash
python3 RSA/main.py
```

---

### 3️⃣ Resultado esperado

O terminal exibirá as etapas:

```
🔐 Gerando chaves RSA (pública e privada)...

✅ Chaves geradas com sucesso! (2048 bits)

📩 Mensagem original: Transferencia de R$1000 aprovada

🔒 Criptografando a mensagem...

✅ Mensagem criptografada com sucesso!
📦 Conteúdo criptografado (parcial): b'\x9f\xac\xf3...' ...

💾 Conteúdo criptografado salvo em (base64): mensagem_cripto.txt


🔓 Descriptografando a mensagem...

✅ Mensagem descriptografada com sucesso!

📨 Mensagem final recuperada:
Transferencia de R$1000 aprovada
```

---

## 💾 Sobre o arquivo `mensagem_cripto.txt`

O conteúdo é salvo em **Base64**, para que possa ser lido como texto simples.
Exemplo do arquivo gerado:

```
q9Bv+V2zYaf3Aq7O5s+ip0C7qKcKLBxkDGYcVtK2WwW3m7z1c...
```

Esse texto representa os **bytes criptografados da mensagem original**.

---

## 🧠 Estrutura do código

O script é dividido em funções:

| Função                                                   | Descrição                                                            |
| -------------------------------------------------------- | -------------------------------------------------------------------- |
| `gerar_chaves()`                                         | Gera as chaves RSA (pública e privada).                              |
| `criptografar_mensagem(mensagem, public_key)`            | Criptografa a mensagem original.                                     |
| `descriptografar_mensagem(mensagem_cripto, private_key)` | Descriptografa o conteúdo.                                           |
| `salvar_em_txt(mensagem_cripto, caminho)`                | Salva o conteúdo criptografado em formato base64 num arquivo `.txt`. |
| `main()`                                                 | Executa o fluxo completo de criptografia e descriptografia.          |

---

## 🔒 Explicação teórica (resumo para seminário)

| Etapa                    | Descrição                                                  | Aplicação nos bancos                         |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------- |
| **Geração de chaves**    | Cada cliente/sistema tem um par de chaves RSA              | Servidores e apps usam certificados SSL/TLS  |
| **Criptografia**         | Os dados são codificados com a chave pública               | Protege senhas, transações, tokens           |
| **Armazenamento seguro** | Dados criptografados são salvos/transferidos com segurança | Proteção contra interceptação e vazamento    |
| **Descriptografia**      | Apenas o detentor da chave privada pode ler                | Servidor ou banco decifra os dados recebidos |

---
