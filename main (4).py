
def is loop year(year)
if(year%4==0 and year%100!=0)or year%400==0:
  _return true
else:
  return false
year=int(input("enter a year:"))
if is loop year(year):
print('{}is a loop year.'.format(year))
else  