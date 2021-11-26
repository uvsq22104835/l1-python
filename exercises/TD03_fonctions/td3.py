def affiche(v, labele):
    if v > 1:
        print(v, labele + "s", end=" ") 
    elif v == 1:
        print(v, labele, end=" ")
    
def afficheTemps(temps):
    affiche(temps[0], "jour")
    affiche(temps[1], "heure")
    affiche(temps[2], "minute")
    affiche(temps[3], "seconde")
    print()

def tempsEnSeconde(temps):
    return ((temps[0]*24*3600)+(temps[1]*3600)+(temps[2]*60)+temps[3])


def secondeEnTemps(seconde):
    j=seconde//86400
    h=(seconde%86400)//3600
    m=(seconde%3600)//60
    s=seconde%60
    
    return (j, "jours", h, "heures" , m, "minutes", s, "secondes")

def afficheTemps(temps):
    if (temps[0] != 0):
        if (temps[0] >1):
            print (temps[0], "jours ", end = "")
        else:
            print (temps[0], "jour ", end = "")
    if (temps[1] != 0):
        if (temps[1] >1):
            print (temps[1], "heures ", end = "")
        else:
            print (temps[1], "heure ", end = "")
    if (temps[2] != 0):
        if (temps[2] >1):
            print (temps[2], "minutes ", end = "")
        else:
            print (temps[2], "minute ", end = "")
    if (temps[3] != 0):
        if (temps[3] >1):
            print (temps[3], "secondes ", end = "")
        else:
            print (temps[3], "seconde ", )

def demandeTemps():
    j = int(input("Combien de jours?"))
    h = int(input("Combien d'heures?"))
    if h > 24:
        print("Valeur incohÃ©rente, rentrez la Ã  nouveau")
        h = int(input("Combien d'heures?"))
    m = int(input("Combien de minutes?"))
    if m > 60:
        print("Valeur incohÃ©rente, rentrez la Ã  nouveau")
        m = int(input("Combien de minutes?"))
    s = int(input("Combien de seconde?"))
    if s > 60:
        print("Valeur incohÃ©rente, rentrez la Ã  nouveau")
        s = int(input("Combien de secondes?"))
    return (j,h,m,s)

def sommeTemps(temps1,temps2):
    t = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(t)
    
    
def demandeTemps():
    while True:
         jours = int(input("jours?"))
         heures = int(input("heures?"))
         minutes = int(input("minutes?"))
         secondes = int(input("secondes?"))
         if heures > 24 or minutes > 60 or secondes > 60:
            continue
         return (jours, heures, minutes, secondes)

afficheTemps(demandeTemps())
 
 
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[2] * 60 + temps[1] * 3600 + 24 * 3600 * temps[0] + temps[3]
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(t):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    seconde = t % 60
    t = t // 60
    minute = t % 60
    t = t // 60
    heure = t % 24
    jour = t // 24
    return (jour, heure, minute, seconde)
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def afficheTemps(temps):
    if (temps[0] != 0):
        if (temps[0] >1):
            print (temps[0], "jours ", end = "")
        else:
            print (temps[0], "jour ", end = "")
    if (temps[1] != 0):
        if (temps[1] >1):
            print (temps[1], "heures ", end = "")
        else:
            print (temps[1], "heure ", end = "")
    if (temps[2] != 0):
        if (temps[2] >1):
            print (temps[2], "minutes ", end = "")
        else:
            print (temps[2], "minute ", end = "")
    if (temps[3] != 0):
        if (temps[3] >1):
            print (temps[3], "secondes ", end = "")
        else:
            print (temps[3], "seconde ", )
    
afficheTemps((1,0,14,23))    
def sommeTemps(temps1,temps2):
    t1 = tempsEnSeconde(temps1)
    t2 = tempsEnSeconde(temps2) 
    return secondeEnTemps(t1 + t2)

resultat = sommeTemps((2,3,4,25),(5,22,57,1))
print(resultat)

def proportionTemps(temps,proportion):
    t3 = tempsEnSeconde(temps)
    return secondeEnTemps(int(t3 * proportion))
resultat = afficheTemps(proportionTemps((2,0,36,0),0.2))
print(resultat)

def tempsEnDate(temps):
    jour, heure, minute, seconde = temps 
    annee = 1970 + jour // 365 
    jour = jour % 365 # autre facon jour %= 365 
    return (annee, jour, heure, minute, seconde)


def afficheDate(date = -1):
    affiche(date[0], "annee")
    afficheTemps(date[1:])
    # ou bien 
    annee, jour, heure, minute, seconde = date 
    temps = (jour, heure, minute, seconde)
    afficheTemps(temps)

def bisextile(jour):
année = 1970
while jour > 0:
    if année % 4 == 0 and année % 100 != 0 and année % 400 != 0:
        jour -= 366
        print("l'année est bisextile", année)
    else:
        jour -= 365
    année += 1
        
bisextile(20000)

def nombreBisextile(jour):
    année = 1970
    b = 0
    while jour > 0:
        if année % 4 == 0 and année % 100 != 0 and année % 400 != 0:
            jour = jour - 366  # c est la meme chose que jour -= 366
            b = b + 1 #compteur
        else:
            jour -= 365
        année += 1
    return b


def tempsEnDateBisextile(temps):
    jour, heure, minute, seconde = temps
    return tempsEnDate((jour - nombreBisextile(jour), heure, minute, seconde))
