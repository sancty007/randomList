import random

liste = ["Docteur_D","cap","ibucap","BID","jeChangeDeCap","Outsider",]

liste_1 = []
liste_2 = []

liste = random.sample(liste,len(liste))

liste_1 = liste[:int(len(liste)/2)]

liste_2 = liste[int(len(liste)/2):]

print(liste_1)
print(liste_2)
