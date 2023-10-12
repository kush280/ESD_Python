import re
logfile = open("Logfile.log", "r")
ippattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
ip_add_lst = []
for log in logfile:
    st = (log)
    ip_add = re.search(ippattern, log)
    ip_add_lst.append(ip_add.group())
print(ip_add_lst)
st.find("requestsuccessful: ")