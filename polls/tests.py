import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question


class QuestionMethodTest(TestCase):
  def test_was_pub_recently_with_future_question (self):
    time = timezone.now() + datetime.timedelta(days=30)
    question = Question(pub_date = time, question_text = "test")
    self.assertIs(question.was_published_recently(), False)
    


# Create your tests here.
