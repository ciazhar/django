from django.shortcuts import render, redirect
from .forms import UserForm,MemberForm
# Create your views here.
#ada 2 buah view dlm djangon yaitu class based view atau function based view
#kalo ini pake function based view

def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        memberform = MemberForm(request.POST)
        if userform.is_valid() * memberform.is_valid():
            user = userform.save(commit=False)
            user.set_password(userform.cleaned_data['password1'])
            user.save()

            member = memberform.save(commit=False)
            member.user = user
            member.save()
            return redirect('login')
    else:
        userform = UserForm()
        memberform = MemberForm()
    return render(request, 'register.html',{'userform':userform,'memberform':memberform})
