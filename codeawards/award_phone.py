import random

"""
Ecrivez une fonction qui accepte un tableau de 10 nombres entiers (entre 0 et 9)
et qui renvoie une chaîne de ces nombres sous la forme d'un numéro de téléphone.
Le format retourné doit être correct pour que le défi soit relevé.

N'oubliez pas l'espace après les parenthèses fermantes !
"""
def create_phone_number(n):
    #your code here
    tab = [1,2,3,4,5,6,7,8,9,0]
    n_1 = ''.join(map(str, random.sample(tab, 3)))
    n_2 = ''.join(map(str, random.sample(tab, 3)))
    n_3 = ''.join(map(str, random.sample(tab, 4)))

    tel = n_1 + n_2 + n_3
    n = f'({n_1}) {n_2}-{n_3}  **{tel}'
    return n

print(create_phone_number(n=''))
