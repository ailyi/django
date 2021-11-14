from django.db import models


class User:

    def __init__(self, username, e_mail):

        self.username = username
        self.e_mail = e_mail
