monthdays=[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
weekdays=["monday","tuesday","wednesday","thursay","friday"]
day= raw_input("What day is it? ")
date= raw_input("What date is it? ")
if (day.lower()== "sunday" or day.lower()=="saturday") and int(date) in monthdays:
	print("It's the weekend and date is " + date)
elif day.lower() in weekdays:
	print("Today is a weekday and date is " + date) 
else:
	print("This is not weekday")


# "1" does not equal 1
# 1 == 1 and "1" == "1"
