import time
import datetime
# import pytz
import influxdb_client
from log_generate import get_network_usage, get_cpu_temperature, get_ram_utilization, get_storage_utilization, get_cpu_usage


def log_system_usage():
    client = influxdb_client.InfluxDBClient(url="http://localhost:8086",
                                            token="0hRgIohSUmTOMjrEe39Uq2keQ9fDKwf-NXoAKM-3SvpIYR1lg2nQ4mSyQe5Alf417J233Wds8KdffwEu5b9bOw==",
                                            org="ESD B2",
                                            bucket="PYTHON PROJECT")

    point = influxdb_client.Point("system_usage")

    point.tag("host", "localhost")
    point.field("cpu_usage", get_cpu_usage())

    point.field("network_usage", get_network_usage())
    point.field("cpu_temperature", get_cpu_temperature())
    point.field("ram_utilization", get_ram_utilization())
    point.field("storage_utilization", get_storage_utilization())

    client.write_api().write(bucket="PYTHON PROJECT", record=point)


def main():
    while True:
        log_system_usage()
        time.sleep(1)


if __name__ == '__main__':
    main()
