from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class MyUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()

class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)
