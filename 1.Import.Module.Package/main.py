from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

def main():
    calculate_salary()
    get_employees()
    dt = datetime.datetime.today()
    print('Today: ', dt.strftime("%d %B %Y"))


if __name__ == '__main__':
    main()