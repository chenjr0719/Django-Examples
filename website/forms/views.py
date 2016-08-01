from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms.models import Message, MessageForm
from forms.form import QueryForm

# Create your views here.

def forms_home(request):
    if request.method == 'POST':
        post_form = MessageForm(request.POST)
        if post_form.is_valid():
            cd = post_form.cleaned_data
            message = 'Contact success!'
            post_form.save()
            return HttpResponseRedirect('/forms/thanks/')

    elif request.method == 'GET' and 'num' in request.GET and request.GET['num']:
        num = int(request.GET['num'])
        message_list = Message.objects.all()[:num]
        return render(request, 'forms/messages.html', locals())
        
    else:
        post_form = MessageForm(initial = {'subject' : 'initial subject'})
        get_form = QueryForm()

    return render(request, 'forms/home.html', locals())

def forms_thanks(request):
    return render(request, 'forms/thanks.html')
