import calendar
import datetime

today = str(datetime.date.today())
todayYr = int(today[:4])
todayMon = int(today[5:7])
todayDay = int(today[8:])

def ageVerify(year, month, day):
    if todayYr - year > 18:
        return True
    elif todayYr - year < 18:
        return False
    else:
        if todayMon >= month:
            if todayDay >= day:
                return True
            else:
                return False

while 1:
    try:
        userYr = int(input("What year were you born in?: "))
        if userYr > int(today[0:4]) or userYr < 1900:
            print("Please give your real birth year")
            print()
            continue

        userMon = int(input("What month were you born in?: "))
        if userMon > 12 or userMon < 1:
            print("Please give a valid month number")
            print()
            continue

        userDay = int(input("What day were you born in?: "))
        if userDay > calendar.monthrange(userYr, userMon)[1] or userDay < 1:
            print("Please give a valid day")
            continue

        break
    except ValueError:
        print("Please respond with an integer")

if ageVerify(userYr, userMon, userDay) == True:
    print("You are old enough.")
else:
    print("You are not old enough.")
    print("How about going to www.youtube.com?")