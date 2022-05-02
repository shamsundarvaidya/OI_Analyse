from datetime import datetime, timedelta
from datetime import date
import csv
import calendar

holidaydates: date = []


def find_holidays():
    if holidaydates:
        return holidaydates
    else:
        with open('holidays.csv') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for entry in csv_reader:
                holidaydates.append(datetime.strptime(entry[2], "%d-%b-%y").date())

            return holidaydates


def is_holiday(dt: date) -> bool:
    holiday_list = find_holidays()
    if dt in holiday_list or dt.weekday() == 5 or dt.weekday() == 6:
        return True
    else:
        return False


def last_day_of_month(d: datetime.date) -> date:
    """Calculate current month last date"""
    return d.replace(day=calendar.monthrange(d.year, d.month)[1])


def getNextWeeklyExpiry(fromdate: date) -> date:
    """get nearest weekly expiry from the given date"""
    # assume given date is expiry
    expDate = fromdate
    # time delta
    tomorrow = timedelta(days=+1)
    yesterday = timedelta(days=-1)
    # increment from given date until next thursday(3) is found.
    for i in range(7):
        if expDate.weekday() == 3:
            if isHoliday(expDate):  # if thurnsday is holiday
                if expDate != fromdate:  # if given date not holiday thursday
                    expDate = expDate + yesterday  # expiry is one day before
                    print(f"next weekly expiry date:{expDate.strftime('%d-%m-%Y')}")
                    return (expDate)
                else:  # if given date is  holiday thursday
                    fromdate = fromdate + tomorrow
                    return getNextWeeklyExpiry(fromdate)  # get expiry of next week
            else:
                print(f"next weekly expiry date:{expDate.strftime('%d-%m-%Y')}")
                return (expDate)
        # go to next day
        expDate = expDate + tomorrow


def getMonthlyExpiry(fromDate: date):
    # time delta
    tomorrow = timedelta(days=+1)
    yesterday = timedelta(days=-1)
    # assume given last day of month is expiry
    lastDay = last_day_of_month(fromDate)
    expDate = lastDay
    # find closest thursday(3) to end of the month
    for i in range(7):
        if expDate.weekday() == 3:  # on thursday
            if isHoliday(expDate):  # if last thurday is holiday
                expDate = expDate + yesterday  # wedensday is the expiry
                break  # exit from loop as expiry is found

            else:  # not holiday
                break  # exit from loop as expiry is found
        # go to next day
        else:
            expDate = expDate + yesterday

    if expDate >= fromDate:  # if month expiry is after given date
        print(f"Monthly expiry date:{expDate.strftime('%d-%m-%Y')}")
        return (expDate)

    else:  # given date is past the month expiry
        return getMonthlyExpiry(lastDay + tomorrow)  # get next month expiry


if __name__ == '__main__':
    curDate = date.today()
    print(f"current date:{curDate.strftime('%d-%m-%Y')}")
    getNextWeeklyExpiry(curDate)
    print(last_day_of_month(curDate))
