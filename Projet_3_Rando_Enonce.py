from random import randint

# Les fonctions pré-programmées sur les listes (count, max, etc...) sont INTERDITES
# Seule l'utilisation de la fonction len() est autorisée !

def test_denivele(tab):
    """
    tab – liste d'entiers
    Sortie : booléen – True si tab contient des éléments
             successifs distincts, False sinon.
    >>> test_denivele([1, 2, 3, 1, 2, 3])
    True
    >>> test_denivele([1, 2, 3, 1, 2, 2])
    False
    """
    pass


def denivele(n, mini, maxi):
    """
    n – entier strictement positif
    mini, maxi – entiers strictement positifs avec mini < maxi
    Sortie : liste – liste de n entiers aléatoires compris
             entre mini (inclus) et maxi (inclus). Attention,
             deux éléments successifs doivent être distincts.
    >>> test_denivele(denivele(5, 1, 4))
    True
    >>> test_denivele(denivele(20, 1, 8))
    True
    """
    pass


def nb_hauts_sommets(chemin):
    """
    chemin – liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : couple d'entiers – le nombre d'occurrences du plus
             grand élément de la liste et sa valeur.
    >>> nb_hauts_sommets([2, 3, 2, 5, 4])
    (1, 5)
    >>> nb_hauts_sommets([2, 8, 3, 8, 4, 8, 5, 6, 8])
    (4, 8)
    """
    pass


def temps_trajet(chemin):
    """
    chemin – liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : entier – temps de parcours de la liste
    >>> temps_trajet([2, 3, 2, 5, 4])
    50
    >>> temps_trajet([2, 8, 3, 8, 4, 8, 5, 6, 8])
    240
    """
    pass


def nb_sommets(chemin):
    pass





if __name__ == '__main__':
    # tests des fonctions pouvant être testées avec doctest
    # il ne doit pas y avoir de failure dans votre script final.
    import doctest
    doctest.testmod()
    
    
