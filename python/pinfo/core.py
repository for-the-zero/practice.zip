import subprocess
import re

def get():
	try:
		perf = {'storge':{},'battery':{},'cpu':{},'mem':{}}


		res_storge = subprocess.check_output("adb shell df /storage/emulated", shell=True).decode('utf-8')
		res_storge = re.search(r'(\d+)\s+(\d+)\s+(\d+)\s+(\d+)%', res_storge)
		#return res_storge.group(1), res_storge.group(2), res_storge.group(4)
		storge_total = round(int(res_storge.group(1)) / 1024 / 1024, 2)
		storge_used = round(int(res_storge.group(2)) / 1024 / 1024, 2)
		storge_use = int(res_storge.group(4))
		perf_storge = {'total':storge_total,'used':storge_used,'use':storge_use}
		perf['storge'] = perf_storge


		res_battery = subprocess.check_output("adb shell dumpsys battery", shell=True).decode('utf-8')
		res_battery = int(re.search(r"level: (\d+)", res_battery).group(1))
		perf['battery'] = res_battery


		res_cpu1 = subprocess.check_output("adb shell cat /proc/cpuinfo", shell=True).decode('utf-8')
		res_cpu1 = res_cpu1.count('processor')
		perf['cpu']['cores'] = res_cpu1
		res_cpu2 = subprocess.check_output("adb shell top -n 1", shell=True).decode('utf-8')
		res_cpu2 = round(float(re.search(r"(\d+)%cpu", res_cpu2).group(1)) / res_cpu1,2)
		perf['cpu']['use'] = res_cpu2


		res_mem = subprocess.check_output("adb shell cat /proc/meminfo", shell=True).decode('utf-8')
		res_mem_total = round(int(re.search(r'MemTotal:\s+(\d+)\skB', res_mem).group(1)) / 1024 / 1024 , 2)
		res_mem_available = round(int(re.search(r'MemAvailable:\s+(\d+)\skB', res_mem).group(1)) / 1024 / 1024 , 2)
		res_mem_used = res_mem_total - res_mem_available
		res_mem_use = round((res_mem_used / res_mem_total)*100,2)
		perf['mem'] = {'total':res_mem_total,'used':res_mem_used,'use':res_mem_use}




		return perf
	except Exception as e:
		raise e

if __name__ == '__main__':
	import rich
	rich.print(get())
	"""
{
    'storge': {'total': 51.42, 'used': 47.72, 'use': 93},
    'battery': 100,
    'cpu': {'cores': 8, 'use': 100.0},
    'mem': {'total': 3.69, 'used': 2.31, 'use': 62.6}
}
	"""