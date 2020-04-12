'''
  Script to test importing the password generator as a module
'''

from password_generator import PasswordGenerator as pg

PASSWORD = pg(9, ['number'])
print(PASSWORD.get_password())
