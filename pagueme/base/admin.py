from django.contrib import admin

# Register your models here.
from pagueme.base.models import Usuario


@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
