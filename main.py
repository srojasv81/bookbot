def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    cuenta_palabras = contar_palabras(text)
    letras_diccionario = contar_letras(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{cuenta_palabras} words found in the document")
    resultado_ordenado(letras_diccionario)
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def contar_palabras(texto):
    cuenta = len(texto.split())
    return cuenta

def contar_letras(texto):
    resultado = {}
    for letra in texto:
        letra_minuscula = letra.lower()
        if letra_minuscula in resultado:
            resultado[letra_minuscula] += 1
        else:
            resultado[letra_minuscula] = 1
    return resultado

def resultado_ordenado(diccionario):
    ordenado = dict(sorted(diccionario.items(), key=lambda item:item[1], reverse=True))
    letras = ("abcdefghijklmnopqrstuvwxyz")
    for letra in ordenado:
        if letra in letras:
            print(f"The '{letra}' character was found {ordenado[letra]} times")
    
main()