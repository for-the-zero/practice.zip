import requests
#import json

# for test
proxies = {'http': 'http://192.168.11.100:58300','https': 'http://192.168.11.100:58300'}

def get_url(url):
	try:
		data = requests.get(url,timeout=10,headers={'Accept': 'application/json'})
		#data = requests.get(url,timeout=10,headers={'Accept': 'application/json'},proxies=proxies)
		return data.json()
	except:
		return "error"

token = ""   # your api key
cid = "UCbKWv2x9t6u8yZoB3KcPtnw"    # Alan Becker

def get_list(token,cid):
	list =  get_url(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&part=id&channelId={cid}&maxResults=10&order=date&key={token}')
	#list = json.loads(list)   # 6
	list = list["items"]

	vids = []
	times = []
	titles = []
	for i in list:
		vids.append(i["id"]["videoId"])
		times.append(i["snippet"]["publishedAt"])
		titles.append(i["snippet"]["title"])
	return vids,times,titles


if __name__ == '__main__':
	print(get_list(token,cid))