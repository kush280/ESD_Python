import datetime
import time
import pytz
import datetime
import influxdb_client

from test import get_network_usage, get_cpu_temperature, get_ram_utilization, get_storage_utilization, get_cpu_usage


def log_system_usage():
    """Logs the system usage to InfluxDB."""

    # Create an InfluxDB client
    client = influxdb_client.InfluxDBClient(url="http://localhost:8086",
                                            token="9vdSpaDNTMbkA8e7OjkSmaFwQzGjQ0vQge7B906bkbiJxTU-gL57mwv_KQ0-CMMiJw2gn1QQnQ96ZQ5tjn2AdA==",
                                            org="ESD_B2",
                                            bucket="Project")

    # Create a new point
    point = influxdb_client.Point("system_usage")

    # Add the system usage metrics to the point
    point.tag("host", "localhost")
    point.field("cpu_usage", get_cpu_usage())
    # point.field("gpu_usage", get_gpu_usage()) hello
    point.field("network_usage", get_network_usage())
    point.field("cpu_temperature", get_cpu_temperature())
    point.field("ram_utilization", get_ram_utilization())
    point.field("storage_utilization", get_storage_utilization())

    # Write the point to InfluxDB
    client.write_api().write(bucket="Project", record=point)


def main():
    """Main function."""

    while True:
        log_system_usage()
        time.sleep(1)


if __name__ == '__main__':
    main()
