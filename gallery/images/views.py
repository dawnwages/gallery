from django.shortcuts import render

from django.core.paginator import Paginator
from django.conf import settings
import json


# Create your views here.
def gallery(request):
    # Get json data and loads the object for our view context
    json_data = open('data.json').read()
    json_object = json.loads(json_data)

    # Because of the structure of the data we want to go down to the photo object
    image_gallery = json_object['photos']['photo']

    # Empty dictionary to display photos
    gallery_dic = []

    # Goes through image objects and appends to empty dictionary
    def get_gallery_dic(imagedata):
        for imageobject in imagedata:
            gallery_dic.append(imageobject)

    # Executes this with our photo object
    get_gallery_dic(image_gallery)

    # gallery_list is now what  we want to use because it paginates our gallery objects
    paginator = Paginator(gallery_dic, 10)  # show 10 images per page
    page = request.GET.get('page')
    gallery_list = paginator.get_page(page)

    # filtering by description or title
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    return render(
        request,
        'base.html',
        {'image_gallery': image_gallery,
         'gallery_list': gallery_list,
         },
    )
