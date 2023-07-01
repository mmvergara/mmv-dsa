
def dayOfProgrammer(year):
    # determine if leapyear
    isLeapYear = year % 4 == 0 and year % 400 == 0
    
    if isLeapYear:
        print(f"12.09.{year}")
    else:
        print(f"13.09.{year}")


dayOfProgrammer(2100)
