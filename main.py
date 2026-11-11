from training import *

log = []
kinds = {"бег": 30, "плавание": 45, "йога": 20}
kinds_set = set(kinds)

print("Дневник тренировок")

while True:
    command = input("\nВведите команду:")

    if command == "exit":
        random_phrase()
        print("До свидания!")
        break

    elif command == "help":
        show_help()

    elif command == "list":
        if log:
            for kind, minutes in log:
                print(f"{kind} — {minutes} мин")
        else:
            print("Записей нет.")
    elif command == "total":
        print(f"Общее время тренировок: {total_minutes(log)} мин.")

    elif command == "long":
        long_workouts = [k for k, m in kinds.items() if m > 30]
        if long_workouts:
            print("Тренировки дольше 30 минут:", ", ".join(long_workouts))
        else:
            print("Тренировок дольше 30 минут нет.")

    elif command == "kinds":
        print("Виды тренировок:", ", ".join(k.upper() for k in kinds))

    elif command.startswith("add"):
        parts = command.split(maxsplit=2)

        if len(parts) != 3:
            print("Укажите вид тренировки и количество минут.")
            continue

        _, kind, minutes_text = parts

        try:
            minutes = int(minutes_text)
        except ValueError:
            print("Ошибка: минуты должны быть числом.")
            continue

        if minutes <= 0:
            print("Ошибка: укажите число больше нуля.")
            continue

        log = add_workout(log, kind, minutes)
        kinds[kind] = minutes
        kinds_set = add_kind(kinds_set, kind)
        print("Тренировка добавлена.")

    else:
        print("Данная команда недоступна. Введите help.")
