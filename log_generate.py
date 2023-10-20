import datetime
import time
# import gputil
import psutil


def get_cpu_usage():
    return psutil.cpu_percent()


# def get_gpu_usage():
#     gpu = gputil.get_gpu(0)
#     return gpu.load * 100


def get_network_usage():
    return psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv


def get_cpu_temperature():
    try:
        return psutil.sensors_temperatures()['coretemp'][0].current
    except:
        return 0


def get_gpu_temperature():
    if psutil.GPUs:
        gpu = psutil.GPUs[0]
        return gpu.temperature
    else:
        return 0


def get_ram_utilization():
    return psutil.virtual_memory().percent


def get_storage_utilization():
    return psutil.disk_usage('/').percent


def log_system_usage():
    timestamp = datetime.datetime.now()
    log_file = open('LOGFILE.log', 'a')
    log_file.write(
        '{timestamp},{cpu_usage},{network_usage},{cpu_temperature},{ram_utilization},{storage_utilization}\n'.format(
            timestamp=timestamp,
            cpu_usage=get_cpu_usage(),
            # gpu_usage=get_gpu_usage(),
            network_usage=get_network_usage(),
            cpu_temperature=get_cpu_temperature(),
            ram_utilization=get_ram_utilization(),
            storage_utilization=get_storage_utilization()
        ))
    log_file.close()


def main():
    while True:
        log_system_usage()
        time.sleep(1)


if __name__ == '__main__':
    main()
