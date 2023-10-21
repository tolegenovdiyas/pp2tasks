#1
'''
from datetime import datetime, timedelta
current_date = datetime.now()
fivedaysago = current_date - timedelta(days=5)
formatted_date = fivedaysago.strftime('%Y-%m-%d')
print(formatted_date)
'''
#2
'''
from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
formatted_date_yesterday = yesterday.strftime('%Y-%m-%d')
formatted_date_today = current_date.strftime('%Y-%m-%d')
formatted_date_tomorrow = tomorrow.strftime('%Y-%m-%d')
print('Today is: ', formatted_date_today)
print('Yesterday date is: ' , formatted_date_yesterday)
print('Tommorow date is: ', formatted_date_tomorrow)
'''
#3
'''
from datetime import datetime
current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)
print(without_microseconds)
'''
#4
'''
from datetime import datetime
input('Second date is bigger than first')
date_str1 = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
time_difference = (date2 - date1).total_seconds()
print(time_difference)
'''