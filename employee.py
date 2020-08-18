"""A simple employee class which accepts three parameters i.e. firstname, lastname and pay"""
class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    """@property allow us to define the email as a method but we can use it as an attrivute"""
    @property
    def email(self):
        """Returns the valid email address of a person"""
        return '{}.{}@email.com'.format(self.first, self.last)

    """@property allow us to define the fullname as a method but we can use it as an attrivute"""
    @property
    def fullname(self):
        """Returns the fullname of a person"""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Gives 5% raise to each employee"""
        self.pay = int(self.pay * self.raise_amt)
