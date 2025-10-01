scrabble_es = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'L': 1,
    'M': 3,
    'N': 1,
    'Ñ': 8,
    'O': 1,
    'P': 3,
    'Q': 5,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

def puntuarPalabra():
    palabra = input("Introduzca la palabra a puntuar ").upper()
    puntuacion = 0
    for i in palabra:
        puntuacion += scrabble_es[i]
    print(puntuacion)
    return puntuacion

puntuarPalabra()
