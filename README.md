Tout au long de ce TP, nous allons implémentez une application de gestion de tâches (ToDoList).
Le document n'a pas jamais été révisé donc il est possible que vous y trouvez des erreurs. N'hésitez pas à me le signaler.

- Gmail: [assogbaromaricci@gmail.com](mailto:assogbaromaricci@gmail.com)


# Version 1

Nous allons progressivement mettre en place une appli de ToDoList (en console)

Pour commencer, on va faire simple en ne considérant que le nom ou la description de la tâche.
Après on pourra rajouter des détails comme: le nom de la tâche, sa description, son statut (fait ou pas), sa date et heure de création, la date et heure à laquelle elle doit être accomplie.
Ainsi, on définit la liste d'actions réalisables sur la ToDoList.

1. ajouter un élément à la liste
2. mettre à jour un élément
3. retirer un élément de la liste
4. afficher la liste des éléments

Maintenant, définissons les structures de données à utiliser. Pour la ToDoList elle-même, c'est clair qu'on utilisera une **liste** pour stocker les tâches.
Pourquoi pas les tuples ? Belle question. Mais les tuples sont immuables, non modifiables donc pas très adaptés ici. Alors, au clavier. Créer un premier fichier (vous lui donner le nom qui vous plaît)
*On définit des tâches par défaut dans la ToDoList*

```py
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

Alors, demandons à l'utilisateur l'opération à effectuer sur la liste de tâches
```py
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
*Veuillez avec les idées formulées ci-dessous essayer de coder avant de regarder la proposition de correction.*

