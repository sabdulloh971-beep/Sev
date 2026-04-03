from django.contrib import admin

from blog.models import Home, Home1, Home2, Home3, Home4, Home5, Home6, Contact


# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['text']
    list_filter = ['nomi']
    search_fields = ['nomi','text']
    readonly_fields = []
    ordering = ('nomi','text')

    
@admin.register(Home1)
class Home1Admin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Home2)
class Home2Admin(admin.ModelAdmin):
    list_display = ['nomi']


@admin.register(Home3)
class Home3Admin(admin.ModelAdmin):
    list_display = ['nomi']

@admin.register(Home4)
class Home4Admin(admin.ModelAdmin):
    list_display = ['nomi']


@admin.register(Home5)
class Home5Admin(admin.ModelAdmin):
    list_display = ['nomi']
    prepopulated_fields = {'slug':('nomi',)}


@admin.register(Home6)
class Home6Admin(admin.ModelAdmin):
    list_display = ['nomi']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['nomi']