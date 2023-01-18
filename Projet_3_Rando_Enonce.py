import turtle
from random import randint

import numpy as np


# Les fonctions pré-programmées sur les listes (count, max, etc...) sont INTERDITES
# Seule l'utilisation de la fonction len() est autorisée !

# import argparse
# parser = argparse.ArgumentParser(
#                    prog = 'ProgramName',
#                    description = 'What the program does',
#                    epilog = 'Text at the bottom of help')


# parser.add_argument('-n', '--npoints',default=20,type=int)      # option that takes a value
# parser.add_argument('-l', '--length',default=20,type=int)      # option that takes a value
# parser.add_argument('-m', '--minvalue',default=1500,type=int)      # option that takes a value
# parser.add_argument('-M', '--Maxvalue',default=2500,type=int)      # option that takes a value
# parser.add_argument('-d', '--drawmode',default='turtle',type=str)      # option that takes a value
# args = parser.parse_args()

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
        trajet = [randint(hauteur_min, hauteur_max) for i in range(nombre_etapes)]
        if test_denivele(trajet):
            return (trajet)


def positions_hauts_sommets(trajet):
    """
    trajet - liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : liste des indices du plus grand élément
             de la liste trajet.
    >>> positions_hauts_sommets([2, 3, 2, 5, 4])
    [3]
    >>> positions_hauts_sommets([2, 8, 3, 8, 4, 8, 5, 6, 8])
    [1, 3, 5, 8]
    """

    liste_positions = []
    hauteur_hauts_sommets = 0
    for position in range(len(trajet)):
        if trajet[position] > hauteur_hauts_sommets:
            hauteur_hauts_sommets = trajet[position]
            liste_positions = [position]

        elif trajet[position] == hauteur_hauts_sommets:
            liste_positions.append(position)

    return liste_positions


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


def temps_par_etapes(trajet):
    """
    trajet – liste d'entiers dont deux éléments successifs sont
             distincts.
    Sortie : liste – temps pour chaques étapes
    >>> sum(temps_par_etapes([2, 3, 2, 5, 4]))
    50
    >>> sum(temps_par_etapes([2, 8, 3, 8, 4, 8, 5, 6, 8]))
    240
    """
    liste_durees = [0]
    for i in range(len(trajet) - 1):
        denivele = trajet[i + 1] - trajet[i]
        if denivele < 0:
            liste_durees.append(5 * (-denivele))
        else:
            liste_durees.append(10 * denivele)

    return liste_durees


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
    return sum(temps_par_etapes(trajet))


def nb_sommets(trajet):
    nombre_sommets = 0
    for i in range(1, len(trajet) - 1):
        if trajet[i - 1] < trajet[i] > trajet[i + 1]:
            nombre_sommets += 1

    return nombre_sommets


def interface(t, chemin):
    print(chemin)

    p = len(chemin) * 5
    x = -p * len(chemin) / 2
    ox = x - p

    t.fillcolor("white")
    t.begin_fill()
    t.goto(ox, 0)
    t.pendown()

    for y in chemin:
        t.goto(x, y * 5)
        x += p

    t.goto(x, 0)
    t.goto(ox, 0)
    t.end_fill()

    # t.fillcolor("cyan")
    # t.begin_fill()
    # t.goto(ox-p, -10)
    # t.goto(p*(len(chemin)+2), -10)
    # t.goto(p*(len(chemin)+1), 0)
    # t.goto(ox, 0)
    # t.end_fill()

    t.penup()


# def main(n=args.npoints,min=args.minvalue,max=args.Maxvalue,drawmode=args.drawmode):
def main(n=20, hauteur_min=1500, hauteur_max=2500, drawmode='plotly'):
    chemin = denivele(n, hauteur_min, hauteur_max)
    print(f"Nombre de hauts sommets : {nb_hauts_sommets(chemin)[0]}")
    print(f"Hauteur des hauts sommets : {nb_hauts_sommets(chemin)[1]}")
    print(f"Temps prévu de la randonnée : {temps_trajet(chemin)}")
    print(f"Nombre de sommets : {nb_sommets(chemin)}")

    if drawmode == 'turtle':
        t = turtle.Turtle()
        turtle.Screen().bgcolor("black")
        t.pencolor("white")
        t.pensize(1)
        t.speed(0)
        t.hideturtle()
        t.penup()
        interface(t, chemin)
        turtle.exitonclick()

    if drawmode == 'plotly':
        import plotly.graph_objects as go
        from plotly.graph_objs.layout import XAxis
        layout = go.Layout(title="Randonée",
                           xaxis=XAxis(title="Distance"),
                           xaxis2=XAxis(overlaying='x',
                                        dtick=7,
                                        title='Temps',
                                        side='top',
                                        ),
                           yaxis=dict(title="Hauteur"),
                           )
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=np.arange(n) * n / n,
                                 y=chemin,
                                 fill='tozeroy',
                                 mode="markers+text",
                                 textposition="top center",
                                 # hovertemplate = 'Atlitude: %{y}m<extra></extra><br/>'+['Temps {:d} min'.format(int(t/60)) for t in np.cumsum(temps_trajet(chemin))],
                                 hovertemplate=['Temps: {:d} min<extra></extra>'.format(int(t / 60)) for t in
                                                np.cumsum(temps_par_etapes(chemin))],
                                 # text=['{:d} min'.format(int(t/60)) for t in np.cumsum(temps_trajet(chemin))],
                                 # y='altitude (m)',x='trajet (km)',
                                 ))
        for position in positions_hauts_sommets(chemin):
            print(position)
            fig.add_annotation(x=position, y=chemin[position], text=f" sommet le plus haut: {chemin[position]} m ",
                               bgcolor="#7F062A", opacity=0.6, )
        fig.update_layout(hovermode="x", title='Randonnée', yaxis_range=[0, 3 * np.max(chemin)], template="plotly_dark")
        #       fig.add_trace(go.Scatter(x=np.cumsum(temps_trajet(chemin)),y=chemin,xaxis='x2'))
        fig.write_html('./output.html')
    return chemin


if __name__ == '__main__':
    # tests des fonctions pouvant être testées avec doctest
    # il ne doit pas y avoir de failure dans votre script final.
    import doctest

    doctest.testmod()
    import sys

    sys.exit(main())
