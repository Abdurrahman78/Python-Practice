#implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
#wherein the month in the latter might be any of the values in the list below:

#1636-09-08
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date=input("Date: ")
        if "/" in date:
            slash_list=date.split('/')
            month=int(slash_list[0])
            day=int(slash_list[1])
            year=int(slash_list[2])
            if month>12 or day>31:
                continue
            else:
                print(f"{year}-{month:02}-{day:02}")
                break
        else:
            new_date=date.split(',')
            month_and_day=new_date[0].split(" ")
            if month_and_day[0] in months:
                year=new_date[1].split(" ")
                newYear=int(year[1])
                month=months.index(month_and_day[0])+1
                day=int(month_and_day[1])
                if day>31 or month>12:
                    continue
                else:
                    print(f"{newYear}-{month:02}-{day:02}")
                    break
    except (ValueError,IndexError):
        pass

