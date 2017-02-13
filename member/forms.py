from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from member.models import Member, TopUp

class TopUpForm(ModelForm):
    class Meta:
        model = TopUp
        fields = ('amount', 'receipt')


class UserForm(ModelForm):
    password1 = forms.CharField(max_length=40, widget = forms.PasswordInput, label = "Password")
    password2 = forms.CharField(max_length=40, widget = forms.PasswordInput, label = "Konfirmasi Password")

    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email')#kalo dikosongkan dia ngambil semua

    #fungsi untuk validasi username
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError(u"Username %s sudah digunakan" % self.cleaned_data['username'])
        return self.cleaned_data['username']

    #fungsi untuk validasi password
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Password dan konfirmasi harus sama")

        return self.cleaned_data

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('prof_pic', 'address', 'phone')
