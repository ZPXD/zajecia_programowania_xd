from datetime import datetime 
import pytz

# podejrzenie biblioteki, sprawdzamy zawartość 
#x = dir (pytz)

#for i in dir(pytz):
 #   print (i)

#for i, s in enumerate (pytz.all_timezones): 
 #   print(i,s)

teskt = [1,2,3,4]
for i in dir(teskt):
    if i[0] != " _ " : 
        print (i)


