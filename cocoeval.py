from pycocoevalcap.eval import COCOEvalCap
from pycocotools.coco import COCO
coco = COCO('/content/drive/MyDrive/Vision_LanguageFinal/MeaCap/Flickr30K/flickr_ground_truth.json')
cocoRes = coco.loadRes('/content/drive/MyDrive/Vision_LanguageFinal/MeaCap/outputs/CustomKarpathy.json')
cocoEval = COCOEvalCap(coco, cocoRes)
cocoEval.evaluate()
for metric, score in cocoEval.eval.items():
    print(f'{metric}: {score:.3f}')
