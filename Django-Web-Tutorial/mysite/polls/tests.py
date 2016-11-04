import datetime

from django.utils import timezone 
from django.test import TestCase

from .models import Question



class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
        Was published recently should return false if pub_date is 
        in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        '''
        Was published recently should return false if pub_date is
        older than one day
        '''
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        '''
        Was published recently should return true if pub_date is
        in the past day
        '''        
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
