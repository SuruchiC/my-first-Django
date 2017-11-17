# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, 'appone/index.html')

def get_name(request):
    if request.method == 'POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'appone/form1.html', { 'form' :form})

