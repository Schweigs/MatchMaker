from django.http import Http404
from django.shortcuts import render
from .models import Question, Answer

from .forms import UserResponseForm


def single(request, id):
    try:
        instance = Question.objects.get(id=id)
    except:
        raise Http404
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print form.cleaned_data
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print question_instance.text, answer_instance.text

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[id]
        context = {
            "form": form,
            "instance": instance,
            # "queryset": queryset
        }
        return render(request, "questions/home.html", context)
    else:
        raise Http404


def home(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print form.cleaned_data
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print question_instance.text, answer_instance.text

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
            "form": form,
            "instance": instance,
            # "queryset": queryset
        }
        return render(request, "questions/home.html", context)
    else:
        raise Http404
