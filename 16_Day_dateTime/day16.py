from datetime import datetime, time, date
now = datetime.now()
print(now)                     
day = now.day                 
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute            
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  

formated = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formated)

today = "15 November, 2025"
today_date = datetime.strptime(today, "%d %B, %Y")
print(today_date)

today = datetime(2019, 8, 5)
new_year_date = datetime(2021, 1, 1)
time_diff = new_year_date - now
print(time_diff)

new_time = datetime(1970, 1, 1)
print(today-new_time)