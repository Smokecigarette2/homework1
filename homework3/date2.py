
import datetime

today = datetime.date.today()
print(f"{today}, {today - datetime.timedelta(days=1)}, {today +datetime.timedelta(days=1) }")