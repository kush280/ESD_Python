from influxdb import InfluxDBClient
from datetime import datetime
client = InfluxDBClient('localhost', 8086, 'admin', 'Kush2809#', 'ESD_python')
client.create_database('ESD_python')
client.get_list_database()
client.switch_database('ESD_python')
