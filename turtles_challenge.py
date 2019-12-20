import turtle as tu
from random import randint


# Initialisation du jeu


def getOrder(turtles):	
	order = []
	positions = []

	for t in turtles:
		positions.append((t[1]['x'], t[1]['numero']))
	
	positions.sort(reverse=True)
	
	for pos in positions:
		order.append(pos[1])

	return order[:3]



ts = tu.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue à la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)




# Déclarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
turtles = [
( tu.Turtle(), {"name": "Michelangelo", "numero": 5, "color": "orange", "x": -600, "y": -300}),
(tu.Turtle(), {"name": "Leonardo", "numero": 4, "color": "blue", "x": -600, "y": -150}),
(tu.Turtle(), {"name": "Raphael", "numero": 3, "color": "red", "x": -600, "y": 0}),
(tu.Turtle(), {"name": "Splinter", "numero": 2, "color": "grey", "x": -600, "y": 150}),
(tu.Turtle(), {"name": "Donatello", "numero": 1, "color": "yellow", "x": -600, "y": 300})
]

for turt in turtles:
	turt[0].up()
	turt[0].speed(0)
	turt[0].pencolor(turt[1]['color'])
	turt[0].color(turt[1]['color'])
	turt[0].shape("turtle")
	turt[0].goto(turt[1]['x'], turt[1]['y'])

	turt[0].down()

# Demander de saisir dans la console les prédictions des joeurus 1 et 2 dans le format 1,2,3
predictions_j_1 = input("Prédictions joueur 1 (au format 1,2,3) : ")
predictions_j_2 = input("Prédictions joueur 1 (au format 1,2,3) : ")

predictions_j_1 = predictions_j_1.split(",")
predictions_j_2 = predictions_j_2.split(",")


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui représente le nombre de pixels du déplacement vers la droite
winner = None
while not winner:
	for turt in turtles:
		avancee = randint(0,5)
		turt[1]['x'] += avancee

		turt[0].goto(turt[1]['x'], turt[1]['y'])
		
		if turt[1]['x'] >= 1300/2:
			winner = turt
			break

# Comparer les résultats de la course avec les pronostics des joueurs 
# et afficher le résultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write à la position 0,0

	
turtle_arbitre = tu.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write(winner[1]['name'] + " à gagné", move=True, align="left", font=("Arial", 16, "normal"))

order = getOrder(turtles)

textForWinner = "Personne n'a trouvé les bonnes prédictions"

if predictions_j_1 == order:
	textForWinner += "\r\nJoueur 1 a gagné avec ses prédictions"
if predictions_j_2 == order:
	textForWinner = "\r\nJoueur 2 a gagné avec ses prédictions"

turtle_arbitre.up()
turtle_arbitre.goto(0,50)
turtle_arbitre.down()
turtle_arbitre.write(textForWinner, move=True, align="left", font=("Arial", 16, "normal"))



print("Order is : " + str(order))


tu.mainloop()

