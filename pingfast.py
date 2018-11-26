import subprocess

netscope='10.11.1.'

for i in range(200,254):
    target = netscope+str(i)
    exCode = subprocess.Popen('ping -c 1 -n -w 1 '+target).wait()
    if exCode == 0:
        print(target+' is alive')
    else:
        print(target+' is unresponsive')
