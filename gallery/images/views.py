from django.shortcuts import render
from django.conf import settings
import json


# Create your views here.
def gallery(request):
    json_data = open('data.json').read()
    json_object = json.loads(json_data)

    first_image_gallery = json_object['photos']['photo'][0]
    first_image_gallery_id = json_object['photos']['photo'][0]['id']
    image_gallery = json_object['photos']['photo']
    gallery_dic = []

    def get_gallery_dic(imagedata):
        for imageobject in imagedata:
            gallery_dic.append(imageobject)

    get_gallery_dic(image_gallery)
    print('###')
    print(gallery_dic)

    return render(
        request,
        'base.html',
        {'image_gallery': image_gallery,
         'gallery_dic': gallery_dic,
         'first_image_gallery': first_image_gallery,
         'first_image_gallery_id': first_image_gallery_id,
         },
    )
