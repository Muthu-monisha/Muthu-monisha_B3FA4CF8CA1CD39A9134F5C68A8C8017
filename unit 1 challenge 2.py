def leapyear(year):
 if(year%4==0 and year%100!=0) or year%400==0:   
  return True
 else:
  return False
year=int(input("Enter a year: "))
if leapyear(year):
 print("{} is a Leap year.".format(year))
else:
 print("{} not a leap         year.". format(year))