# Change the string used above so that it uses a / character in between the %02d and %04d.
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d' % (now.month, now.day, now.year)

#  Change the string that you are printing so that you have a : character in between the %02d
# placeholders. the three things that you are printing from month, day, and year to now.hour,
# now.minute, and now.second.
from datetime import datetime
now = datetime.now()

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)