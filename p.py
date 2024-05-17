from datetime import datetime
import pytz

# Calling the now() function to
# get current date and time
# adding a timezone

ct = pytz.timezone("Asia/Jakarta").localize(datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


# over the above localized time
print(ct)