# Ecrivez votre code ici !
nombres = input("Entrer les nombres séparés par des virgules: ")

liste = nombres.split(",")
print('liste de nombres: ', liste)

liste_entier = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entier.append(nombre_entier)
    
print('liste de nombres: ', liste_entier)
    
somme = 0
for nombre in liste_entier:
    somme += nombre

print(f"La somme des nombres est égale à {somme}")

moyenne = somme / len(liste_entier)
print(f"La moyenne des nombres est égale à {moyenne}")

nombre_au_dessus_moyenne = []
for nombre in liste_entier:
    if nombre > moyenne:
        nombre_au_dessus_moyenne.append(nombre)
    else:
        continue
    
print(f"les nombres au dessus de la moyenne sont {nombre_au_dessus_moyenne}")

nombre_pair = []
for nombre in liste_entier:
    if nombre % 2 == 0:
        nombre_pair.append(nombre)
        
print(f"les nombres pairs sont : {nombre_pair}")