- Pour ajouter un élément, vous aurez besoin de la méthode `append` des listes. (il suffit de faire `liste.append(element_a_ajouter)`)
- Pour mettre à jour un élément de la liste, nous allons demander à l'utilisateur d'entrer le numéro de la tâche (noter que le programmeur compte à partir de 0 mais l'utilisateur à partir de 1 et adapter votre code à cet effet).
- Pour retirer/supprimer un élément de la liste, vous pouvez utiliser le méthode `pop` ou `remove` des listes. La méthode `pop` prend en argument l'index de l'élément à supprimer et renvoie l'élément supprimé **mais** `remove` prend en argument l'élément à supprimer. Une troisième possibilité est de d'utiliser le mot-clé `del`. Et un simple `del liste[index]` aura. Je préfère `pop`.
- Pour afficher la liste des éléments, on évitera de faire un simple `print(liste)`. On affichera une tâche par ligne et cela avec les numéros.

Voici une proposition de correction.
```py
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
    for i in range(len(todo_list)):
        print(i+1, '.', todo_list[i])
else:
        print('Action indisponible')
```

Testez plusieurs fois le code pour voir s'il fonctionne bien.
Mais ce n'est pas très intéressant d'éxécuter plusieurs fois le programme... Pour cela, ajoutons une boucle `while` avec une condition toujours vérifié.
Ainsi, on ajoute le fait de quitter la boucle (et donc d'arrêter le programme) aux actions réalisables par l'utilsateur.
Le code final pour la première version de notre application est le suivant:

```py

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
```
Présentons quelques limites de la première version qu'on corrigera à la deuxième.
*Vous pouvez tester pour en être sûr(e)*
- Si l'utilisateur entre du texte qui n'est pas un nombre, ou bien qu'il s'agisse d'un nombre celui est hors des numéros des tâches, notre programme soulève une erreur.
- Si la liste est vide, nous avons également un problème lors de la modification ou de la suppression.

---

# Version 2

**Solutions envisageables aux problèmes posés ci-dessus**
- Pour modifier/suppimer une tâche, vérifier si l'utilisateur a entré un nombre et si ce dernier est valide (si le nombre ne dépasse pas le nombre total de tâches)
- Empêcher la suppression/modification en cas de liste vide.
Autre chose, on a bien envie que la les actions réalisables sur la TodoList soit stockées dans une liste `actions` pour simplifier les choses.
Créer un autre fichier et copier l'ancien code à l'intérieur. On aura  à le modifier.

*Ajouter cette liste après la ToDoList créée en dur dans le code*
```py
# liste des actions réalisables sur la liste de tâches
actions = [
    'ajouter un élément à la liste',
    'mettre à jour un élément',
    'retirer un élément de la liste',
    'afficher la liste des éléments',
    'quitter'
]
```
Lors de la modification  ou de la suppression d'une tâche, nous devons verifier si l'entrée de l'utilsateur est correcte.
Tout d'abord, on vérifie si l'entrée de l'utilisateur est un nombre avec la méthode `isdigit` des chaînes de caractères qui renvoie `True` s'il s'agit d'un nombre et `False` dans le cas échéant. Ex: `chaine.isdigit()` (n'oubliez pas les paranthèses).
Une fois sûr qu'il s'agit d'un nombre, nous devons le convertir et tester s'il est valide: compris entre 1 et la longueur de la liste de tâches.
Allez, essayez par vous-même avant de regarder le résultat suivant.


```py
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
*Nous utilisons le mot-clé `pass` lorsque nous voulons laisser un bloc d'instructions vide*
utilisez cette logique pour 

Maintenant, passons au cas où la liste de tâches est vide. Ajoutez une condition qui vérifie si la liste de tâches et afin d'agir en conséquence, au niveau des blocs d'instructions qui gèrent respectivement la modification et la suppression de tâches.
*Je vous laisse implémenter cela. C'est pas si compliqué*
Ensuite, on peut décider d'afficher les actions réalisables sur la liste de tâches de la même manière qu'on affiche cette dernière (la todolist bien sûr) avec une boucle de type `for ... in ...`.

Alors, l'ensemble du code après les modifications.

```py
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
```

**Problèmes avec ce code**
- On peut constater dans ce code, certaines bouts de code identiques à une différence près. Et du copier-coller, c'est contre le principe **DRY** (*Don't Repeat Yourself*). Il est question dans ce principe de limiter la duplication du code afin d'écrire un code maintenable et facilement modifiable.
- On a bien envie de boucler indéfiniment tant que l'utilisateur n'entre pas un nombre valide

---

# Version 3
Pour cette version de notre appli, nous devons refactoriser le code autant que nous pouvons ... 😊.

- Tout d'abord, on remarque très rapidement que la manière dont les éléments des deux listes (celle des tâches et celle des actions) sont très similaires.
La seule différence est la liste en question.
Ainsi, il serait judicieux de définir une fonction pour l'affichage des éléments de la liste, et cette fonction prendra en argument la liste concernée.

```py
def print_list(lst):
    for i, element in enumerate(lst, 1):
        print(f"{i}. {element}")
```
*Commentaire: la fonction `enumerate` prend en argument un itérable (comme une liste, un tuple...) et retourne un itérable constitué de paires (index, element).*
*Testons rapidement cette fonction pour voir le résultat*

```py
>>> li = ['kiwi', 'bonbon', 'soda', 'jambon']
>>> for i, food in enumerate(li):
...     print(i, food)
...
0 kiwi
1 bonbon
2 soda
3 jambon
```

Cette fonction accepte un second argument optionnel qui indique le nombre à partir duquel il faut commencer par compter.

```py
>>> li = ['kiwi', 'bonbon', 'soda', 'jambon']
>>> for i, food in enumerate(li, 1):
...     print(i, food)
...
1 kiwi
2 bonbon
3 soda
4 jambon
```

Aussi, dans ma fonction, on peut aussi voir `f"{i}. {element}"`. Pas de panique! Il s'agit simplemant d'un f-string.
C'est une technique moderne de formatage de teste en Python. Il suffit de préceder la chaine de caractères de la lettre `f` et puis à l'intérieur de cette indiquer les variables à introduire entre des accolades.

```py
>>> name = "Bruno"
>>> age = 25
>>> print(f"Monsieur {name} a {age} ans.")
Monsieur Bruno a 25 ans.

```

- Passons à la deuxième factorisation: le test de validité sur le nombre.
Pour cela, implémentons une fonction nommée `make_check_choice` qui prend en argument le prompt, les bornes de l'intervalle entier dans lequel le nombre doit être pris. Pour information, le prompt désigne le message qui indique à l'utilisateur ce qu'il doit entrer.

```py
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

Afin de boucler indéfiniment tant que l'utilisateur n'entre pas un nombre valide, nous rajoutons une boucle infinie et le mot-clé `return` dans la fonction nous garantit que la boucle s'arrêtera si le nombre est valide.

```py
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

Voici le code que nous obtenions.

```py
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


condition = True
# boucler indéfiniment pour prendre des requêtes de l'utilisateur
while condition:
    # afficher le nombre de de tâches
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
J'ai remplacé `if len(todo_list) != 0:` par `if todo_list:`. C'est équivalent. En effet, on peut mettre l'objet à la place de la condition sur l'objet dans notre cas ci. Alors, essayons de comprendre comment Python interprète cela. Python interprète une liste vide, un tuple vide, un nombre nul comme False et lorsqu'il s'agit d'une liste/tuple non vide ou d'un entier non nul, Python considère cela comme True.

Pour terminer, definissons les fonctions `add_task_to_list`, `update_task` et `remove_task` pour simplifier le code qui est à l'intérieur des blocs conditionnelles. Puis vient la fonction `main` qui contient le programme principal. et aussi, nous ajoutons une ligne pour afficher le nombre de tâches dans la liste à chaque itération.

```py
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

Nous allons rendre les données un peu plus complexes.

---

# Version 4
Maintenant, nous allons représenter une tâche par un dictionnaire donnant les détails concernant la tâche: nom, description, date et heure de création et statut (déjà fait ou non).

Alors, voici comment se présente notre ToDo List cette fois-ci.
```py
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
*`Done`est à True si la tâche est déjà réalisée ou False au cas contraire et `create` indique la date et l'heure de création. Vous pourriez ajouter d'autres détails mais pour ce TP, ce que nous avons là suffit largement pour faire asseoir les notions ....*

Maintenant, que nous avons faire cette modification. Testons le code.

Après avoir ajouté une tâche et j'affiche la liste des tâches et j'obtiens ceci:

```
LISTE DES TÂCHES
1. {'name': 'templates', 'description': 'créer les templates', 'done': False, 'create': '16/03/2024 - 18:20:34'}     
2. {'name': 'back', 'description': 'réaliser la logique du backend', 'done': True, 'create': '14/03/2024 - 18:27:34'}
3. {'name': 'shopping', 'description': 'faire du shopping', 'done': False, 'create': '14/01/2024 - 10:45:20'}        
4. La tâche du siècle
```

 - D'abord, ce n'est pas très esthétique d'afficher des dictionnaires à l'utilsateur, juste le nom et le statut de la tâche, ça peut suufire. Créons donc une fonction adapté à la l'affichage de notre liste de tâches sous son nouveau format. Rien de compliqué.
```py
def print_tasks():
    if todo_list:
        status_list = ['Pas encore effectuée', 'Déja effectuée']
        for i, task in enumerate(todo_list, 1):
            name = task['name']
            status = status_list[task['done']]
            print(f"{i}- {name} ({status})")
    else:
        animated_print("Liste vide")

# .....

# Et puis vous savez ce qu 'il faut modifier dans la fonction main() 
```
Vous avez remarqué un truc pas nette dans cette fonction: utiliser une valeur booléenne (True or False) comme index de la liste. Eh oui, Python nous accorde cette flexibilité; lorsque nous les utilisons comme index d'un itérable, Python interprète False comme 0 et True comme 1. Ainsi, dans la liste `status_list`, on place "Pas encore effectuée" comme premier élément (d'indice 0 qui correspond au False) et l'autre comme second élément.


Autre chose, l'élément que j'ai rajouté à la liste n'est pas au bon format. Si l'on mettait à jour également une tâche, il ne serait pas au bon format. Il faut alors revoir nos fonctions d'ajout et de modification: il faut demander à l'utilisateur le nom la tâche et sa description.

```py
from datetime import datetime # au début du code

# ......

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
            'done': todo_list[task_id - 1]['done'], # important de conserver l'ancienne valeur de ce champ
            'created': todo_list[task_id - 1]['created'], # et de celui-ci
        }
    else:
        print('Impossible de modifier une tâche car la liste est vide')

```
Alors, super non ? Mais c'est quoi `datetime`  et  `datetime.now().strftime('%d/%m/%Y - %H:%M:%S')` ? 😯 On reste zen, c'est rien de sorcier. Tout d'abord, on importe l'objet `datetime` du module `datetime` qui permet de manipuler les dates et les heures. Le code suivant vous aidera à mieux comprendre.

```py
>>> from datetime import datetime
>>> now = datetime.now() # on récupère la date et l'heure actuelle
>>> now
datetime.datetime(2024, 3, 17, 8, 40, 1, 566195) # représentation de l'objet (année, mois, jour, heure, minute, seconde, microseconde)
>>> print(now)
2024-03-17 08:40:01.566195
>>> str(now) # la fonction str nous propose déja un formattage de la datetime mais nous voulons la personnaliser.
'2024-03-17 08:40:01.566195'
>>> now_formatted = now.strftime('%d/%m/%Y - %H:%M:%S') 
>>> print(now_formatted)
17/03/2024 - 08:40:01
```
 *On indique le format souhaité à la méthode `strftime`. Pour plus d'informations, lisez la documentation locale ou celle en ligne.*


- Nous avons le dictionnaire (représentant une tâche) qui se répète dans les deux fonctions et la seule différence c'est le nom, la description de la tâche, le status et date/heure de création. Ainsi, implémentons une fonction pour factoriser cela. Pour que cette fonction soit flexible, les paramètres **status** et **created** auront une valeur par défaut. 

```py

def generate_task(task_name, task_description, status=False, created=None):
    if created is None:
        # si created est None, cela suppose que ça n'a pas été préciser
        created = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    return {
        'name': task_name,
        'description': task_description,
        'done': status,
        'created': created,
    }
```

La fonction `add_task_to_list` devient plus simple, après modification.

```py
def add_task_to_list():
    task_name = input('Entrer le nom de la tâche: ')
    task_description = input('Entrer la description de la tâche: ')
    task = generate_task(task_name, task_description) # les valeurs par défaut rempliront les autres champs
    todo_list.append(task)
    print('Tâche ajoutée')
```
*Faites de même pour la fonction `update`, et n'oubliez d'indiquer le statut de la tâche et sa date de création*


La fonction de suppression ne change presque pas. Mais n'oublions pas de modifier la ligne suivante dans son code:
```py
print("Vous avez retiré la tâche:", task['name']) # on remplace task par task['name']
```

On aurait pu permettre à l'utilisateur de modifier le statut de la tâche lorqu'il modifie. Mais aussi, l'utilisateur pourrait avoir envie de ne signaler seulement que la tâche est faite. Ainsi, pour faire simple, on détache les deux fonctionnalités. Implémentons la fonction de marquage de tâche. Et si l'utilisateur a par erreur marquer une tâche comme réalisée, il faut qu'il puisse annuler cela.

**Fonction de marquage (réalisée ou non réalisée)**

```py
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

Touchons à l'avant-dernière fonctionnalité de notre application. Affichez les détails d'une tâche spécifique.

```py
def view_details():
    if todo_list:
        task_id = make_check_choice('Entrer le numéro de la tâche déja réalisée: ', 1, len(todo_list))
        task = todo_list[task_id - 1]
        print() # saut de ligne
        # on itère sur les paires clés valeurs
        for key, value in task.items():
            print(f"{key.upper()}: {value}")
            # les clés sont en majuscules ...
    else:
        print("Vous n'avez aucune tâche définie")
```

Il existe une fonction native en Python qui vous permet d'arrêter le programme: la fonction `quit`, nous l'utiliserons ...

Pour terminer, revoyons la liste des actions... Il s'agira maintenant d'un tuple (nom_de_l_action, fonction_a_appeler). Pourquoi cela ? Bah, on peut déja voir qu'on a 8 actions réalisables, donc 8 blocs conditionnels et puis ces if, elif, elif, ...., else, ça saoule.

Donc cette liste est à placer après la définition des fonctions.  

```py
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
```

Remplaçons la fonction `print_list` par celle-ci pour l'adapter au nouveau format de notre liste d'actions
```py
def print_actions(actions):
    print('ACTIONS')
    for i, element in enumerate(actions, 1):
        print(f"{i}. {element[0]}")
```

Et la fameuse fonction `main` se résume à ceci. *Plus simple que jamais*.

Aussi, nous évitons d'enerver l'utilisateur en affichant à chaque fois cette longue liste des actions; juste une fois au début du programme et c'est bon.

```py
def main(actions):
    # boucler indéfiniment pour prendre des requêtes de l'utilisateur
    while True:
        # afficher le nombre de de tâches
        print(f"\nVous avez un total de {len(todo_list)} tâches")
        # demander l'action à réaliser
        print("\nChoisir une action à réaliser avec son numéro")
        choice_id = make_check_choice('>>> ', 1, len(actions)) 
        print() # pour sauter une ligne
        # retouver la fonction à appeler
        command = actions[choice_id - 1][1]
        # éxécuter la commande
        command()

```

**BONUS**
Pour avoir une interface conviviale, nous allons animer l'affichage avec la fonction suivante. C'est si vous voulez....
Au cas où ça vous plairait, remplacer les appels de la fonction `print()` par `animated_print()` qu'on définit comme suit.

```py
import time # au début de votre code

# ...... Notre fonction ne prend qu'une seule chaine de caractères.
# consulter la documentation de la fonction print et de la fonction sleep du module time si vous voulez mieux comprendre

def animated_print(string=''):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05) # faire une pause de 0.05 seconde
    print() # pour aller à la ligne

```
Si vous obtenez une erreur en utilisant cette fonction, rappelez-vous qu'elle ne prend qu'un seul argument.



## **Le code final de la version 4**

```py
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

```


Prochainement, on verra comment enregistrer les tâches dans un fichier pour garantir leurs permanence. Ainsi, notre application sera complète.

A la prochaine.... 
A vous maintenant de personnaliser le code comme vous voulez, rajoutez des fonctionnalités de votre choix. Ce code est loin d'être parfait mais c'est un bon début.
