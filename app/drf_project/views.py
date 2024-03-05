from django.http import JsonResponse


# Create your views here.
def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)
