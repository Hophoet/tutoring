# Exercices 3
lesmodules = ["VBA", "BD", "Python", "Maths"]
lesnotes = [12, 11, [15, 18], [13, 14]]

# Affichage des notes
print('Sara a suivi ?? modules. Voici les notes:')
for index in range(len(lesmodules)):
    print(lesmodules[index], ':', lesnotes[index])

# Calculer la moyenne
moyenne_vba = lesnotes[0]  
moyenne_db = lesnotes[1] 
moyenne_python = sum(lesnotes[2])/len(lesnotes[2])
moyenne_maths = sum(lesnotes[3])/len(lesnotes[3]) 
moyenne_generale = (moyenne_db + moyenne_vba + moyenne_python + moyenne_maths)/len(lesnotes)
print('La moyenne de Sara est: ', moyenne_generale)
