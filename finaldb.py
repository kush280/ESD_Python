import time
import psutil
import GPUtil
import influxdb_client


def log_system_usage():
    client = influxdb_client.InfluxDBClient(url="http://localhost:8086",
                                            token="pKIqmJs3a-lTctA04-1oyH3nNuFm_KxQLbSLnXDjGd11U5GEjEKX4oFKzSN2OGtPNRqRm5nK-QBy4Jb27UndeQ==",
                                            org="ESD_B2",
                                            bucket="Browser")
    point = influxdb_client.Point('Utilization')
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    upload_usage = psutil.net_io_counters().bytes_sent
    download_usage = psutil.net_io_counters().bytes_recv
    disk_usage = psutil.disk_usage('/').percent
    gpu_usage = GPUtil.getGPUs()[0].memoryUtil
    gpu_temperature = GPUtil.getGPUs()[0].temperature
    point.tag("hostname", "localhost")
    point.field("CPU_usage", cpu_usage)
    point.field("RAM_usage", mem_usage)
    point.field("upload_speed", upload_usage)
    point.field("download_speed", download_usage)
    point.field("disk_usage", disk_usage)
    point.field("GPU_usage", gpu_usage)
    point.field("GPU_temperature", gpu_temperature)

    client.write_api().write(bucket="Browser", record=point)


if __name__ == '__main__':
    while True:
        log_system_usage()
        time.sleep(1)
