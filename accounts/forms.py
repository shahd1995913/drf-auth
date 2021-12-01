
from django.contrib.auth.forms import UserCreationForm

from .models import Account_Info

class AcountCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        model = Account_Info

        fields = ('username', 'email_account', 'full_name', 'pass1', 'pass2')
