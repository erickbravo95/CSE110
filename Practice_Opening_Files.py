with open("books.txt") as libros_de_mormon:
    for libro in libros_de_mormon:
        no_blanks = libro.strip()
        print(no_blanks)