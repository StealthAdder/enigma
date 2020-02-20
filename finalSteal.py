import re
import subprocess

command1 = "netsh wlan show profile"
network = subprocess.run(command1, shell=True, capture_output=True, text=True)
net_op = network.stdout

pattern = re.compile(r'(Profile\s*:\s)(.*)')
matches = pattern.finditer(net_op)
for match in matches:
	
	net_name = match.group(2)
	command2 = 'netsh wlan show profile '+'"'+net_name+'"'+' key=clear'
	net_info = subprocess.run(command2, shell=True, capture_output=True, text=True)
	
	pattern2 = re.compile(r'(SSID name\s*:\s)(.*)')
	wlan_name = pattern2.finditer(net_info.stdout)
	pass_pattern = re.compile(r'(Key Content\s*:\s)(.*)')
	pass_match = pass_pattern.finditer(net_info.stdout)

	file=open('passdata.txt', 'a')
	for wname,passwd in zip(wlan_name, pass_match):
		#print("NETWORK NAME: "+ wname.group(2) + "\t\tPASSWORD: "+passwd.group(2))
		out="NETWORK NAME: "+ wname.group(2) + "\t\tPASSWORD: "+passwd.group(2)+ "\n"
		file.write(out)
	file.close()
			