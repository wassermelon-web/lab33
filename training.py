from random import *


def show_help():
    print("Список команд:add <вид> <минуты>, total, list, exit")


def random_phrase():
    phs = ["У вас все получится, вы молодец!", "Продолжайте в том же духе!",
           "Успехов!", "Все к лучшему!", "Вы прекрасны!"]
    print(choice(phs))


def add_workout(log, kind, minutes):
    log += f"{kind} — {minutes} мин \n"
    return log


def total_minutes(current, minutes):
    current += minutes
    return current
