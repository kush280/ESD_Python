import os
import sys
import datetime
import socket
import subprocess

hostname = socket.gethostname()
time = datetime.datetime.now().strftime("%y%m%d%H%M%S")

with open("Ping_output_" + time + ".log", 'w') as outfile:
    original_stdout = sys.stdout  # Save the original sys.stdout
    sys.stdout = outfile  # Redirect sys.stdout to the file

    with open("IP.txt", 'r') as file:
        print(hostname, ":", datetime.datetime.now(), ":", "Reading the text file")
        t2 = " ".join([x.strip() for x in file])
        t3 = t2.split()
        print(hostname, ":", datetime.datetime.now(), ":", "Conversion of string to list")

        for i in t3:
            try:
                res = subprocess.Popen(["ping", "-n", "1", i], stdout=subprocess.PIPE, shell=True)
                res.communicate()

                if "unreachable" in res.stdout.decode():
                    print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is Down")
                elif "expired" in res.stdout.decode():
                    print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is Down")
                elif "timed out" in res.stdout.decode():
                    print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is Down")
                else:
                    print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is UP")

            except subprocess.CalledProcessError as ff:
                print(hostname, ":", datetime.datetime now(), ":", ff)
            except Exception as e:
                print(hostname, ":", datetime.now(), ":", "Error:", e)

    sys.stdout = original_stdout  # Reset sys.stdout to the original value
