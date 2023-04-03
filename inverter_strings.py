# String a ser invertida
string = "Have a nice day"

# Convertendo a string para uma lista de caracteres
chars = list(string)

# Índices para iterar pela lista
i = 0
j = len(chars) - 1

# Invertendo os caracteres da lista
while i < j:
    chars[i], chars[j] = chars[j], chars[i]
    i += 1
    j -= 1

# Convertendo a lista de volta para uma string
inverted_string = ''.join(chars)

# Imprimindo a string invertida
print(inverted_string)
