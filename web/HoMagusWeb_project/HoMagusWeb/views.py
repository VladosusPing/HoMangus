# views.py
from django.shortcuts import render
from django.http import HttpResponse
import subprocess

#def index(request):
#    return render(request, 'main/index.html')

def run_script(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')  # Получаем значение из формы
        script_path = '/путь/к/твоему/скрипту.py'
        arguments = [user_input]

        result = subprocess.run(['python', script_path] + arguments, capture_output=True)
        print(result.stdout.decode('utf-8'))

        return HttpResponse("Скрипт успешно запущен с аргументом: {}".format(user_input))
    return render(request, 'HoMagusWeb/index.html')