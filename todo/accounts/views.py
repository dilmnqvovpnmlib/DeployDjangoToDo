from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        self.object = form.save()
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        # Signupの処理後にログインの状態にしないと、Loginページに遷移する
        if user is not None:
            login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class AccountsView(TemplateView):
    template_name = 'accounts/accounts.html'
