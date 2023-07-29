from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {'name': 'Bill', 'birthday': datetime(year=1988, month=8, day=2)},
    {'name': 'John', 'birthday': datetime(year=1978, month=7, day=30)},
    {'name': 'Jane', 'birthday': datetime(year=1992, month=8, day=28)},
    {'name': 'Adam', 'birthday': datetime(year=2002, month=7, day=31)},
    {'name': 'Marius', 'birthday': datetime(year=2003, month=1, day=20)},
    {'name': 'Sabine', 'birthday': datetime(year=1988, month=3, day=23)},
]


def day_of_week (day):
    day_of_week = {
     'Monday':    0,
     'Tuesday' :  1,
     'Wednesday': 2,
     'Thursday' : 3,
     'Friday' :   4,
     'Saturday' : 5,
     'Sunday' :   6
}
    
    for key, value in day_of_week.items():
        if value == day:
            result = key
            break
    return result 


def get_birthdays_per_week(users):
    # Отримуємо поточну дату:
    current_date = datetime.now().date() 
    # Визначаємо кінець тижня(кінцеву дату):
    end_of_week = current_date + timedelta(days=7) 
    # Створюємо значення за замовчуванням для ключів, які ще не існують у словнику. 
    # Та для кожного нового ключа створюємо пустий список.
    grouped_birthdays = defaultdict(list) 

    for user in users:
        #Змінюємо рік народження на поточний
        bday_date = datetime(year = current_date.year, month = user['birthday'].month, day = user['birthday'].day).date() 
                
        if current_date < bday_date <= end_of_week:
            if bday_date.weekday() != 5 and bday_date.weekday() != 6: # в список grouped_birthdays додаємо імена юзерів
                grouped_birthdays[day_of_week(bday_date.weekday())].append(user['name'])
            elif bday_date.weekday() == 5: #Юзерів з днем народження в суботу додаємо в список понеділка
                grouped_birthdays[day_of_week(0)].append(user['name'])
            elif bday_date.weekday() == 6: #Юзерів з днем народження в неділю додаємо в список понеділка
                grouped_birthdays[day_of_week(0)].append(user['name'])

    return grouped_birthdays


if __name__ == '__main__':
    dict = get_birthdays_per_week(users)
    for key, value in dict.items():
        print("{:<10}: {:<20}" .format(key, ', '.join(map(str, value))))   