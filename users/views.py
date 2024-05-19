from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
        
        else:
    form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')