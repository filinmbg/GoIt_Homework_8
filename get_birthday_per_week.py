from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "John", "birthday": datetime(year=1978, month=7, day=30)},
    {"name": "Bill", "birthday": datetime(year=1988, month=8, day=2)},
    {"name": "Jane", "birthday": datetime(year=1992, month=8, day=28)},
    {"name": "Adam", "birthday": datetime(year=2002, month=7, day=31)},
    {"name": "Marius", "birthday": datetime(year=2003, month=8, day=5)},
    {"name": "Sabine", "birthday": datetime(year=1988, month=7, day=29)},
]


def get_birthdays_per_week(users):
    # Отримуємо поточну дату:
    current_date = datetime.now().date()
    # Визначаємо кінець тижня (кінцеву дату):
    end_of_week = current_date + timedelta(days=7)
    # Створюємо словник для збереження користувачів по днях тижня
    birthdays_per_week = defaultdict(list)

    for user in users:
        # Змінюємо рік народження на поточний
        bday_date = datetime(
            year=current_date.year,
            month=user["birthday"].month,
            day=user["birthday"].day,
        ).date()

        if current_date <= bday_date < end_of_week:
            if bday_date.weekday() >= 5:  # Якщо день народження в суботу або неділю
                # Призначаємо привітання на понеділок
                next_monday = bday_date + timedelta(days=(7 - bday_date.weekday()))
                birthdays_per_week[next_monday].append(user["name"])
            else:
                # Додаємо користувача до відповідного дня тижня
                birthdays_per_week[bday_date].append(user["name"])

    return birthdays_per_week


if __name__ == "__main__":
    birthdays_dict = get_birthdays_per_week(users)
    for date, names in birthdays_dict.items():
        # Отримуємо назву дня тижня для відповідної дати

        day_name = date.strftime("%A")
        # Форматуємо список користувачів у зручний рядок
        names_str = ", ".join(names)
        print(f"{day_name}: {names_str}")
