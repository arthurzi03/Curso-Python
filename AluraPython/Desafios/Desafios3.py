


vogal = ('a', 'e', 'i', 'o', 'u')
consoante = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
letra = input("Digite uma letra: ")
if letra in vogal:
    print("A letra é uma vogal")
elif letra in consoante:
    print("A letra é uma consoante")
else:
    print("Caractere inválido")