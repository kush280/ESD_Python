import os, sys, datetime, socket, subprocess

hostname = socket.gethostname()
time = datetime.datetime.now().strftime("%y%m%d%H%M%S")

with open("Ping_output_" + time + ".log", 'w') as outfile:
    sys.stdout = outfile
    
    with open("IP.txt", 'r') as file:
        print(hostname, ":", datetime.datetime.now(), ":", "Reading the text file")
        t2 = " ".join([x.strip() for x in file])
        t3 = t2.split()
        print(hostname, ":", datetime.datetime.now(), ":", "Conversion of string to list")
        
        for i in t3:
            try:
                res = subprocess.Popen(["ping", "-n", "1", i], stdout=subprocess.PIPE, shell=True).communicate()[0]
            except socket.error as ff:
                print(hostname, ":", datetime.datetime.now(), ":", ff)
            
            if b'unreachable' in res:
                print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is Down")
            elif b'expired' in res:
                print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is Down")
            elif b'timed out' in res:
                print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is Down")
            else:
                print(hostname, ":", datetime.datetime.now(), ":", "Client", i, "is UP")
