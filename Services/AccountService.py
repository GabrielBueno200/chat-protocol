from Repositories.UserRepository import UserRepository
from Auth.Auth import Auth


class AccountService():

    userRepository = UserRepository()

    def signIn(self, username, password):

        users = list(self.userRepository.findByUsername(username))

        if len(users) == 1:

            user = users[0]

            if password == user.password:
                return Auth.logged_user(user)

        return "Incorrect username or password"

    def signOut(self):

        if Auth.logged_user() is not None:
            Auth.logout()
