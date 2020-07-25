class User:
    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1


def main():
    u1 = User("johnsmith10")
    print(User.user_count)
    # User.user_count ➞ 1

    u2 = User("marysue1989")
    print(User.user_count)

    u3 = User("milan_rodrick")
    # User.user_count ➞ 3


if __name__ == '__main__':
    main()
