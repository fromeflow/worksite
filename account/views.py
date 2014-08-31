from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf


def login_view(request):
    ctx = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                ctx.update({'error': 'Пользователь отключён'})
        else:
            ctx.update({'error': 'Неправильный логин или пароль'})
    ctx.update(csrf(request))
    return render_to_response('account/login.html', ctx,
                              context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('/')