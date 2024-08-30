import numpy as np

phrases = [
    "El servicio fue excelente y la comida deliciosa.",
    "La pelicula fue una perdida total de tiempo.",
    "Estoy feliz de haber aprobado el examen.",
    "La situacion en la ciudad es alarmante.",
    "El equipo gano el campeonato, que alegria!",
    "La musica era demasiado ruidosa y molesta.",
    "Es un gran logro para todos nosotros.",
    "El proyecto fue un fracaso absoluto.",
    "Este libro es una obra maestra.",
    "Las instalaciones del hotel estaban deterioradas.",
    "La atencion al cliente fue muy buena.",
    "La perdida del empleo fue devastadora.",
    "El evento fue un exito rotundo.",
    "La relacion entre los companeros es excelente.",
    "La politica del gobierno esta siendo criticada por todos."
]

positive_words = ["excelente", "deliciosa", "feliz",
                  "alegria", "logro", "exito", "buena", "obra maestra"]
neutral_words = ["servicio", "situacion",
                 "proyecto", "pelicula", "evento", "relacion"]
negative_words = ["perdida", "alarmante", "ruidosa",
                  "molesta", "fracaso", "devastadora", "deterioradas", "criticada"]
key_words = positive_words + neutral_words + negative_words


def calculate_vectors(phrase, positive_words, neutral_words, negative_words, key_words):
    w = []  # palabras claves que hay en la frase
    s = [0, 0, 0]  # cantidad de palabras positivas, neutrales y negativas por frase
    words_in_phrase = [word.strip('.,!?').lower() for word in phrase.split()]
    
    # Calcular w
    for word in key_words:
        if word in words_in_phrase:
            w.append(1)
        else:
            w.append(0)

    # Calcular s
    for word in words_in_phrase:
        if word in positive_words:
            s[0] += 1
        elif word in neutral_words:
            s[1] += 1
        elif word in negative_words:
            s[2] += 1

    return w, s


def avg_w(w):
    return sum(w) / len(w)

def avg_s(s):
    return np.dot((1, 0, -1), s)


print("Phrase        Average w    Average s\n--------------------------------------------------------------------------------------------")
for phrase in phrases:
    w, s = calculate_vectors(
        phrase, positive_words, neutral_words, negative_words, key_words)
    print(phrase, "|", str(avg_w(w)), "|", str(avg_s(s)), "|")
    print("--------------------------------------------------------------------------------------------")

def mostPositivePhrase():
    max_value = 0
    phrase = ""
    for p in phrases:
        w, s = calculate_vectors(
            p, positive_words, neutral_words, negative_words, key_words)
        if avg_s(s) > max_value:
            max_value = avg_s(s)
            phrase = p
    print("Most positive phrase: ", phrase)

def mostNegativePhrase():
    min_value = 0
    phrase = ""
    for p in phrases:
        w, s = calculate_vectors(
            p, positive_words, neutral_words, negative_words, key_words)
        if avg_s(s) < min_value:
            min_value = avg_s(s)
            phrase = p
    print("Most negative phrase: ", phrase)

mostPositivePhrase()
mostNegativePhrase()
