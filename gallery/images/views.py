from django.shortcuts import render

from django.core.paginator import Paginator
from django.conf import settings
import json


# Create your views here.
def gallery(request):
    json_data = open('data.json').read()
    json_object = json.loads(json_data)

    image_gallery = json_object['photos']['photo']
    gallery_dic = []

    def get_gallery_dic(imagedata):
        for imageobject in imagedata:
            gallery_dic.append(imageobject)

    get_gallery_dic(image_gallery)

    paginator = Paginator(gallery_dic, 10)  # show 10 images per page
    page = request.GET.get('page')
    gallery_list = paginator.get_page(page)

    return render(
        request,
        'base.html',
        {'image_gallery': image_gallery,
         'gallery_list': gallery_list,
         },
    )
