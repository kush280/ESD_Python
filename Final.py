import time
import psutil
import datetime
import GPUtil

last_upload_usage = psutil.net_io_counters().bytes_sent
last_download_usage = psutil.net_io_counters().bytes_recv
last_time = time.time()

def display_usage(cpu_usage, mem_usage, upload_usage, download_usage, disk_usage, gpu_usage, gpu_temperature, bars=50):
    global last_upload_usage, last_download_usage, last_time
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = "█" * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = "█" * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    upload_speed = (upload_usage - last_upload_usage) / (time.time() - last_time) / 1048576
    last_upload_usage = upload_usage

    download_speed = (download_usage - last_download_usage) / (time.time() - last_time) / 1048576
    last_download_usage = download_usage

    disk_percent = (disk_usage / 100.0)
    disk_bar = "█" * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))

    gpu_usage_percent = (gpu_usage / 100.0)
    gpu_usage_bar = "█" * int(gpu_usage_percent * bars) + '-' * (bars - int(gpu_usage_percent * bars))

    print(f"\rcpu usg: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"mem usg: |{mem_bar}| {mem_usage:.2f}%  ", end="")
    print(f"upld spd: {upload_speed:.2f}Mb/s  ", end="")
    print(f"dwnld spd: {download_speed:.2f}Mb/s  ", end="")
    print(f"disk usg: |{disk_bar}| {disk_usage:.2f}%  ", end="")
    print(f"gpu usg: |{gpu_usage_bar}| {gpu_usage:.2f}%  ", end="")
    print(f"gpu temp: {gpu_temperature:.2f}°C  ", end="\r")

    with open("system_usage.log", "a") as f:
        f.write(
            f"{timestamp}, {cpu_usage:.2f}%, {mem_usage:.2f}%, {upload_speed:.2f}Mb/s, "
            f"{download_speed:.2f}Mb/s, {disk_usage:.2f}%, {gpu_usage:.2f}%, {gpu_temperature:.2f}°C\n")


if __name__ == "__main":
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent
        upload_usage = psutil.net_io_counters().bytes_sent
        download_usage = psutil.net_io_counters().bytes_recv
        disk_usage = psutil.disk_usage('/').percent
        gpu_usage = GPUtil.getGPUs()[0].memoryUtil
        gpu_temperature = GPUtil.getGPUs()[0].temperature

        display_usage(cpu_usage, mem_usage, upload_usage, download_usage, disk_usage, gpu_usage, gpu_temperature, bars=12)
        last_time = time.time()
        time.sleep(1)
