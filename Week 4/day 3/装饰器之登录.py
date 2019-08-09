# __Author__: Han
# __Date__: 2019/1/8

username = 'guest'
password = ''
login_status = 0


def weixin_interface():
    print('weixin logging in')


def authentication(status, login_type):
    def jd_login(func):
        global username, password, login_status
        user = input('username:')
        passwd = input('password:')
        if user == 'han' and passwd == '123':
            username = user
            password = passwd
            login_status = 1
            func()
        else:
            pass



    def weixin_login(func):
        global username, password, login_status
        weixin_interface()
        login_status = 1
        func()

    if status == 0:
        if login_type == 'jd':
            return jd_login
        elif login_type == 'weixin':
            return weixin_login
    else:
        pass


@authentication(login_type='jd', status=login_status)   # home = authentication(home)
def home():
    print('home...')


@authentication(login_type='weixin', status=login_status)
def finance():
    print('finance...')



