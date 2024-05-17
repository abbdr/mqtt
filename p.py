import os
from datetime import datetime
os.environ['TZ'] = 'Europe/London'
ct = datetime.now()
print(ct)