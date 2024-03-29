from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Count
from .models import Hobby

import random

def index(response):
    return HttpResponse("<h1>test</h1>")

def start(response):
    return render(response, "main/start.html", {})

def survey_view(request):
    if request.method == 'POST':
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')
        question9 = request.POST.get('question9')
        question10 = request.POST.get('question10')
        question11 = request.POST.get('question11')

        hobbies = Hobby.objects.all()

        # Calculate scores for each hobby
        scores = {}
        for hobby in hobbies:
            score = 0
            if hobby.sport.capitalize() == 'Yes' and question1 == 'Yes':
                score += 10
            elif hobby.sport.capitalize() == 'No' and question1 == 'No':
                score -= 10

            if hobby.speed.capitalize() == 'Fast' and question2 == 'Fast':
                score += 10
            elif hobby.speed.capitalize() == 'Slow' and question2 == 'Slow':
                score += 10

            if hobby.intellectual.capitalize() == 'Yes' and question3 == 'Yes':
                score += 10
            elif hobby.intellectual.capitalize() == 'No' and question3 == 'No':
                score -= 10

            if hobby.focus.capitalize() == 'Yes' and question4 == 'Yes':
                score += 10
            elif hobby.focus.capitalize() == 'No' and question4 == 'No':
                score -= 10

            if hobby.social.capitalize() == 'Alone' and question5 == 'Alone':
                score += 10
            elif hobby.social.capitalize() == 'With others' and question5 == 'Group':
                score += 10
            elif (hobby.social.capitalize() == 'Either' and question5 == 'Either') or (hobby.social.capitalize() == 'With others' and question5 == 'Either') or (hobby.social.capitalize() == 'Alone' and question5 == 'Either'):
                score += 10

            if hobby.time.capitalize() == 'A lot' and question6 == 'Alot':
                score += 10
            elif hobby.time.capitalize() == 'In between' and question6 == 'InBetween':
                score += 10
            elif hobby.time.capitalize() == 'Minimal' and question6 == 'Minimal':
                score += 10

            if hobby.creative.capitalize() == 'Yes' and question7 == 'Yes':
                score += 10
            elif hobby.creative.capitalize() == 'No' and question7 == 'No':
                score -= 10

            if hobby.art.capitalize() == 'Yes' and question8 == 'Yes':
                score += 10
            elif hobby.art.capitalize() == 'No' and question8 == 'No':
                score -= 10

            if hobby.craft.capitalize() == 'Yes' and question9 == 'Yes':
                score += 10
            elif hobby.craft.capitalize() == 'No' and question9 == 'No':
                score -= 10

            if hobby.physicalexp.capitalize() == 'Yes' and question10 == 'Yes':
                score += 10
            elif hobby.physicalexp.capitalize() == 'No' and question10 == 'No':
                score -= 10

            if hobby.cost.capitalize() == "It's free" and question11 == 'free':
                score += 100                
            elif (hobby.cost.capitalize() == "It's free" or hobby.cost.capitalize() == 'Less than $10') and question11 == 'LTT':
                score += 100
            elif  (hobby.cost.capitalize() == "It's free" or hobby.cost.capitalize() == 'Less than $10' or hobby.cost.capitalize() == '$10-$50') and question11 == 'TTF':
                score += 100
            elif (hobby.cost.capitalize() == "It's free" or hobby.cost.capitalize() == 'Less than $10' or hobby.cost.capitalize() == '$10-$50' or hobby.cost.capitalize() == '$50-$100') and question11 == 'FTH':
                score += 100
            elif (hobby.cost.capitalize() == "It's free" or hobby.cost.capitalize() == 'Less than $10' or hobby.cost.capitalize() == '$10-$50' or hobby.cost.capitalize() == '$50-$100' or hobby.cost.capitalize() == 'More than $100') and question11 == 'MTH':
                score += 100
            
            scores[hobby] = score

        # Get top 5 hobbies with highest scores
        top_hobbies = sorted(scores, key=scores.get, reverse=True)[:10]

        context = {
            'top_hobbies': top_hobbies
        }

        return render(request, 'main/survey_results.html', context)
    else:
        return render(request, 'main/survey.html')      

def results(response):
    return render(response, "main/results.html", {})