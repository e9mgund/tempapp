from django.test import TestCase
import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_pubished_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        new_question = Question(pub_date = time)
        return self.assertIs(new_question.was_published_recently(),False)