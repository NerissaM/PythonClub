from django.shortcuts import render, get_object_or_404
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

def meetingdetail (request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render(request, 'ClubApp/meetingdetail.html', context=context)