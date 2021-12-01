from django.contrib import admin


from django.contrib.auth.admin import UserAdmin

from .models import Account_Info

from .forms import AcountCreationForm

class Admin(UserAdmin):

    add_form = AcountCreationForm

    model = Account_Info

    fieldsets = UserAdmin.fieldsets

    add_fieldsets = ((None,{'fields':('username', 'email_account', 'full_name', 'pass')}),)

# Register your models here.
admin.site.register(Account_Info, Admin)
