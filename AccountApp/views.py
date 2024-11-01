from django.views import View
from AccountApp.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class Login(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'AccountApp/index.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('AccountApp:login')
            form = LoginForm()
        return render(request, 'AccountApp/index.html', {'form': form})