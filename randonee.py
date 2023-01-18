from random import randint


def test_denivele(trajet):
    """
    trajet – liste d'entiers
    Sortie : booléen – True si tab contient des éléments
             successifs distincts, False sinon.
    >>> test_denivele([1, 2, 3, 1, 2, 3])
    True
    >>> test_denivele([1, 2, 3, 1, 2, 2])
    False
    """
    for i in range(len(trajet) - 1):
        if trajet[i] == trajet[i + 1]:
            return False

    return True


def denivele(nombre_etapes, hauteur_min, hauteur_max):
    """
    nombre_etapes – entier strictement positif
    hauteur_min, hauteur_max – entiers strictement positifs avec mini < maxi
    Sortie : trajet – liste de nombre_etapes entiers aléatoires compris
             entre hauteur_min (inclus) et hauteur_max (inclus). Attention,
             deux éléments successifs doivent être distincts.
    >>> test_denivele(denivele(5, 1, 4))
    True
    >>> test_denivele(denivele(20, 1, 8))
    True
    """
    while True:
        trajet = [randint(hauteur_min, hauteur_max) for _ in range(nombre_etapes)]
        if test_denivele(trajet):
            return trajet


def find_couples_max_indices(liste):
    """
    trajet - liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : liste des couples (indices, valeur) du plus grand élément
             de la liste trajet.
    >>> find_couples_max_indices([2, 3, 2, 5, 4])
    [(3, 5)]
    >>> find_couples_max_indices([2, 8, 3, 8, 4, 8, 5, 6, 8])
    [(1, 8), (3, 8), (5, 8), (8, 8)]
    """

    couples_max_indices = []
    max_value = 0
    for i in range(len(liste)):
        if liste[i] > max_value:
            max_value = liste[i]
            couples_max_indices = [(i, liste[i])]

        elif liste[i] == max_value:
            couples_max_indices.append((i, liste[i]))

    return couples_max_indices


def nb_hauts_sommets(trajet):
    """
    trajet – liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : couple d'entiers – le nombre d'occurrences du plus
             grand élément de la liste et sa valeur.
    >>> nb_hauts_sommets([2, 3, 2, 5, 4])
    (1, 5)
    >>> nb_hauts_sommets([2, 8, 3, 8, 4, 8, 5, 6, 8])
    (4, 8)
    """
    nombre_hauts_sommets = 0
    hauteur_hauts_sommets = 0
    for etape in trajet:
        if etape == hauteur_hauts_sommets:
            nombre_hauts_sommets += 1

        elif etape > hauteur_hauts_sommets:
            hauteur_hauts_sommets = etape
            nombre_hauts_sommets = 1

    return nombre_hauts_sommets, hauteur_hauts_sommets


def duree_etapes(trajet):
    """
    trajet – liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : liste – durée de chaques étapes
    >>> sum(duree_etapes([2, 3, 2, 5, 4]))
    50
    >>> sum(duree_etapes([2, 8, 3, 8, 4, 8, 5, 6, 8]))
    240
    """
    liste_durees = [0]
    for i in range(len(trajet) - 1):
        denivele_etape = trajet[i + 1] - trajet[i]
        if denivele_etape < 0:
            liste_durees.append(5 * (-denivele_etape))
        else:
            liste_durees.append(10 * denivele_etape)

    return liste_durees


def temps_etapes(trajet):
    """
    liste_duree – liste de la durée de chaques étapes
    Sortie : liste – temps à chaques étapes
    >>> temps_etapes([2, 3, 2, 5, 4])[-1]
    50
    >>> temps_etapes([2, 8, 3, 8, 4, 8, 5, 6, 8])[-1]
    240
    """
    liste_durees = duree_etapes(trajet)
    liste_temps = [0]
    for i in range(1, len(liste_durees)):
        liste_temps.append(liste_durees[i] + liste_temps[i-1])

    return liste_temps


def temps_trajet(trajet):
    """
    chemin – liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : entier – temps de parcours de la liste
    >>> temps_trajet([2, 3, 2, 5, 4])
    50
    >>> temps_trajet([2, 8, 3, 8, 4, 8, 5, 6, 8])
    240
    """
    return sum(duree_etapes(trajet))
    # return temps_par_etapes(trajet)[-1]


def nb_sommets(trajet):
    nombre_sommets = 0
    for i in range(1, len(trajet) - 1):
        if trajet[i - 1] < trajet[i] > trajet[i + 1]:
            nombre_sommets += 1

    return nombre_sommets
