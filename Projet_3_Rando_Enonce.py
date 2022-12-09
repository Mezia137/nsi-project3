from random import randint
import turtle
import math

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
	for i in range(len(tab)-1):
		if tab[i] == tab[i+1]:
			return False
			
	return True


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
	while True:
		tab = [randint(mini, maxi) for i in range(n)]
		if test_denivele(tab):
			return (tab)


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
	n = 0
	v = 0
	for i in chemin:
		if i > v:
			v = i
			n = 1
		
		elif i == v:
			n += 1
	
	return (n, v)


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
	t = 0
	for i in range(len(chemin)-1):
		d = chemin[i+1] - chemin[i]
		if d < 0:
			t += 5*(-d)
		else:
			t += 10*d
			
	return t


def nb_sommets(chemin):
	n = 0
	for i in range(1, len(chemin)-1):
		if chemin[i-1] < chemin[i] > chemin[i+1]:
			n += 1
	
	return n

def interface(t, chemin):
	print(chemin)
	
	p=len(chemin)*5
	x = -p*len(chemin)/2
	ox = x-p
	
	t.fillcolor("white")
	t.begin_fill()
	t.goto(ox, 0)
	t.pendown()
	
	for y in chemin:
		t.goto(x, y*5)
		x += p
	
	t.goto(x, 0)
	t.goto(ox, 0)
	t.end_fill()
	
	t.fillcolor("cyan")
	t.begin_fill()
	t.goto(ox-p, -10)
	t.goto(p*(len(chemin)+2), -10)
	t.goto(p*(len(chemin)+1), 0)
	t.goto(ox, 0)
	t.end_fill()

	t.penup()
		
	
	

def main(args):
	chemin = denivele(10, 10, 25)
	print(f"Nombre de hauts sommets : {nb_hauts_sommets(chemin)[0]}")
	print(f"Hauteur des hauts sommets : {nb_hauts_sommets(chemin)[1]}")
	print(f"Temps prévu de la randonnée : {temps_trajet(chemin)}")
	print(f"Nombre de sommets : {nb_sommets(chemin)}")
	
	t = turtle.Turtle()
	turtle.Screen().bgcolor("black")
	t.pencolor("white")
	t.pensize(1)
	t.speed(0)
	t.hideturtle()
	t.penup()
	interface(t, chemin)
	turtle.exitonclick()

	


if __name__ == '__main__':
	# tests des fonctions pouvant être testées avec doctest
	# il ne doit pas y avoir de failure dans votre script final.
	import doctest
	doctest.testmod()
	import sys
	sys.exit(main(sys.argv))
	
	
