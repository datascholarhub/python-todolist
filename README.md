Tout au long de ce TP, nous allons **implémenter** une application de gestion de tâches (ToDoList).
Le document n'a pas été révisé, donc il est possible que vous y **trouviez** des erreurs. N'hésitez pas à me les signaler.

* Gmail : [assogbaromaricci@gmail.com](mailto:assogbaromaricci@gmail.com)

# Version 1

Nous allons progressivement mettre en place une appli de ToDoList (en console).

Pour commencer, on va faire simple en ne considérant que le nom ou la description de la tâche.
Après, on pourra rajouter des détails comme : le nom de la tâche, sa description, son statut (fait ou pas), sa date et heure de création, la date et heure à laquelle elle doit être accomplie.
Ainsi, on définit la liste d'actions réalisables sur la ToDoList :

1. ajouter un élément à la liste
2. mettre à jour un élément
3. retirer un élément de la liste
4. afficher la liste des éléments

Maintenant, définissons les structures de données à utiliser. Pour la ToDoList elle-même, il est clair qu'on utilisera une **liste** pour stocker les tâches.
Pourquoi pas les tuples ? Belle question. Mais les tuples sont immuables, non modifiables, donc pas très adaptés ici. Alors, au clavier ! Créez un premier fichier (vous lui **donnez** le nom qui vous plaît).
*On définit des tâches par défaut dans la ToDoList*

```python
# créer une liste de tâches par défaut pour commencer
todo_list = [
    "créer les templates pour l'authentification",
    "réaliser la logique du backend",
    "faire le jeu du pendu",
    "aller faire du shopping",
    "regarder une série",
    "lire un roman"
]

```

Alors, demandons à l'utilisateur l'opération à effectuer sur la liste de tâches :

```python
# afficher la liste des actions réalisables sur la todo_list
print('''
Choisir une action à réaliser avec son numéro
1 . ajouter un élément à la liste
2 . mettre à jour un élément
3 . retirer un élément de la liste
4 . afficher la liste des éléments
''')

# demander l'action à réaliser
choice = input('>>> ')

```

Maintenant, en fonction du numéro choisi, nous exécuterons l'action. Pour cela, une série d'instructions conditionnelles peut faire l'affaire.
*Veuillez, avec les idées formulées ci-dessous, essayer de coder avant de regarder la proposition de correction.*

