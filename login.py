import json
import sys


def acquire_username_file(username):
    return "{}.json".format(username)


def acquire_code_file(username):
    return "{}code.json".format(username)


def get_stored_username(filename):
    try:
        with open(filename)as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_stored_code(filename):
    try:
        with open(filename)as file:
            code = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return code


def verify_code(code):
    for i in range(4):
        code_input = input('请输入你的密码')
        if code == code_input:
            print('登录成功')
            break
        else:
            if i <= 2:

                print('密码错误，请输入密码，你还有{}次机会'.format(3 - i))
            else:
                print('次数用光')
                sys.exit()


def get_new_username():
    username = input("请设置你的用户名")
    username = username.strip()
    filename = acquire_username_file(username)
    with open(filename, 'w')as file:
        json.dump(username, file)
    return username


def setup_code(code_file):
    while True:
        code = input('请输入你想要输入的密码')
        code2 = input('请再次输入你想要输入的密码')
        if code == code2:
            with open(code_file, 'w')as file:
                json.dump(code, file)
                break


def great_user():
    user_name = input('请输入你的用户名')
    user_name = user_name.strip()
    username_file = acquire_username_file(user_name)

    username = get_stored_username(username_file)

    if username:
        code_file = acquire_code_file(username)
        code = get_stored_code(code_file)
        if code:
            verify_code(code)
        else:
            setup_code(code_file)
    else:
        print('不存在这个用户名')
        username = get_new_username()
        print('我们会记住这个用户名' + username)
        new_code_file = acquire_code_file(username)
        setup_code(new_code_file)
    return username


great_user()
