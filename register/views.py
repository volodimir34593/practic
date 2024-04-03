from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import RegistrationForm

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration_widget.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request, 'registration_widget.html', {'form': form})
