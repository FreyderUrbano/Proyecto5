import profile
from django.contrib import admin
from .models import Profile, Case, Metodologia, Encuesta

# admin.site.register(Profile)

#self.user, self.name, self.nitempresa, self.ransomware, self.rams, self.detail, self.imagen, self.exte, self.email, self.wallet, self.timestamp

# admin.site.register(Case)


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'nitempresa',
                    'rams', 'detail', 'imagen', 'email', 'wallet', 'timestamp',)
    search_fields = ('name', 'nitempresa', 'rams', 'detail',
                     'email', 'wallet',)
    list_display_links = ('name', 'nitempresa',
                           'detail', 'email', 'wallet',)
    list_filter = ('timestamp', 'name', 'rams',)
    list_per_page = 10
    exclude = ('timestamp',)


@admin.register(Metodologia)
class MetodologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'case', 'name',)

@admin.register(Encuesta)
class MetodologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'question1', 'question2',)