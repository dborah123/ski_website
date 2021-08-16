from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def logout_view(request):
    '''
    handles logout
    '''
    logout(request)
    return redirect('login')


def login_view(request):
    '''
    handles login authentication
    '''
    error_message = None
    form = AuthenticationForm()

    if(request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)

        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if(user is not None):
                login(request, user)
                
                if(request.GET.get('next')):
                    return redirect(request.GET.get('next'))
                else:
                    # Brings user to homepage
                    return redirect('profiles:home')
        else:
            error_message = "Oops... something wen wrong"

    context = {
        'form':form,
        'error_message': error_message,
    }

    return render(request, 'auth/login.html', context)
