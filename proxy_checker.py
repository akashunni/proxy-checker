import urllib2
import time
import array
import os

def check_proxies(proxy, port, user, passwd):
    global res_time
    global i
    global cnt
    formatted_proxy = user + ":" + passwd + "@" + proxy + ":"+ port +""
    proxy_support = urllib2.ProxyHandler({"http": "http://" + formatted_proxy, "https": "https://" + formatted_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    try:
        start = time.time()
        html = urllib2.urlopen("https://www.google.com").read()
        time_proxy = time.time() - start
        res_time[i] += time_proxy
        print proxy, " UP  ", " {:.4f}".format(time_proxy), " Avg: {:.4f}".format(res_time[i] / cnt[i])
        cnt[i] += 1
    except Exception:
        res_time[i] = 0
        cnt[i] = 1
        print proxy, " DOWN", " -.----", " Avg: -.----"
    return

################################################################################################################
print "Enter the no. of proxies : ",
size = input();
hosts = ["" for x in range(size)]
ports = ["" for x in range(size)]
user = ["" for x in range(size)]
passwd = ["" for x in range(size)]

print "==== Enter the Details ===="
for i in range(0,size):
    print "======= FOR PROXY",i+1,"======="
    print "Enter Proxy Host Address",i+1,": ",
    hosts[i] = raw_input();
    print "Enter Port for",hosts[i],": ",
    ports[i] = raw_input();
    print "Enter Username for",hosts[i],": ",
    user[i] = raw_input();
    print "Enter Password for",hosts[i],": ",
    passwd[i] = raw_input();

print "==== Enter the time to refresh ====>>"
sleep = input();
os.system('cls')
print "Initializing..."
n = len(hosts)

cnt = array.array('i', (1 for i in range(0, n)))
res_time = array.array('f', (0 for i in range(0, n)))

while True:
    print "=== Proxy ===  ===== Response Time =====",
    for i in range(0, n):
        check_proxies(hosts[i], ports[i], user[i], passwd[i])
    print "\nRefreshing in",sleep,"sec."
    time.sleep(sleep)
    os.system('cls')
###############################################################################################################
