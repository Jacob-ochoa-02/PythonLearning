def reverse(texto):
    turned_text = ""
    for char in texto:
        turned_text = char + turned_text
    return turned_text


def no_spaces(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def es_palindromo(texto):
    texto = no_spaces(texto)
    turned_text = reverse(texto)
    return texto.lower() == turned_text.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola"))
