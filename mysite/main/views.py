from django.forms import modelformset_factory
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Email
from .forms import EmailForm


class HomeView(TemplateView):
  template_name = 'main/home.html'

  def get(self, request):
    form = EmailForm()
    return render(request, self.template_name, {'form': form})

  def post(self, request):
    form = EmailForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      form.save()
      # send alerting email
      content = "{} ({}, {})".format(form.cleaned_data['email'], form.cleaned_data['last_name'], form.cleaned_data['first_name'])
      subject = content
      message = content
      sender = 'info@marqoapp.com'

      recipients = ['info@marqoapp.com']

      send_mail(subject, message, sender, recipients)
      return HttpResponseRedirect('/received/')

      # process the data in form.cleaned_data as required
      # ...
      # redirect to a new URL:
    return render(request, self.template_name, {'form': form})


def purpose(request):
	return render(request, 'main/purpose.html')

def team(request):
	return render(request, 'main/team.html')

def contact(request):
	return render(request, 'main/contact.html')

def comingSoon(request):
	return render(request, 'main/coming-soon.html')

def test(request):
	return render(request, 'main/test.html')

def received(request):
  return render(request, 'main/received.html')
