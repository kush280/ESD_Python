import time
import psutil
import GPUtil
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

def log_system_usage():
    client = InfluxDBClient(url="http://localhost:8086",
                            token="pKIqmJs3a-lTctA04-1oyH3nNuFm_KxQLbSLnXDjGd11U5GEjEKX4oFKzSN2OGtPNRqRm5nK-QBy4Jb27UndeQ==",
                            org="ESD_B2",
                            bucket="Browser")
    
    point = {}
    point["measurement"] = "Utilization"
    point["tags"] = {
        "hostname": "localhost"
    }
    point["fields"] = {
        "CPU_usage": psutil.cpu_percent(),
        "RAM_usage": psutil.virtual_memory().percent,
        "upload_speed": psutil.net_io_counters().bytes_sent,
        "download_speed": psutil.net_io_counters().bytes_recv,
        "disk_usage": psutil.disk_usage('/').percent,
        "GPU_usage": GPUtil.getGPUs()[0].memoryUtil,
        "GPU_temperature": GPUtil.getGPUs()[0].temperature
    }

    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket="Browser", record=point)

if __name__ == '__main__':
    while True:
        log_system_usage()
        time.sleep(1)
