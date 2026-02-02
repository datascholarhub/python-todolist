
# créer une liste de tâches par défaut pour commencer
todo_list = [
    "créer les templates pour l'authentification",
    "réaliser la logique du backend",
    "faire le jeu du pendu",
    "aller faire du shopping",
    "regarder une série",
    "lire un roman"
]


condition = True
while condition:
    # afficher la liste des actions réalisables sur la todo_list
    print('''
Choisir une action à réaliser avec son numéro
1. ajouter un élément à la liste
2. mettre à jour un élément
3. retirer un élément de la liste
4. afficher la liste des éléments
5. quitter
''')

    # demander l'action à réaliser
    choice = input('>>> ')

    # exécuter cette commande de l'utilisateur
    print() # pour sauter une ligne
    if choice == '1':
        task = input('Entrer le nom de la tâche: ')
        todo_list.append(task) # ajouter l'élément à la liste

    elif choice == '2':
        task_id = int(input('Entrer le numéro de la tâche à mettre à jour: '))
        task = input('Entrer la nouvelle description de la tâche \n>>> ')
        todo_list[task_id - 1] = task # modifier l'élément à l'index task_id - 1.
        # On fait moins 1 puisque rappelez-vous, en Python, on compte à partir de 0.

    elif choice == '3':
        task_id = int(input('Entrer le numéro de la tâche à supprimer: '))
        task = todo_list.pop(task_id - 1)
        print("Vous avez retiré la tâche:", task)

    elif choice == '4':
        print("LISTE DES TÂCHES")
        for i in range(len(todo_list)):
            print(i+1, '.', todo_list[i])

    elif choice == '5':
        # quitter la boucle
        condition = False 

    else:
        print('Action indisponible')