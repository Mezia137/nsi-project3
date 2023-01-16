from random import randint
import turtle
import math
import numpy as np
# Les fonctions pré-programmées sur les listes (count, max, etc...) sont INTERDITES
# Seule l'utilisation de la fonction len() est autorisée !

import argparse
parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')


parser.add_argument('-n', '--npoints',default=10,type=int)      # option that takes a value
parser.add_argument('-l', '--length',default=10,type=int)      # option that takes a value
parser.add_argument('-m', '--minvalue',default=10,type=int)      # option that takes a value
parser.add_argument('-M', '--Maxvalue',default=25,type=int)      # option that takes a value
parser.add_argument('-d', '--drawmode',default='turtle',type=str)      # option that takes a value
args = parser.parse_args()

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
	>>> sum(temps_trajet([2, 3, 2, 5, 4]))
	50
	>>> sum(temps_trajet([2, 8, 3, 8, 4, 8, 5, 6, 8]))
	240
	"""
	t = [0]
	for i in range(len(chemin)-1):
		d = chemin[i+1] - chemin[i]
		if d < 0:
			t.append(5*(-d))
		else:
			t.append(10*d)
			
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
	
	#t.fillcolor("cyan")
	#t.begin_fill()
	#t.goto(ox-p, -10)
	#t.goto(p*(len(chemin)+2), -10)
	#t.goto(p*(len(chemin)+1), 0)
	#t.goto(ox, 0)
	#t.end_fill()

	t.penup()
		
	
	

def main(n=args.npoints,min=args.minvalue,max=args.Maxvalue,drawmode=args.drawmode):
	chemin = denivele(n, min, max)
	print(f"Nombre de hauts sommets : {nb_hauts_sommets(chemin)[0]}")
	print(f"Hauteur des hauts sommets : {nb_hauts_sommets(chemin)[1]}")
	print(f"Temps prévu de la randonnée : {sum(temps_trajet(chemin))}")
	print(f"Nombre de sommets : {nb_sommets(chemin)}")

	if drawmode=='turtle':
		t = turtle.Turtle()
		turtle.Screen().bgcolor("black")
		t.pencolor("white")
		t.pensize(1)
		t.speed(0)
		t.hideturtle()
		t.penup()
		interface(t, chemin)
		turtle.exitonclick()

	if drawmode=='plotly':
		import plotly.graph_objects as go
		from plotly.graph_objs.layout import YAxis,XAxis,Margin
		layout = go.Layout(
			title="Randonée",
			xaxis=XAxis(
				title="Distance"
			),
		xaxis2 = XAxis(
			overlaying= 'x', 
			dtick = 7,
			title = 'Temps',
			side= 'top',
			),
		yaxis=dict(
			title="Hauteur"
			),
		)
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=np.arange(args.npoints)*args.length/args.npoints,y=chemin,fill='tozeroy',mode="markers+text",textposition="top center", hovertemplate = 'Atlitude: %{y}m<extra></extra>',
					text=['{:d} min'.format(int(t/60)) for t in np.cumsum(temps_trajet(chemin))]))
		fig.update_layout(hovermode="x",title='Randonnée',yaxis_range=[0,3*np.max(chemin)])
#		fig.add_trace(go.Scatter(x=np.cumsum(temps_trajet(chemin)),y=chemin,xaxis='x2'))
		fig.write_html('/home/lgostiau/output.html')
	return chemin

	


if __name__ == '__main__':
	# tests des fonctions pouvant être testées avec doctest
	# il ne doit pas y avoir de failure dans votre script final.
	import doctest
	doctest.testmod()
	import sys
	sys.exit(main())
	
	
