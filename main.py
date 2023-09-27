from datetime import date, datetime


def get_birthdays_per_week(users):
    birthdayers = {}
    today = date.today()

    for u in users:
        if (today.month < u['birthday'].month):
            next_birthday = datetime(today.year, u['birthday'].month, u['birthday'].day)
        elif (today.month == u['birthday'].month) and (today.day <= u['birthday'].day):
            next_birthday = datetime(today.year, u['birthday'].month, u['birthday'].day)
        elif (today.month == u['birthday'].month) and (today.day > u['birthday'].day):
            next_birthday = datetime(today.year + 1, u['birthday'].month, u['birthday'].day)
        else:
            next_birthday = datetime(today.year + 1, u['birthday'].month, u['birthday'].day)

        delta = next_birthday.date() - today
        if delta.days > 7:
            continue
        
        if next_birthday.weekday() >= 5:
            day_week = 'Monday'
        else:
            day_week = next_birthday.strftime('%A')
        if day_week not in birthdayers:
            birthdayers[day_week] = []
        birthdayers[day_week].append(u['name'])
    return birthdayers


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
