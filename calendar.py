def getMonth():
  month = 0
  while int(month) < 1 or int(month) > 12:
    month = input("Enter month: ")
    if int(month) < 1 or int(month) > 12:
      print("ERROR: Month must be between 1 and 12\n")
  return int(month)

def getYear():
  #it has to be lower than 1753 or else it will continue to display error
  year = 1752
  while int(year) < 1753:
    year = input("Enter year: ")
    if int(year) < 1753:
      print("ERROR: Year must be 1753 or later\n")
  return int(year)

def isLeapYear(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

def numDaysInYear(year):
  return 365 + isLeapYear(year)

def numDaysInMonth(year, month):
  if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    number = 31
  elif month == 2:
    number = 28 + isLeapYear(year)
  elif month == 4 or month == 6 or month == 9 or month == 11:
    number = 30
  else:
    number = 0
  return number

def computeOffset(year, month):
  sumOfDays = 0
  currentYear = 1753
  currentMonth = 1
  for x in range(1753, year):
    sumOfDays += numDaysInYear(x + 1753)
    currentYear += 1
  for y in range(1, month):
    tempNum = numDaysInMonth(year, y)
    sumOfDays += tempNum
    currentMonth += 1
  return (sumOfDays % 7)

def displayHeader(year, month):
  print("\n")
  if month == 1:
    print(f"January, {year}\n")
  elif month == 2:
    print(f"Febrary, {year}\n")
  elif month == 3:
    print(f"March, {year}\n")
  elif month == 4:
    print(f"April, {year}\n")
  elif month == 5:
    print(f"May, {year}\n")
  elif month == 6:
    print(f"June, {year}\n")
  elif month == 7:
    print(f"July, {year}\n")
  elif month == 8:
    print(f"August, {year}\n")
  elif month == 9:
    print(f"September, {year}\n")
  elif month == 10:
    print(f"October, {year}\n")
  elif month == 11:
    print(f"November, {year}\n")
  elif month == 12:
    print(f"December, {year}\n")
  pass

def displayTable(numDays, offset):
  print("  Su  Mo  Tu  We  Th  Fr  Sa")

  if isLeapYear(year):
    offset -= 1
  for i in range(0, (offset)):
    print("   ", end=' ')

  for j in range(0, numDays):
    newLine = j + offset
    if newLine % 7 == 0:
      print("\n", end = ' ')

    if j + 1 < 10:  
      print(f"  {j + 1}", end=' ')
    else:
      print(f" {j + 1}", end=" ")
  
  return 0

def display(year, month, offset):
  numDays = numDaysInMonth(year, month)
  displayHeader(year, month)
  displayTable(numDays, offset)
  pass

month = getMonth()
year = getYear()
offset = computeOffset(year, month)
display(year, month, offset)
print("\n")