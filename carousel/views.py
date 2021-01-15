# from django.shortcuts import render
# from django.template import RequestContext
#
# from carousel.models import *
#
#
# def render_to_response(param, param1, context_instance):
#     pass
#
#
# def my_view(request):
#     ## Your code here.
#     carousel = Carousel.objects.get(pk=1)
#     return render_to_response(
#         'home.html',
#         {
#             'carousel': carousel,
#         },
#         context_instance=RequestContext(request)
#     )