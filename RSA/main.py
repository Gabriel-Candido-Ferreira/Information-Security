import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def gerar_chaves():
    print("🔐 Gerando chaves RSA (pública e privada)...\n")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    print("✅ Chaves geradas com sucesso! (2048 bits)\n")
    return private_key, public_key

def criptografar_mensagem(mensagem: bytes, public_key):
    print("🔒 Criptografando a mensagem...\n")
    mensagem_cripto = public_key.encrypt(
        mensagem,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("✅ Mensagem criptografada com sucesso!")
    print("📦 Conteúdo criptografado (parcial):", mensagem_cripto[:60], "...\n")
    return mensagem_cripto

def descriptografar_mensagem(mensagem_cripto: bytes, private_key):
    print("🔓 Descriptografando a mensagem...\n")
    mensagem_original = private_key.decrypt(
        mensagem_cripto,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("✅ Mensagem descriptografada com sucesso!\n")
    return mensagem_original

def salvar_em_txt(mensagem_cripto: bytes, caminho_arquivo: str):
    b64 = base64.b64encode(mensagem_cripto).decode("ascii")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(b64)
    print(f"💾 Conteúdo criptografado salvo em (base64): {caminho_arquivo}\n")

def main():
    private_key, public_key = gerar_chaves()

    mensagem = b"Transferencia de R$1000 aprovada"
    print("📩 Mensagem original:", mensagem.decode(), "\n")

    mensagem_cripto = criptografar_mensagem(mensagem, public_key)

    caminho = "mensagem_cripto.txt"
    salvar_em_txt(mensagem_cripto, caminho)

    mensagem_recuperada = descriptografar_mensagem(mensagem_cripto, private_key)
    print("📨 Mensagem final recuperada:")
    print(mensagem_recuperada.decode())


if __name__ == "__main__":
    main()
