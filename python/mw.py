weekdays=["monday","tuesday","wednesday","thursay","friday"]
day= raw_input("What day is it? ")
if day.lower()== "sunday" or day.lower()=="saturday":
	print("It's the weekend!")
elif day.lower() in weekdays:
	print("Today is a weekday!")
else:
	print("This is not weekday")
