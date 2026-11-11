from random import choice


def show_help():
    print("Список команд:")
    print("add <вид> <минуты> — добавить тренировку")
    print("total — показать общее время")
    print("list — показать все тренировки")
    print("long — показать тренировки дольше 30 минут")
    print("kinds — показать все виды тренировок")
    print("help — показать справку")
    print("exit — выйти")


def random_phrase():
    phrases = [
        "У Вас все получится, Вы молодец!",
        "Продолжайте в том же духе!",
        "Успехов!",
        "Все к лучшему!",
        "Вы прекрасны!"
    ]
    print(choice(phrases))


def add_workout(log, kind, minutes):
    log.append((kind, minutes))
    return log


def total_minutes(log):
    return sum(minutes for _, minutes in log)


def add_kind(kinds_set, k):
    kinds_set.add(k)
    return kinds_set


def get_long_workouts(kinds):
    return [k for k, m in kinds.items() if m > 30]


def get_upper_kinds(kinds):
    return [k.upper() for k in kinds]
