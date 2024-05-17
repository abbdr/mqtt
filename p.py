import os, pytz, time
from datetime import datetime
ct = datetime.now().astimezone(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S")
time.sleep(2)
print(ct)