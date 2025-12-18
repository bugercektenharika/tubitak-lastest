from fuzzywuzzy import fuzz
import json
import requests
from ayarlar import * # apikey, cxkey

eslesme = False

with open("domains.json", "r", encoding="utf-8") as berlin:
	veri = json.load(berlin)

with open("domains1.json", "r", encoding="utf-8") as berlinx:
        veri1 = json.load(berlinx)

with open("counter.json", "r", encoding="utf-8") as berlinxrf:
	counters = json.load(berlinxrf)

target = input("Hedef: ").strip().casefold()
api = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX_KEY}&q={target}"
apidata = requests.get(api).json()
link1 = apidata["items"][0]["link"]
domain = link1.split("/")[2] 

for key in veri.keys():
	benzerlik = fuzz.ratio(key, target)
	if benzerlik > 50:
		print(f"{key}, ana listedeki {target} ile benziyor. Sonuc: {veri[key]} ")
		eslesme = True 
		break

if not eslesme:
	for key1 in veri1.keys():
		benzerlik1 = fuzz.ratio(key1, target)
		if benzerlik1 > 40:
			print(f"yedek listedeki {key1}, {target} ile benziyor. Sonuc: {veri1[key1]}")
			counters[key1] = counters.get(key1, 0) + 1
			with open("counter.json", "w", encoding="utf-8") as berlinxrf:
				json.dump(counters, berlinxrf, indent=4)
			if counters[key1] == 5:
				veri[key1] = veri1[key1]
				with open("domains.json", "w", encoding="utf-8") as berlin:
					json.dump(veri, berlin, indent=4) 
				del counters[key1]
				with open("counter.json", "w", encoding="utf-8") as berlinxrf:
                                	json.dump(counters, berlinxrf, indent=4)
				del veri1[key1]
				with open("domains1.json", "w", encoding="utf-8") as berlinx:
					json.dump(veri1, berlinx, indent=4)
			eslesme = True
			break

if not eslesme:
	print(f"{domain}, iki listede de bulunmadigi icin internetten aratilarak bulundu.")
	veri1[target] = domain
	with open("domains1.json", "w", encoding="utf-8") as berlinxr:
		json.dump(veri1, berlinxr, indent=4)
	counters[target] = counters.get(target, 0) + 1
	with open("counter.json", "w", encoding="utf-8") as berlinxrf:
        	json.dump(counters, berlinxrf, indent=4)