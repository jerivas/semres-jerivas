from django.template.defaultfilters import yesno

__version__ = "0.0.dev0"  # DO NOT EDIT: Updated automatically

MSG = 5


def hello(count=0):
    return "Hello world {}! {}".format(MSG, count)


def goodbye(name="Joe"):
    return "Goodbye {} {}".format(MSG, name)


def my_yesno(*args, **kwargs):
    return yesno(*args, **kwargs)
