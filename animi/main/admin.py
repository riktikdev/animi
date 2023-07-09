from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Снятие с регистрации "Группы"
admin.site.unregister(Group)


# Смешивание информации о профиле с информацией о пользователе
class ProfileInline(admin.StackedInline):
    model = Profile


# Расширение модели пользователя
class UserAdmin(admin.ModelAdmin):
    model = User
    ''' Отображение полей имени пользователя в панели администратора '''
    fields = ["username", "is_staff"]
    inlines = [ProfileInline]


# Снятие с регистрации первоначального пользователя
admin.site.unregister(User)

# Перерегистрация пользователя и профиля
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)