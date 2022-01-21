# Runner script for all modules
from datetime import date
from datetime import datetime
import house_info
from load_data import load_sensor_data

##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
# Module 2 code here:

# Module 3 code here:
house_info = house_info.HouseInfo
test_area = 1
recs = house_info.get_data_by_area
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

test_date = datetime.strptime()

print("\nHouse sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))




# Module 4 code here:

# Module 5 code here: