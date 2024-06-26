from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question , Choice
from django.urls import reverse
from django.db.models import F
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try :
        choice_selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,"polls/detail.html",{
                "question":question,
                "error_message":"You did not select a choice."
            },
        )
    else:
        choice_selected.votes = F('votes') + 1
        choice_selected.save()

        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))