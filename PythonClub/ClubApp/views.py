from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'ClubApp/index.html')

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'ClubApp/resources.html', {'resource_list' : resource_list})
    
def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'ClubApp/meeting.html', {'meeting_list' : meeting_list})
