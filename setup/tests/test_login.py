import pytest
from core.models import User
from core import views
from core.views import login, authenticate, deactivate


@pytest.mark.django_db(transaction=True)
def test_user_authenticate():
    # Deve autenticar um usuário no banco de dados, conferindo o username e a senha
    User.objects.create(username='teste', password='teste')
    user = {
        'username': 'teste',
        'password': 'teste'
    }
    user, msg = authenticate(user['username'], user['password'])
    assert type(user) is User


@pytest.mark.django_db(transaction=True)
def test_user_login():
    # Deve fazer o login do usuário criando uma Session no banco de dados
    User.objects.create(username='teste', password='teste')
    user = User.objects.get(username='teste')
    logged = login(user)
    assert logged == "Login feito com sucesso!"


@pytest.mark.django_db(transaction=True)
def test_user_deactivate():
    # Deve desativar o usuário no bando de dados e trocar a senha
    user_data = {
        'username': 'teste',
        'password': 'teste'
    }
    User.objects.create(username='teste', password='teste')
    user = User.objects.get(username='teste')
    deactivate(user)
    user, msg = authenticate(user_data['username'], user_data['password'])
    assert msg == "Senha incorreta!"

