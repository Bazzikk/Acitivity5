# To verify if a year is a leap year
def leapYear (year = None):

    # Verifying val is a number
    if not(type(year) == type(0)):
        try:
          year = int(year)
        except:
          #print("Error: Invalid Input")
          return False


    # Converting val if negative into a positive number
    if year < 0:
        year = year * -1
    #print("Notice: Converted into a positive number")


    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                #print("It is a leap year")
                 return True
        else:
            #print("It is a leap year")
            return True
    return False
