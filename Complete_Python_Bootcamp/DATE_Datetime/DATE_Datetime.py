###################################### SECTION 15 - Advanced Python Modules ############################################
########################### Datetime

##### The Datetime module in Python will help you deal with date and time in your code. The time values are represented
##### with the Time class.

#### The Time class has attributes such as: hour, minute, second and microsecond (time zones info also!)
#### Default arguments are zero

import datetime
#### Time class
t = datetime.time(5,25,1) ### Creating a time-stamp (hour, minutes, seconds, microseconds)
print(t)

### We can grab the different components of a time-stamp, consider the following:
print(t.hour)
print(t.minute)
print(t.second)

### A time instance only holds values of time and not associated dates. We can check min and max values of a Time
### instance
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution) ### Shows the resolution of the Time instance - Min time step that a Time instance can
                                ### take (1 microsecond).

print("############################################## \n")

#### Date class - Calendar day values are represented with the Date class. Instances of the Date class have attributes
#### for year, month and day.

#### Consider the following Date stamp
d = datetime.date.today()
print(d)
print(d.timetuple()) ### Gives you more info about the current day

#### We can also call the attributes of the datestamp
for i in [d.year, d.month, d.day]:
    print(i)

#### Let's also check the min and max days possibles + resolution
print(datetime.date.max)
print(datetime.date.min)
print(datetime.date.resolution)

#### We can also call the replace() method to change date attributes
d1 = datetime.date(2020,4,20)
d2 = d1.replace(month = 5)
print((d1,d2))

#### Finally some arithmetic between dates.
#### timedelta() - Gives difference in days between two dates
print(d1 - d2)
