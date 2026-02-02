
# créer une liste de tâches
todo_list = [
    "créer les templates pour l'authentification",
    "réaliser la logique du backend",
    "faire le jeu du pendu",
    "aller faire du shopping",
    "regarder une série",
    "lire un roman"
]
actions = [
    'ajouter un élément à la liste',
    'mettre à jour un élément',
    'retirer un élément de la liste',
    'afficher la liste des éléments',
    'quitter'
]

# definir les fonctions
def print_list(lst):
    for i, element in enumerate(lst, 1):
        print(f"{i}. {element}")

def make_check_choice(prompt, a, b):
    while True:
        choice = input(prompt)
        if choice.isdigit():
            choice = int(choice)
            if a <= choice <= b:
                return choice
            else:
                print("Le nombre n'est pas dans le bon intervalle")
        else:
            print("Ce n'est pas un nombre")

def add_task_to_list():
    task = input('Entrer le nom de la tâche: ')
    todo_list.append(task)

def update_task():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à mettre à jour: ', 1, len(todo_list))
        task = input('Entrer la nouvelle description de la tâche \n>>> ')
        todo_list[task_id - 1] = task
    else:
        print('Impossible de modifier une tâche car la liste est vide')

def remove_task():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à supprimer: ', 1, len(todo_list))
        task = todo_list.pop(task_id - 1)
        print("Vous avez retiré la tâche:", task)
    else:
        print('Impossible de supprimer une tâche car la liste est vide')

def main():
    condition = True
    # boucler indéfiniment pour prendre des requêtes de l'utilisateur
    while condition:
        # afficher le nombre de de tâches
        print("\nVous avez un total de ", len(todo_list), 'tâches')
        # afficher la liste des actions réalisables sur la todolist (add, remove, delete)
        print("\nChoisir une action à réaliser avec son numéro")
        print_list(actions)
        # demander l'action à réaliser
        choice = input('>>> ')
        
        print() # pour sauter une ligne
        # exécuter cette commande de l'utilisateur
        if choice == '1':
            add_task_to_list()
        elif choice == '2':
            update_task()
        elif choice == '3':
            remove_task()       
        elif choice == '4':
            print("LISTE DES TÂCHES")
            print_list(todo_list)     
        elif choice == '5':
            # quitter la boucle
            print("Au revoir")
            condition = False 
        else:
            print('Action indisponible')

if __name__ == '__main__':
    main()
