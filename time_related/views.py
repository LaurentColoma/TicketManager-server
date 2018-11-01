from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
# Create your views here.
from django.views.generic import View

from .models import TimeRelatedObject


def schedule(request):
    return render(request, 'index.html')


class ManageSchedule(View):

    def get(self, request):
        my_data = [
            {
                'id': o.id,
                'text': o.label,
                'start_date': o.start.strftime('%Y-%m-%d %H:%M'),
                'end_date': o.end.strftime('%Y-%m-%d %H:%M')
            } for o in TimeRelatedObject.objects.all()
        ]
        return JsonResponse(my_data, safe=False)

    def post(self, request):
        object_id = request.POST.get('id')
        import pdb; pdb.set_trace()
        new_object = TimeRelatedObject.objects.create(
            start=request.POST.get('start', '%Y-%m-%d %H:%M'),
            end=request.POST.get('end', '%Y-%m-%d %H:%M'),
            label=request.POST.get('text', ''),
        )

        return JsonResponse({'status': 'event created', 'old_id': object_id, 'new_id': new_object.id} ) # return old id and new id

    def put(self, request):
        object_id = request.POST.get('id')
        object_to_update = TimeRelatedObject.objects.get(id=object_id)
        object_to_update.start = request.PUT.get('start', '%Y-%m-%d %H:%M')
        object_to_update.end = request.PUT.get('end', '%Y-%m-%d %H:%M')
        object_to_update.label = request.PUT.get('text', '')
        object_to_update.save()
        return JsonResponse({'status': 'event updated'}) # return old id and new id


# def delete_object(request):
#     print("in delete")
#     import pdb; pdb.set_trace()
#     object_id = request.POST.get('id')
#     TimeRelatedObject.objects.get(id=object_id).delete()
#     return JsonResponse({'status': 'event deleted'})


# def put(request):
#     import pdb; pdb.set_trace()
#     new_object = TimeRelatedObject.objects.get(PK=event_id)
#     new_object.start = request.PUT.get('start', '%Y-%m-%d %H:%M')
#     new_object.end = request.PUT.get('end', '%Y-%m-%d %H:%M')
#     new_object.label = request.PUT.get('text', '')
#     new_object.update()
#     #import pdb; pdb.set_trace()

    # class ZipCodeListJson(View):
    #     """ZipCode's JSON view"""
    #     def get(self, request, *args, **kwargs): # pylint: disable=unused-argument
    #         """Send back a select2 query filtered ZipCode list"""
    #         queryset = ZipCode.objects
    #         query = self.request.GET.get("q")
    #         city = self.request.GET.get("city")
    #         if city:
    #             queryset = queryset.filter(city_set__in=City.objects.filter(name=City.objects.filter(id=city).first().name))
    #         if query:
    #             for chunk in query.split():
    #                 queryset = queryset.filter(name__startswith=chunk)
    #         else:
    #             queryset = queryset.all()
    #         return JsonResponse([{"id": o.pk, "text": o.name}
    #         for o in queryset], safe=False)
    #
    #
    # class CityListJson(View):
    #     """City's JSON view"""
    #     def get(self, request, *args, **kwargs): # pylint: disable=unused-argument
    #         """Send back a select2 query filtered City list"""
    #         queryset = City.objects
    #         query = self.request.GET.get("q")
    #         zip_code = self.request.GET.get("zip_code")
    #         if zip_code:
    #             if isinstance(zip_code, str):
    #                 queryset = queryset.filter(zip_code__name=zip_code)
    #             else:
    #                 queryset = queryset.filter(zip_code=zip_code)
    #         if query:
    #             for chunk in query.split():
    #                 queryset = queryset.filter(name__icontains=chunk)
    #         else:
    #             queryset = queryset.all()
    #         return JsonResponse([{"id": o.pk, "text": o.name}
    #         for o in queryset], safe=False)
