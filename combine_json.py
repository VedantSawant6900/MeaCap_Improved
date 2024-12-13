import json

with open("/Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/data/memory/cc3m/memory_captions.json", 'r') as f:
    cc3m = json.load(f)

with open("/Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/data/memory/coco/memory_captions.json", 'r') as f:
    coco = json.load(f)

with open("/Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/data/memory/flickr30k/memory_captions.json", 'r') as f:
    flick = json.load(f)

with open("/Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/data/memory/ss1m/memory_captions.json", 'r') as f:
    ss1m = json.load(f)

big_data =  cc3m+coco+flick+ss1m

with open("/data/memory/big_data/big_data.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(big_data, indent=2) + "\n")
