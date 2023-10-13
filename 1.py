from influxdb import InfluxDBClient
from datetime import datetime
client = InfluxDBClient('localhost', 8086, 'Sachin Singh', '9parasf@-!', 'ESD_python')
client.create_database('ESD_python')
client.get_list_database()
client.switch_database('ESD_python')

# from influxdb import InfluxDBClient
# from datetime import datetime

# # Initialize the InfluxDB client
# client = InfluxDBClient('localhost', 8086, 'Sachin-Singh', '9parasf@-1','ESD_python')

# # Create a new database (if it doesn't exist)
# client.create_database('ESD_python')

# # Switch to the 'ESD_python' database
# client.switch_database('ESD_python')

# # Now you can interact with the 'ESD_python' database, for example, inserting data
# # ...

# # To get the list of databases (optional)
# databases = client.get_list_database()
# print('List of databases:', databases)
