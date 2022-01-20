from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess
import re


def filters(std):
    strin = std

    reg = r"\W\W\W\W"
    reg2 = r"\W"

    lst = re.findall(reg,strin)
    lst2 = re.findall(reg2,strin)

    statement = False

    if len(lst) >=1:
        for x in lst:
            strin = strin.replace(x, x[1])
        return strin

    else:
        for x in lst2:
            strin = strin.replace(x, "")
        return strin

def home(request):
    if request.GET.get('word'):
        user_inp = request.GET.get('word')
        vari = filters(user_inp)
        process = subprocess.check_output([f'echo {vari}'], shell=True).decode()
        contex = {'result': process}
        return render(request, 'core/home.html', contex)
    return render(request, 'core/home.html')
    # return HttpResponse("hello")

# def result(request):
#     user_inp = request.GET.get('urls')
#     vari = filters(user_inp)
#     process = subprocess.check_output([f'echo {vari}',], shell=True, encoding='UTF-8')
#     contex = {'result': process}
#     return render(request, 'core/res.html', contex)