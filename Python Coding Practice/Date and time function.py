# date and time functioms
import time
print(time.time())
print(time.localtime())
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
print(time.localtime().tm_mday)
print(time.localtime().tm_hour)
print(time.asctime())  # formatted time which is readable format

# calendar
import calendar
print(calendar.month(2024,1))
