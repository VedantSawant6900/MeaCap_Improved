import json
dicti={
    "images" :[],
    "annotations":[]
}
result_dict = {}
count=0
import os
os.system('rm /Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/FlickrDataset/flickr30k/test.json')
with open('/Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/FlickrDataset/flickr30k/results_20130124.token') as f:
    for line in f:
        li=line.split("#")
        caption = li[1][2:len(li[1])-1]
        image_id=li[0].split(".")[0]
        result_dict[image_id] = 1
        count=len(result_dict)
        if (count >30000):
            print(count)
            dicti['images'].append({"id":image_id})
            dicti['annotations'].append({
                "id": image_id,
                "image_id": image_id,
                "caption":caption
            })
print(len(result_dict))
with open('/Applications/Mix_N_Max/Vedant/SEM-1/Vision_and_langugage/Final_Project/MeaCap/FlickrDataset/flickr30k/test.json','w',encoding='utf-8') as _json:
    json.dump(dicti,_json,indent=2)