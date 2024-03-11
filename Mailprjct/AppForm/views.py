
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from AppForm.forms import StudentForm


def stdform(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'LEaRninG SoftsOftWare'
            message = 'Dear Candidate,\nWe are pleased to offer you an internship at our company in the Python Developer department at our LEaRninG SoftsOftWare.'
            recipient = form.cleaned_data.get('email')     
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient])
            return redirect('/')
    return render(request, 'home.html', {'form': form})