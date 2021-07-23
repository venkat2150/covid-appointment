import datetime
from dateutil import relativedelta

def difference_between_dates_without_time(to_date, from_date):
    
    diff=relativedelta.relativedelta(to_date, from_date)
    years=diff.years
    months=diff.months
    days=diff.days
    
    return "{} years, {} months, {} days".format(years, months, days)
    
    

def difference_between_dates_with_times(to_date, from_date):
    
    diff=relativedelta.relativedelta(to_date, from_date)
    years=diff.years
    months=diff.months
    days=diff.days
    hours=diff.hours
    minutes=diff.minutes
    seconds=diff.seconds
    
    return "{} years, {} months, {} days, {} hours, {} minutes, {} seconds".format(years, months, days, hours, minutes, seconds)
    
    

if __name__ == '__main__':
    
    val = input("Enter 1 to enetr date with time or enter 2 to enter date without time: ")
    
    while True:
        if val=="1":
            to_date = input("Enter the date time in the yyyy-mm-dd-Hr-Min-Sec format: ")
            temp = to_date.split("-")
            to_date = datetime.datetime(year=int(temp[0]), month=int(temp[1]), day=int(temp[2]), hour=int(temp[3]), minute=int(temp[4]), second=int(temp[5]))
            from_date = datetime.datetime.now()
            print(difference_between_dates_with_times(to_date, from_date))
            break
        elif val=="2":
            to_date = input("Enter the date time in the yyyy-mm-dd format: ")
            temp = to_date.split("-")
            to_date = datetime.date(year=int(temp[0]), month=int(temp[1]), day=int(temp[2]))
            from_date = datetime.date.today()
            print(difference_between_dates_without_time(to_date, from_date))
            break
        else:
            print("INVALID!!!")
            val = input("Enter 1 to enetr date with time or enter 2 to enter date without time: ")