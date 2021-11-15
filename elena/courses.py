affichage = """
************** MENU GENERAL **************
    Gesion 
        1. Afficher les courses
        2. Ajouter des courses
        3. Suprimer des courses
        4. Mettre à jour des courses
    Fin
        0. Quitter l'application
******************************************
Choix: """

# Represente l'etat de l'application
active = True
# Les courses 
coures_keys = ['Types', 'Dates', 'Villes', 'Meilleur temps']
courses = [
    #https://results.nyrr.org/event/108/finishers
    {
        'typec':'Marathon',
        'datec':'6/11/2011',
        'lieuc':'New York City',
        'tempsrecord':'02:05:06',
    },
    {
        'typec':'semi-marathon',
        'datec':'12/03/20',
        'lieuc':'bruxelle',
        'tempsrecord':'12:09:00',
    },
    {
        'typec':'semi-marathon',
        'datec':'12/03/20',
        'lieuc':'bruxelle',
        'tempsrecord':'12:09:00',
    },
    {
        'typec':'semi-marathon',
        'datec':'12/03/20',
        'lieuc':'bruxelle',
        'tempsrecord':'12:09:00',
    },
]



while active:
    choix = int(input(affichage))
    if choix == 0:
        active = False
        print("Vous avez quitter l'application")
    elif choix == 2:
        print('Ajouter une course')
        typec = input('Entrer le type de la course: ')
        lieuc = input('Entrer la ville de la course: ')
        tempsrecord = input('Entrer le temps record de la course(jj/mm/aa): ')
        course = {'typec':typec, 'lieuc': lieuc, 'tempsrecord':tempsrecord}
        for key, value in course.items():
            #
            print(f'\t{key} : {value}')
        enregistrer_choix = input('Voulez-vous enregistrer cette course(Oui/Non): ')
        if enregistrer_choix == 'Oui':
            print("La course a été enrégister avec succes!")    
            courses.append(course)
        elif enregistrer_choix == 'Non':
            print("La course n'a pas été enrégister")    
            
    

    elif choix == 1:
        # recupération des villes des coures (tout en evitant les doublons)
        villes = [course.get('lieuc') for course in courses]
        villes = set(villes)
        villes = list(villes)
        # affichage des villes
        print(f'\nNombre de villes: {len(villes)}')
        for ville_index in range(len(villes)):
            print(f'{ville_index+1}. {villes[ville_index]}')
        # affichage des courses
        print(f'\nNombre de coures: {len(courses)}')
        for course_index in range(len(courses)):
            print(f'{course_index + 1}. ')
            for course_cle, course_valeur in courses[course_index].items():
                print(f'\t{course_cle}: {course_valeur}')
        # affichage des courses par ville
        print('\nCourses par villes')
        for ville in villes:
            print(ville)
            i = 1
            for course in courses:
                if course.get('lieuc') == ville:
                    print(f'{i}. ')
                    for course_cle, course_valeur in course.items():
                        print(f'\t{course_cle}: {course_valeur}')
                    i += 1
        



        # ce print c'est pour annuller la tabulation
        # print()
        # afficher les coures
        # for course in courses:
        #     #
        #     for course_value in course.values():
        #         print(course_value, end='\t\t')

        
