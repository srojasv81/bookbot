import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        cuenta = file_contents.split()
    return cuenta

def contar_letras(path):
    with open(path) as f:
        file_contents = f.read()
        letras = list(file_contents.lower())
        dicc = {x:letras.count(x) for x in set(letras)}
    return dicc

def imprimir():
    args = sys.argv

    dicc = contar_letras(args[1])
    cuenta = get_book_text(args[1])
    ordenado = {k: v for k, v in sorted(dicc.items(), key=lambda item: item[1], reverse=True)}
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}")
    print("----------- Word Count ----------")
    print(f"Found {len(cuenta)} total words")
    print("--------- Character Count -------")
    
    for item in ordenado:
        if item.isalpha():
            print(f"{item}: {ordenado[item]}")

    print("============= END ===============")
