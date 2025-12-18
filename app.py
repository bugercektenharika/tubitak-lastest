from flask import Flask, request, render_template
import json
from fuzzywuzzy import fuzz
from ayarlar import *
import requests
from score import hesapla_puan

with open("domains.json", "r", encoding="utf-8") as berlin:
    veri = json.load(berlin)

with open("domains1.json", "r", encoding="utf-8") as berlinx:
    veri1 = json.load(berlinx)

with open("counter.json", "r", encoding="utf-8") as berlinxrf:
    counters = json.load(berlinxrf)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", baslik="Ana Sayfa")
    GercekSite = None

@app.route("/islem", methods=["POST"])
def doyoumean():

    target = request.form.get("trg").strip().casefold()
    api = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX_KEY}&q={target}"
    apidata = requests.get(api).json()
    link1 = apidata["items"][0]["link"]
    domain = link1.split("/")[2]

    for key in veri.keys():
        benzerlik = fuzz.ratio(key, target)
        if benzerlik > 50:
            return render_template("index.html", GercekSite=veri[key], Puan="Yüksek")

    for key1 in veri1.keys():
        benzerlik1 = fuzz.ratio(key1, target)
        if benzerlik1 > 40:
            counters[key1] = counters.get(key1, 0) + 1
            with open("counter.json", "w", encoding="utf-8") as berlinxrf:
                json.dump(counters, berlinxrf, indent=4)

                        
                    
            if counters[key1] == 5:
                score = hesapla_puan(veri1[target])
                if score >= 3:
                    veri[key1] = veri1[key1]
                    with open("domains.json", "w", encoding="utf-8") as berlin:
                        json.dump(veri, berlin, indent=4)

                    del counters[key1]
                    with open("counter.json", "w", encoding="utf-8") as berlinxrf:
                        json.dump(counters, berlinxrf, indent=4)

                    del veri1[key1]
                    with open("domains1.json", "w", encoding="utf-8") as berlinx:
                        json.dump(veri1, berlinx, indent=4)

            return render_template("index.html", GercekSite=veri1[key1], Puan="Orta")

    
        veri1[target] = domain
        score = hesapla_puan(veri1[target])


        with open("domains1.json", "w", encoding="utf-8") as berlinxr:
            json.dump(veri1, berlinxr, indent=4)

        counters[target] = counters.get(target, 0) + 1
        with open("counter.json", "w", encoding="utf-8") as berlinxrf:
            json.dump(counters, berlinxrf, indent=4)
        
        if score >= 2:
            puan = "Yüksek Puan"
        else:
            puan = "Düşük Puan"
        return render_template("index.html", GercekSite=domain, Puan=f"{puan} (Score: {score})")

if __name__ == "__main__":
    app.run(debug=True, port=5169)

