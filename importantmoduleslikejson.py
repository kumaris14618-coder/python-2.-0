import datetime  #date and time
today = datetime.date.today()
print(today)

#opreating system        # all this are library
import os
current_dir = os.getcwd()
print(current_dir)

#JSON data
import json
data = {"name":"alice","age":29}
json_string = json.dumps(data)
print(json_string)




