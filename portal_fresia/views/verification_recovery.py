from django.shortcuts import render
from portal_fresia.lib.sendmail import build_token_recovery_pass

def load(request):
    state = None
    message = None
    print(request.method)
    if request.method == 'POST':
        recovery_url = request.build_absolute_uri()
        recovery_url = recovery_url.replace('verification-recovery', 'recovery')
        message, state =  build_token_recovery_pass(request.POST.get('username'), recovery_url)
        print(message)
        print(state)
    return render(request, 'verification-recovery.html', {'state': state, 'message': message})