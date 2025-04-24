from stats import imprimir
import sys

def main():
    imprimir()

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
