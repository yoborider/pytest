'''
Soit la liste ["vache", "souris", "levure", "bacterie"]. Affichez l’ensemble des éléments de cette liste (un
élément par ligne) de trois manières différentes (deux avec for et une avec while).
'''
animaux = ["vache", "souris", "levure", "bacterie"]
for animal in animaux:
    print(animal)
print("-")
for i in range(len(animaux)):
    print(animaux[i])
print("-")
i = 0
while i < len(animaux):
    print(animaux[i])
    i+=1
'''
Constituez une liste semaine contenant les 7 jours de la semaine.
Écrivez une série d’instructions affichant les jours de la semaine (en utilisant une boucle for), ainsi qu’une autre série
d’instructions affichant les jours du week-end (en utilisant une boucle while)
'''
semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
print(semaine[0:5:1])
print(semaine[5:7:1])
for jour in semaine[0:len(semaine)-2]:
    print(jour)
print("-")
i=5
while (i<7):
    print(semaine[i])
    i+=1

'''
Avec une boucle, affichez les nombres de 1 à 10 sur une seule ligne.
'''
for i in range(1,11):
    print(i,end="")
'''
Soit impairs la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. Écrivez un programme qui, à partir
de la liste impairs, construit une liste pairs dans laquelle tous les éléments de impairs sont incrémentés de 1.
'''
impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pairs = [x+1 for x in impairs]
'''
Voici les notes d’un étudiant [14, 9, 6, 8, 12]. Calculez la moyenne de ces notes. Utilisez l’écriture formatée pour
afficher la valeur de la moyenne avec deux décimales.
'''
notes = [14, 9, 6, 8, 12]
moy = sum(notes) / len(notes)
print("Moyenne = {:.2f}".format(moy))
'''
Avez les fonctions list() et range(), créez la liste entiers contenant les nombres entiers pairs de 2 à 20 inclus.
Calculez ensuite le produit des nombres consécutifs deux à deux de entiers en utilisant une boucle. Exemple pour les
premières itérations :
8
24
48
[...]
'''
entiers = list(range(2,22,2))
c = 0
res = []
while (c < len(entiers)-1):
    res.append(entiers[c] * entiers[c+1])
    c+=1

'''
Créez un script qui dessine un triangle comme celui-ci
*
**
...sur 10 lignes
'''
for i in range(10):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(1, 11):
    print("*" * i)
'''
Triangle inversé
'''
for i in range(10, 0, -1):
    print("*" * i)

for i in range(1,11):
    print(" "* (11-i) + "*"* i)

'''
Pyramide
'''
rep = input("Nb de lignes : ")
n = int(rep)
for i in range(0,n):
    if (i == 0):
        print(" " * (n - i) + "*")
    else:
        print(" "* (n-i) + "*" + "*"* i + "*" * i)

for i in range(10):
    print("{:^19s}".format("*" * ((2*i)+1)))