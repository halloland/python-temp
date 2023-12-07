from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint
from django.http import JsonResponse
from .models import Project
import os
from django.conf import settings
import csv

def index(request):
    return render(request, 'index.html')
    
def my_form_handler(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_goal = request.POST.get('project_goal')
        if project_name:
            project = Project.objects.create(name=project_name, goal=project_goal)
            project_id = project.id
            numbers = request.POST.getlist('form1[number][]')
            names = request.POST.getlist('form1[text][]')
            start_date = request.POST.getlist('form1[startDate][]')
            end_date = request.POST.getlist('form1[endDate][]')
            result = request.POST.getlist('form1[result][]')
            
            combined_data = zip(numbers, names, start_date, end_date, result)
            file_name = f'file_{project_id}.csv'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)

                writer.writerow(['Основные этапы реализации проекта'])

                writer.writerow(['№', 'Наименование прокта', 'Дата начала', 'Дата окончания', 'Результат от реализации проекта'])

                for row in combined_data:
                    writer.writerow(row)
            
            print(request.POST.get('form1'));
            return JsonResponse({'status': 'success', 'message': 'Data received successfully.'});
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)