import datetime

current_year = datetime.datetime.now().year
pass_list = []

work_days = {"Monday": [],
             "Tuesday": [],
             "Wednesday": [],
             "Thursday": [],
             "Friday": []}
weekend_days = {"Saturday": work_days.get("Monday"),
                "Sunday": work_days.get("Monday"),
                **work_days}

def get_birthdays_per_week(users):
    DELTA = 1
    while DELTA !=8:
        for user in users:
            days_in_week = datetime.datetime.now() + datetime.timedelta(days=DELTA)
            for value in user.values():
                if type(value) != str:
                    if value.month == days_in_week.month and value.day == days_in_week.day:
                        pass_list.append(user)
        DELTA += 1
    for user in pass_list:
        date = user.get("birthday")
        replace_year_birthday = date.replace(year=current_year)
        day = replace_year_birthday.strftime("%A")
        weekend_days.get(day).append(user.get("name"))

    for work_day in work_days.keys():
        names_ = work_days.get(work_day)
        valid = ", ".join(names_)
        if len(names_) != 0:
            print(f"{work_day}: {valid}")


get_birthdays_per_week([{"name": "Dmytro", "birthday": datetime.datetime(1998, 5, 23)},
                        {"name": "Mike", "birthday": datetime.datetime(1998, 5, 19)},
                        {"name": "Oleg", "birthday": datetime.datetime(1998, 5, 26)},
                        {"name": "Alex", "birthday": datetime.datetime(1998, 5, 21)}])
