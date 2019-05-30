from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event
from .views import index, getMeeting, getResource
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class MeetingTest(TestCase):
   def test_string(self):
       type=Meeting(titleid="Meeting")
       self.assertEqual(str(type), type.titleid)

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MeetingMinuteTest(TestCase):
   def test_string(self):
       type=MeetingMinute(durationid="1")
       self.assertEqual(str(type), type.durationid)

   def test_table(self):
       self.assertEqual(str(MeetingMinute._meta.db_table), 'MeetingMinute')

class ResourceTest(TestCase):
   def test_string(self):
       self.type=Resource(resourceid="4")
       self.assertEqual(str(type), type.resourceid)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

class GetResourceTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        resourcename='resource1', 
        clubtype=self.type, 
        user=self.u, 
        resourcePrice=100.00, 
        recourceEntryDate='2019-04-02', 
        resourceDescription='referance material on spaghetti monster',

    def test_resource_detail_success(self):
        response=self.client.get(reverse('resourcedetail', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 100.00)