def cifra_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isupper():
            resultado += chr((ord(char) - 65 + chave) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) - 97 + chave) % 26 + 97)
        else:
            resultado += char
    return resultado


def decifra_cesar(texto, chave):
    return cifra_cesar(texto, -chave)


mensagem = "Cifra de Cesar em Python!"
chave = 3

criptografada = cifra_cesar(mensagem, chave)
print("Texto criptografado:", criptografada)

descriptografada = decifra_cesar(criptografada, chave)
print("Texto descriptografado:", descriptografada)
