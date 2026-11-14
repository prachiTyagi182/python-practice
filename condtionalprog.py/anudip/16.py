

is_logged_in = True


def authenticate(func):

    def wrapper():
        if not is_logged_in:
            print("Access Denied")
        else:
            func()

    return wrapper


@authenticate
def view_profile():
    print("Profile opened")


view_profile()
