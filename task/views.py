from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, ProfileForm
from .models import Profile

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def ProfileView(request):

    if request.method != 'POST':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            return redirect('result')

    context = {'form': form}
    return render(request, 'form.html', context)


def Result(request):
    return render(request, 'result.html')
