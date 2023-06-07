from django.shortcuts import render
import datetime
from core.models import User, Session


import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# implementação que vai dar erro no teste
# def authenticate(username, password):
#     user = User.objects.get(username=username)
#     if user.password != password:
#         return f'Senha incorreta!'
#     return f'Usuário Autenticado'


# implementação que vai passar no teste
def authenticate(username, password):
    user = User.objects.get(username=username)
    if user.password != password:
        return None, f'Senha incorreta!'
    return user, None


# implementação que vai falhar no teste
# def login(user):
#     authenticated_user, msg = authenticate(user.username, user.password)
#     if msg is not None:
#         return msg
#     session = Session.objects.create(user=authenticated_user)
#     session.end_date = session.start_date + datetime.timedelta(hours=2)


# implementação que vai passar no teste
def login(user):
    authenticated_user, msg = authenticate(user.username, user.password)
    if msg is not None:
        return msg
    session = Session.objects.create(user=authenticated_user)
    session.end_date = session.start_date + datetime.timedelta(hours=2)
    return "Login feito com sucesso!"


# implementação que vai passar no teste
# def deactivate(user):
#     user.active = False
#     user.password = get_random_string(16)
#     user.save()
#     return user.password


# implementação que vai falhar no teste
def deactivate(user):
    user.active = False
    return user.password


# implementação que vai passar no teste
def change_password(user, new_password1, new_password2):
    if new_password1 != new_password2:
        return f'As senhas não são iguais.'
    if user.password == new_password1:
        return f'A nova senha não pode ser igual a anterior.'
    user.password = new_password1
    user.save()
    return f'Senha alterada com sucesso.'


# implementação que vai falhar no teste
# def change_password(user, new_password1, new_password2):
#     if new_password1 != new_password2:
#         return f'As senhas não são iguais.'
#     if user.password == new_password1:
#         return f'A nova senha não pode ser igual a anterior.'
#     user.password = new_password1
#     return f'Senha alterada com sucesso!'


