import re
import pandas as pd
import pprint

logfile = open("logfile.log", "r")

ippattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
datepattern = r"\d{1,2}\/\d{1,2}\/\d{4}"
timepattern = r"\d{2}:\d{2}:\d{2}"
requestsuccessful_pattern = r"successful:\s+(\S+)"
requestfailed_pattern = r"failed:\s+(\S+)"

ip_add_lst = []
date_lst = []
time_lst = []
successful_lst = []
failed_lst = []

for log in logfile:
    ip_add = re.search(ippattern, log)
    if ip_add:
        ip_add_lst.append(ip_add.group())
    else:
        print("error in getting IP")

    date = re.search(datepattern, log)
    if date:
        date_lst.append(date.group())
    else:
        print("error in getting Date")

    time = re.search(timepattern, log)
    if time:
        time_lst.append(time.group())
    else:
        print("error in getting Time")

    requestsuccessful = re.search(requestsuccessful_pattern, log)
    if requestsuccessful:
        successful_lst.append(requestsuccessful.group())
    else:
        print("error in getting Success data")

    requestfailed = re.search(requestfailed_pattern, log)
    if requestfailed:
        failed_lst.append(requestfailed.group())
    else:
        print("error in getting Failed data")

print(ip_add_lst)
print(date_lst)
print(time_lst)
print(successful_lst)
print(failed_lst)

df = pd.DataFrame(columns=["IP Address", "Date", "Time", "Success", "Failed"])
df["IP Address"] = ip_add_lst
df["Date"] = date_lst
df["Time"] = time_lst
df["Success"] = successful_lst
df["Failed"] = failed_lst

df.to_csv("output.csv",index=False)

pprint.pprint(df)


#total_success = sum(successful_lst)
#total_failed = sum(failed_lst)
#ip_add_lst.append("total_success")
#successful_lst.append("total_failed")'''
