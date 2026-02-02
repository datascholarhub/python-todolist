import time
from datetime import datetime

# créer une liste de tâches
todo_list = [
    {
    'name': 'templates',
    'description': "créer les templates",
    'done': False,
    'created': '16/03/2024 - 18:20:34'
    },
    {
    'name': 'back',
    'description': "réaliser la logique du backend",
    'done': True,
    'created': '14/03/2024 - 18:27:34'
    },
    {
    'name': 'shopping',
    'description': "faire du shopping",
    'done': False,
    'created': '14/01/2024 - 10:45:20'
    }
]


# definir les fonctions
def animated_print(string=''):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05) # faire une pause de 0.05 seconde
    print() # pour aller à la ligne

def print_tasks():
    if todo_list:
        status_list = ['Pas encore effectuée', 'Déja effectuée']
        for i, task in enumerate(todo_list, 1):
            name = task['name']
            status = status_list[task['done']]
            animated_print(f"{i}- {name} ({status})")
    else:
        animated_print("Liste vide")

def print_actions(actions):
    animated_print('ACTIONS')
    for i, element in enumerate(actions, 1):
        animated_print(f"{i}. {element[0]}")

def make_check_choice(prompt, a, b):
    while True:
        choice = input(prompt)
        if choice.isdigit():
            choice = int(choice)
            if a <= choice <= b:
                return choice
            else:
                animated_print("Le nombre n'est pas dans le bon intervalle")
        else:
            animated_print("Ce n'est pas un nombre")

def generate_task(task_name, task_description, status=False, created=None):
    if created is None:
        created = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    return {
        'name': task_name,
        'description': task_description,
        'done': status,
        'created': created,
    }

def view_details():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche déja réalisée: ', 1, len(todo_list))
        task = todo_list[task_id - 1]
        print() # saut de ligne
        # on itère sur les paires clés valeurs
        for key, value in task.items():
            animated_print(f"{key.upper()}: {value}")
            # les clés sont en majuscules ...
    else:
        animated_print("Vous n'avez aucune tâche définie")

def add_task_to_list():
    task_name = input('Entrer le nom de la tâche: ')
    task_description = input('Entrer la description de la tâche: ')
    task = generate_task(task_name, task_description)
    todo_list.append(task)
    print('Tâche ajoutée')

def update_task():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à mettre à jour: ', 1, len(todo_list))
        animated_print(f"Mise à jour de la tâche: {todo_list[task_id - 1]['name']}\n")
        task_name = input('Entrer le nouveau nom de la tâche: ')
        task_description = input('Entrer la nouvelle description de la tâche \n>>> ')
        task = generate_task(
            task_name,
            task_description,
            todo_list[task_id - 1]['done'],
            todo_list[task_id - 1]['created'],
        )
        todo_list[task_id - 1] = task
    else:
        animated_print('Impossible de modifier une tâche car la liste est vide')

def mark_task(value):
    status_list = ['non effectuée', 'effectuée']
    status_text = status_list[value]
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à marquer: ', 1, len(todo_list))
        task = todo_list[task_id - 1]
        task['done'] = value
        animated_print(f"La tâche '{task['name']}' est marquée comme {status_text}")
    else:
        animated_print('Impossible de marquer une tâche car la liste est vide')

def mark_task_as_done():
    mark_task(True)

def mark_task_as_not_done():
    mark_task(False)


def remove_task():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à supprimer: ', 1, len(todo_list))
        task = todo_list.pop(task_id - 1)
        animated_print(f"Vous avez retiré la tâche: {task['name']}")
    else:
        animated_print('Impossible de supprimer une tâche car la liste est vide')

def main(actions):
    # boucler indéfiniment pour prendre des requêtes de l'utilisateur
    while True:
        # afficher le nombre de de tâches
        animated_print(f"\nVous avez un total de {len(todo_list)} tâches")
        # demander l'action à réaliser
        animated_print("\nChoisir une action à réaliser avec son numéro")
        choice_id = make_check_choice('>>> ', 1, len(actions)) 
        print() # pour sauter une ligne
        # retouver la fonction à appeler
        command = actions[choice_id - 1][1]
        # éxécuter la commande
        command()
        

if __name__ == '__main__':
    actions = [
        ('Ajouter un élément à la liste', add_task_to_list),
        ('Mettre à jour une tâche', update_task),
        ("Afficher les détails d'une tâche", view_details),
        ('Marquer une tâche comme réalisée', mark_task_as_done),
        ('Marquez comme non réalisée', mark_task_as_not_done),
        ('Retirer un élément de la liste', remove_task),
        ('Afficher la liste des tâches', print_tasks),
        ("Quitter l'application", quit)
    ]

    # afficher la liste des actions réalisables sur la todolist (add, remove, delete)
    print_actions(actions)
    # Programme principal
    main(actions)
