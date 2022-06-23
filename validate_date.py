import datetime

def validate(d):
    date1 = datetime.datetime.strptime(d, '%Y-%m-%d')
    print(date1)
    date2 = datetime.datetime(2000, 4, 23)
    print(date2)
    if date1 < date2:
        print('es menor')
        return
        


if __name__ == '__main__':
    validate('1999-1-5')