* Pour ajouter un élément, vous aurez besoin de la méthode `append` des listes (il suffit de faire `liste.append(element_a_ajouter)`).
* Pour mettre à jour un élément de la liste, nous allons demander à l'utilisateur d'entrer le numéro de la tâche (notez que le programmeur compte à partir de 0, mais l'utilisateur à partir de 1 ; adaptez votre code à cet effet).
* Pour retirer/supprimer un élément de la liste, vous pouvez utiliser la méthode `pop` ou `remove` des listes. La méthode `pop` prend en argument l'index de l'élément à supprimer et renvoie l'élément supprimé, **mais** `remove` prend en argument l'élément à supprimer. Une troisième possibilité est d'utiliser le mot-clé `del`. Un simple `del liste[index]` fera l'affaire. Je préfère `pop`.
* Pour afficher la liste des éléments, on évitera de faire un simple `print(liste)`. On affichera une tâche par ligne, et cela avec les numéros.

Voici une proposition de correction :

```python
# exécuter cette commande de l'utilisateur
print() # pour sauter une ligne
if choice == '1':
    task = input('Entrer le nom de la tâche: ')
    todo_list.append(task) # ajouter l'élément à la liste
elif choice == '2':
    task_id = int(input('Entrer le numéro de la tâche à mettre à jour: '))
    task = input('Entrer la nouvelle description de la tâche \n>>> ')
    todo_list[task_id - 1] = task # modifier l'élément à l'index task_id - 1.
    # On fait moins 1 puisque, rappelez-vous, en Python, on compte à partir de 0.
elif choice == '3':
    task_id = int(input('Entrer le numéro de la tâche à supprimer: '))
    task = todo_list.pop(task_id - 1)
    print("Vous avez retiré la tâche:", task)
elif choice == '4':
    for i in range(len(todo_list)):
        print(i+1, '.', todo_list[i])
else:
    print('Action indisponible')

```

Testez plusieurs fois le code pour voir s'il fonctionne bien.
Mais ce n'est pas très intéressant d'exécuter plusieurs fois le programme... Pour cela, ajoutons une boucle `while` avec une condition toujours **vérifiée**.
Ainsi, on ajoute le fait de quitter la boucle (et donc d'arrêter le programme) aux actions réalisables par l'utilisateur.
Le code final pour la première version de notre application est le suivant :

```python
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

```

Présentons quelques limites de la première version qu'on corrigera dans la deuxième.
*Vous pouvez tester pour en être sûr(e) :*

* Si l'utilisateur entre du texte qui n'est pas un nombre, ou bien un nombre hors de la plage des tâches, notre programme soulève une erreur.
* Si la liste est vide, nous avons également un problème lors de la modification ou de la suppression.

---

# Version 2

**Solutions envisageables aux problèmes posés ci-dessus :**

* Pour modifier/supprimer une tâche, vérifier si l'utilisateur a entré un nombre et si ce dernier est valide (s'il ne dépasse pas le nombre total de tâches).
* Empêcher la suppression/modification en cas de liste vide.

Autre chose : on a bien envie que les actions réalisables sur la ToDoList soient stockées dans une liste `actions` pour simplifier les choses.
Créez un autre fichier et copiez l'ancien code à l'intérieur. On aura à le modifier.

*Ajouter cette liste après la ToDoList créée en dur dans le code :*

```python
# liste des actions réalisables sur la liste de tâches
actions = [
    'ajouter un élément à la liste',
    'mettre à jour un élément',
    'retirer un élément de la liste',
    'afficher la liste des éléments',
    'quitter'
]

```

Lors de la modification ou de la suppression d'une tâche, nous devons vérifier si l'entrée de l'utilisateur est correcte.
Tout d'abord, on vérifie si l'entrée de l'utilisateur est un nombre avec la méthode `isdigit()` des chaînes de caractères qui renvoie `True` s'il s'agit d'un nombre et `False` dans le cas contraire. Ex : `chaine.isdigit()` (n'oubliez pas les parenthèses).
Une fois sûr qu'il s'agit d'un nombre, nous devons le convertir et tester s'il est valide : compris entre 1 et la longueur de la liste de tâches.
Allez, essayez par vous-même avant de regarder le résultat suivant.

```python
task_id = input('Entrer le numéro de la tâche: ')
if task_id.isdigit(): # si l'entrée est un nombre
    task_id = int(task_id) # conversion vers le type int
    if 1 <= task_id <= len(todo_list):
        # vous mettrez ici la logique de l'action à réaliser
        pass
    else:
        print("Le nombre n'est pas dans le bon intervalle")
else:
    print("Ce n'est pas un nombre")

```

*Nous utilisons le mot-clé `pass` lorsque nous voulons laisser un bloc d'instructions vide.*

Maintenant, passons au cas où la liste de tâches est vide. Ajoutez une condition qui vérifie la liste de tâches afin d'agir en conséquence au niveau des blocs d'instructions qui gèrent respectivement la modification et la suppression de tâches.
*Je vous laisse implémenter cela. Ce n'est pas si compliqué.*

Ensuite, on peut décider d'afficher les actions réalisables sur la liste de tâches de la même manière qu'on affiche cette dernière (la ToDoList bien sûr) avec une boucle de type `for ... in ...`.

Alors, voici l'ensemble du code après les modifications :

```python
# version 2.0
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

```

**Problèmes avec ce code :**

* On peut constater dans ce code certains bouts de code identiques à une différence près. Et faire du copier-coller va à l'encontre du principe **DRY** (*Don't Repeat Yourself*). Il s'agit de limiter la duplication afin d'écrire un code maintenable et facilement modifiable.
* On a bien envie de boucler indéfiniment tant que l'utilisateur n'entre pas un nombre valide.

---

# Version 3

Pour cette version de notre appli, nous devons refactoriser le code autant que nous pouvons... 😊.

* Tout d'abord, on remarque très rapidement que la manière dont les éléments des deux listes (tâches et actions) sont affichés est très similaire.
Il serait judicieux de définir une fonction pour l'affichage, qui prendra en argument la liste concernée.

```python
def print_list(lst):
    for i, element in enumerate(lst, 1):
        print(f"{i}. {element}")

```

*Commentaire : la fonction `enumerate` prend en argument un itérable (comme une liste, un tuple...) et retourne un itérable constitué de paires (index, element).*
*Testons rapidement cette fonction pour voir le résultat :*

```python
>>> li = ['kiwi', 'bonbon', 'soda', 'jambon']
>>> for i, food in enumerate(li):
...     print(i, food)
...
0 kiwi
1 bonbon
2 soda
3 jambon

```

Cette fonction accepte un second argument optionnel qui indique le nombre à partir duquel commencer à compter.

```python
>>> li = ['kiwi', 'bonbon', 'soda', 'jambon']
>>> for i, food in enumerate(li, 1):
...     print(i, food)
...
1 kiwi
2 bonbon
3 soda
4 jambon

```

Aussi, dans ma fonction, on peut voir `f"{i}. {element}"`. Pas de panique ! Il s'agit simplement d'un **f-string**.
C'est une technique moderne de formatage de texte en Python. Il suffit de précéder la chaîne de caractères de la lettre `f`, puis d'indiquer les variables à introduire entre accolades.

```python
>>> name = "Bruno"
>>> age = 25
>>> print(f"Monsieur {name} a {age} ans.")
Monsieur Bruno a 25 ans.

```

* Passons à la deuxième factorisation : le test de validité sur le nombre.
Pour cela, implémentons une fonction nommée `make_check_choice` qui prend en argument le prompt et les bornes de l'intervalle entier. Pour information, le prompt désigne le message qui indique à l'utilisateur ce qu'il doit entrer.

```python
def make_check_choice(prompt, a, b):
    choice = input(prompt)
    if choice.isdigit():
        choice = int(choice)
        if a <= choice <= b:
            return choice
        else:
            print("Le nombre n'est pas dans le bon intervalle")
    else:
        print("Ce n'est pas un nombre")

```

Je vous laisse comprendre ce code.

Afin de boucler indéfiniment tant que l'utilisateur n'entre pas un nombre valide, nous rajoutons une boucle infinie, et le mot-clé `return` nous garantit que la boucle s'arrêtera si le nombre est valide.

```python
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

```

Voici le code que nous obtenons :

```python
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

# définir les fonctions
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


condition = True
# boucler indéfiniment pour prendre des requêtes de l'utilisateur
while condition:
    # afficher le nombre de tâches
    print("Vous avez un total de ", len(todo_list), 'tâches')

    # afficher la liste des actions réalisables sur la todolist (add, remove, delete)
    print("\nChoisir une action à réaliser avec son numéro")
    print_list(actions)
    # demander l'action à réaliser
    choice = input('>>> ')

    # exécuter cette commande de l'utilisateur
    if choice == '1':
        task = input('Entrer le nom de la tâche: ')
        todo_list.append(task)

    elif choice == '2':
        if todo_list:
            task_id = make_check_choice('Entrer le numéro de la tâche à mettre à jour: ', 1, len(todo_list))
            task = input('Entrer la nouvelle description de la tâche \n>>> ')
            todo_list[task_id - 1] = task
        else:
            print('Impossible de modifier une tâche car la liste est vide')
    
    elif choice == '3':
        if todo_list:
            task_id = make_check_choice('Entrer le numéro de la tâche à supprimer: ', 1, len(todo_list))
            task = todo_list.pop(task_id - 1)
            print("Vous avez retiré la tâche:", task)
        else:
            print('Impossible de supprimer une tâche car la liste est vide')
              
    elif choice == '4':
        print("LISTE DES TÂCHES")
        print_list(todo_list)
        
    elif choice == '5':
        # quitter la boucle
        print("Au revoir")
        condition = False 
    else:
        print('Action indisponible')

```

J'ai remplacé `if len(todo_list) != 0:` par `if todo_list:`. C'est équivalent. En Python, une liste vide, un tuple vide ou un nombre nul est interprété comme **False**, et lorsqu'il s'agit d'un objet non vide, Python considère cela comme **True**.

Pour terminer, définissons les fonctions `add_task_to_list`, `update_task` et `remove_task` pour simplifier le code à l'intérieur des blocs conditionnels. Puis vient la fonction `main` qui contient le programme principal.

```python
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

# définir les fonctions
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
        # afficher le nombre de tâches
        print("Vous avez un total de ", len(todo_list), 'tâches')
        # afficher la liste des actions réalisables sur la todolist (add, remove, delete)
        print("\nChoisir une action à réaliser avec son numéro")
        print_list(actions)
        # demander l'action à réaliser
        choice = input('>>> ')
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

```

---

# Version 4

Maintenant, nous allons représenter une tâche par un **dictionnaire** donnant les détails concernant la tâche : nom, description, date et heure de création et statut (déjà fait ou non).

```python
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

```

*`done` est à True si la tâche est déjà réalisée ou False dans le cas contraire, et `created` indique la date et l'heure de création.*

Après avoir ajouté une tâche, si j'affiche la liste des tâches, j'obtiens ceci :

```
LISTE DES TÂCHES
1. {'name': 'templates', 'description': 'créer les templates', 'done': False, 'created': '16/03/2024 - 18:20:34'}     
2. {'name': 'back', 'description': 'réaliser la logique du backend', 'done': True, 'created': '14/03/2024 - 18:27:34'}
3. {'name': 'shopping', 'description': 'faire du shopping', 'done': False, 'created': '14/01/2024 - 10:45:20'}        
4. La tâche du siècle

```

D'abord, ce n'est pas très esthétique d'afficher des dictionnaires à l'utilisateur. Afficher juste le nom et le statut peut suffire. Créons donc une fonction adaptée :

```python
def print_tasks():
    if todo_list:
        status_list = ['Pas encore effectuée', 'Déjà effectuée']
        for i, task in enumerate(todo_list, 1):
            name = task['name']
            status = status_list[task['done']]
            print(f"{i}- {name} ({status})")
    else:
        animated_print("Liste vide")

```

Vous avez remarqué un truc particulier dans cette fonction : utiliser une valeur booléenne (True ou False) comme index de la liste. Eh oui, Python interprète False comme 0 et True comme 1 lorsqu'ils sont utilisés comme indices.

Revenons sur les fonctions d'ajout et de modification car le format a changé :

```python
from datetime import datetime # au début du code

def add_task_to_list():
    task_name = input('Entrer le nom de la tâche: ')
    task_description = input('Entrer la description de la tâche: ')
    todo_list.append(
        {
            'name': task_name,
            'description': task_description,
            'done': False,
            'created': datetime.now().strftime('%d/%m/%Y - %H:%M:%S'),
        }
    )
    print('Tâche ajoutée')

def update_task():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à mettre à jour: ', 1, len(todo_list))
        print(f"Mise à jour de la tâche: {todo_list[task_id - 1]['name']}\n")
        task_name = input('Entrer le nouveau nom de la tâche: ')
        task_description = input('Entrer la nouvelle description de la tâche \n>>> ')
        todo_list[task_id - 1] = {
            'name': task_name,
            'description': task_description,
            'done': todo_list[task_id - 1]['done'],
            'created': todo_list[task_id - 1]['created'],
        }
    else:
        print('Impossible de modifier une tâche car la liste est vide')

```

C'est quoi `datetime.now().strftime('%d/%m/%Y - %H:%M:%S')` ? On reste zen. On récupère l'heure actuelle et on la formate. `%d` pour le jour, `%m` pour le mois, `%Y` pour l'année, `%H` pour l'heure, etc.

* Factorisons la création du dictionnaire avec une fonction `generate_task` :

```python
def generate_task(task_name, task_description, status=False, created=None):
    if created is None:
        created = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    return {
        'name': task_name,
        'description': task_description,
        'done': status,
        'created': created,
    }

```

La fonction de suppression ne change presque pas, mais n'oublions pas de modifier l'affichage :

```python
print("Vous avez retiré la tâche:", task['name'])

```

Implémentons aussi le marquage d'une tâche comme faite ou non faite :

```python
def mark_task(value):
    status_list = ['non effectuée', 'effectuée']
    status_text = status_list[value]
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche à marquer: ', 1, len(todo_list))
        task = todo_list[task_id - 1]
        task['done'] = value
        print(f"La tâche '{task['name']}' est marquée comme {status_text}")
    else:
        print('Impossible de marquer une tâche car la liste est vide')

def mark_task_as_done():
    mark_task(True)

def mark_task_as_not_done():
    mark_task(False)

```

Et pour voir les détails complets d'une tâche :

```python
def view_details():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche: ', 1, len(todo_list))
        task = todo_list[task_id - 1]
        print() 
        for key, value in task.items():
            print(f"{key.upper()}: {value}")
    else:
        print("Vous n'avez aucune tâche définie")

```

Pour terminer, organisons nos actions dans un tuple `(nom, fonction)` pour éviter les `elif` à répétition :

```python
actions = [
    ('Ajouter un élément à la liste', add_task_to_list),
    ('Mettre à jour une tâche', update_task),
    ("Afficher les détails d'une tâche", view_details),
    ('Marquer une tâche comme réalisée', mark_task_as_done),
    ('Marquer comme non réalisée', mark_task_as_not_done),
    ('Retirer un élément de la liste', remove_task),
    ('Afficher la liste des tâches', print_tasks),
    ("Quitter l'application", quit)
]

```

**BONUS : Affichage animé**

```python
import time
def animated_print(string=''):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

```

## **Le code complet de la version 4**

```python
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

# définir les fonctions
def animated_print(string=''):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05) 
    print()

def print_tasks():
    if todo_list:
        status_list = ['Pas encore effectuée', 'Déjà effectuée']
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
        task_id = make_check_choice('Entrer le numéro de la tâche : ', 1, len(todo_list))
        task = todo_list[task_id - 1]
        print() 
        for key, value in task.items():
            animated_print(f"{key.upper()}: {value}")
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
    while True:
        animated_print(f"\nVous avez un total de {len(todo_list)} tâches")
        animated_print("\nChoisir une action à réaliser avec son numéro")
        print_actions(actions)
        choice_id = make_check_choice('>>> ', 1, len(actions)) 
        print() 
        command = actions[choice_id - 1][1]
        command()

if __name__ == '__main__':
    actions = [
        ('Ajouter un élément à la liste', add_task_to_list),
        ('Mettre à jour une tâche', update_task),
        ("Afficher les détails d'une tâche", view_details),
        ('Marquer une tâche comme réalisée', mark_task_as_done),
        ('Marquer comme non réalisée', mark_task_as_not_done),
        ('Retirer un élément de la liste', remove_task),
        ('Afficher la liste des tâches', print_tasks),
        ("Quitter l'application", quit)
    ]
    main(actions)

```

Prochainement, on verra comment enregistrer les tâches dans un fichier pour garantir leur permanence. Ainsi, notre application sera complète.

À la prochaine...

À vous maintenant de personnaliser le code comme vous voulez, rajoutez des fonctionnalités de votre choix. Ce code est loin d'être parfait mais c'est un bon début.
