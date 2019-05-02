from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'ClubApp/index.html')

def getTypes(request):
    type_list=Resource.objects.all()
    return render(request, 'ClubApp/types.html', {'type_list' : type_list})
