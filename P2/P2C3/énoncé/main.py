# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

annuel = float(input("Indiquer votre salaire annuel: "))
travaillees = float(input("Indiquer le nombre d'heure travailler: "))

mensuel = salaire_mensuel(annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, travaillees)

print(f"Votre salaire horaire est de {horaire} $")