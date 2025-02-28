from django.shortcuts import render, redirect
from .forms import ApplicationFormForm

def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationFormForm()

    return render(request, 'application/form.html', {'form': form})

def success_view(request):
    return render(request, 'application/success.html')
