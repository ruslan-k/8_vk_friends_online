import vk
from getpass import getpass

APP_ID = 5779418  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev

def get_user_login():
    login = input('Введите логин: ')
    while not login:
        login = input('Пустой поле, введите логин повторно: ')
    return login


def get_user_password():
    password = getpass('Введите пароль: ')
    while not password:
        password = getpass('Пустой поле, введите пароль повторно: ')
    return password


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        online_friend_ids = api.friends.getOnline()
        online_friends_list = api.users.get(user_ids=online_friend_ids)
        return online_friends_list
    except vk.exceptions.VkAuthError:
        print('Неверный логин или пароль.')
        exit()


def output_friends_to_console(friends_online):
    if friends_online:
        print('Друзья онлайн:')
        for friend in friends_online:
            print(friend['first_name'], friend['last_name'])
    else:
        print('Нет друзей онлайн')

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
