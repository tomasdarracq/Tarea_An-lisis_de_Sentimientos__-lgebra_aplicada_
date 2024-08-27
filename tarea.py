import numpy as np
phrases = [
    "El servicio fue excelente y la comida deliciosa.",
    "La película fue una pérdida total de tiempo.",
    "Estoy feliz de haber aprobado el examen.",
    "La situación en la ciudad es alarmante.",
    "El equipo ganó el campeonato, ¡qué alegría!",
    "La música era demasiado ruidosa y molesta.",
    "Es un gran logro para todos nosotros.",
    "El proyecto fue un fracaso absoluto.",
    "Este libro es una obra maestra.",
    "Las instalaciones del hotel estaban deterioradas.",
    "La atención al cliente fue muy buena.",
    "La pérdida del empleo fue devastadora.",
    "El evento fue un éxito rotundo.",
    "La relación entre los compañeros es excelente.",
    "La política del gobierno está siendo criticada por todos."
]
positive_words = ["excelente", "deliciosa", "feliz",
                  "alegría", "logro", "éxito", "buena", "obra maestra"]
neutral_words = ["servicio", "situación",
                 "proyecto", "película", "evento", "relación"]
negative_words = ["pérdida", "alarmante", "ruidosa",
                  "molesta", "fracaso", "devastadora", "deterioradas", "criticada"]
key_words = positive_words + neutral_words + negative_words


def calculate_vectors(phrase, positive_words, neutral_words, negative_words, key_words):
    w = []  # palabras claves que hay en la frase
    s = [0, 0, 0]  # cantidad de palabras positivas, neutrales y negativas por frase
    words_in_phrase = phrase.lower().split(" ")

    # Calcular w
    for word in key_words:
        word = word.strip('.,!?')
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


print("Phrase        w        s        avg_w    avg_s\n----------------------------------------")
for phrase in phrases:
    w, s = calculate_vectors(
        phrase, positive_words, neutral_words, negative_words, key_words)
    print(phrase, w, s, str(avg_w(w)), str(avg_s(s)))
    print

w, s = calculate_vectors(phrases, positive_words,
                         neutral_words, negative_words,)
