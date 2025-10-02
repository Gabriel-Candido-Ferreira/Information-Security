# Cifra de César em Python

Este projeto implementa a **Cifra de César**, um dos métodos mais antigos de criptografia, utilizando a operação de **módulo (`%`)** para realizar o deslocamento das letras no alfabeto.

## 📖 O que é a Cifra de César?

A Cifra de César é uma técnica simples de criptografia onde cada letra de um texto é substituída por outra letra que está um número fixo de posições à frente no alfabeto.
Exemplo (com chave 3):

```
Texto original:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Texto cifrado:   DEFGHIJKLMNOPQRSTUVWXYZABC
```

Se quisermos **decifrar**, basta deslocar na direção contrária.

---
### Saída esperada:

```
Texto criptografado: Fljud gh Fhvdu hp Sbwkrq!
Texto descriptografado: Cifra de Cesar em Python!
```

---

## 🔑 Como funciona o cálculo com `mod`

O truque principal é o uso do **módulo `% 26`**:

```python
(ord(char) - base + chave) % 26
```

* `ord(char)` → obtém o valor numérico da letra (ASCII).
* `base` → `65` para letras maiúsculas (`A`), `97` para minúsculas (`a`).
* `+ chave` → aplica o deslocamento.
* `% 26` → garante que, ao passar de `Z` ou `z`, o contador volte para o início do alfabeto.
* `chr(...)` → converte de volta para letra.

Exemplo prático:
Se deslocarmos `Z` (código 90) com chave `+3`:

```
(ord('Z') - 65 + 3) % 26 = (25 + 3) % 26 = 2
chr(2 + 65) = 'C'
```

Ou seja, `Z → C`.

---

## 📌 Observações

* Funciona apenas com caracteres do alfabeto latino (`A-Z`, `a-z`).
* Mantém espaços, números e símbolos inalterados.
* É apenas uma **cifra clássica** e **não deve ser usada para segurança real**, apenas para fins didáticos.
