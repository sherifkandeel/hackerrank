from datetime import datetime
actual = raw_input()
expected = raw_input()
actualdate = datetime.strptime(actual,"%d %m %Y")
expecteddate = datetime.strptime(expected,"%d %m %Y")
difference = (actualdate - expecteddate).days
print difference
if difference <=0:
    print 0
elif difference < 30:
    print 15*difference
else:
    print 500* (difference / 30)

