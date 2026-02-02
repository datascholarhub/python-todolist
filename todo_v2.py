
# créer une liste de tâches par défaut pour commencer
todo_list = [
    "créer les templates pour l'authentification",
    "réaliser la logique du backend",
    "faire le jeu du pendu",
    "aller faire du shopping",
    "regarder une série",
    "lire un roman"
]

# liste des actions réalisables sur la liste de tâches
actions = [
    'ajouter un élément à la liste',
    'mettre à jour un élément',
    'retirer un élément de la liste',
    'afficher la liste des éléments',
    'quitter'
]


condition = True
while condition:
    # afficher la liste des actions réalisables sur la todo_list
    print("\nChoisir une action à réaliser avec son numéro")
    for i in range(len(actions)):
        print(i+1, '.', actions[i])
    # demander l'action à réaliser
    choice = input('>>> ')

    # exécuter cette commande de l'utilisateur
    print() # pour sauter une ligne
    if choice == '1':
        task = input('Entrer le nom de la tâche: ')
        todo_list.append(task) # ajouter l'élément à la liste

    elif choice == '2':
        if len(todo_list) != 0:
            task_id = input('Entrer le numéro de la tâche à mettre à jour: ')
            if task_id.isdigit(): # si l'entrée est un nombre
                task_id = int(task_id) # conversion vers le type int
                if 1 <= task_id <= len(todo_list):
                    # vous mettrez ici la logique de l'action à réaliser
                    task = input('Entrer la nouvelle description de la tâche \n>>> ')
                    todo_list[task_id - 1] = task # modifier l'élément à l'index task_id - 1.
                else:
                    print("Le nombre n'est pas dans le bon intervalle")
            else:
                print("Ce n'est pas un nombre")
        else:
            print('Impossible de modifier une tâche car la liste est vide')

    elif choice == '3':
        if len(todo_list) != 0:
            task_id = input('Entrer le numéro de la tâche à supprimer: ')
            if task_id.isdigit(): # si l'entrée est un nombre
                task_id = int(task_id) # conversion vers le type int
                if 1 <= task_id <= len(todo_list):
                    # vous mettrez ici la logique de l'action à réaliser
                    task = todo_list.pop(task_id - 1)
                    print("Vous avez retiré la tâche:", task)
                else:
                    print("Le nombre n'est pas dans le bon intervalle")
            else:
                print("Ce n'est pas un nombre")
        else:
            print('Impossible de supprimer une tâche car la liste est vide')

    elif choice == '4':
        print("LISTE DES TÂCHES")
        for i in range(len(todo_list)):
            print(i+1, '.', todo_list[i])

    elif choice == '5':
        # quitter la boucle
        condition = False 

    else:
        print('Action indisponible')