from re import template
from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', LoginView.as_view(template_name='azul/login.html'), name='login'),

    path('feed/', views.feed, name='feed'),

    path('logout/', LogoutView.as_view(template_name='azul/logout.html'), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),

    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
         template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('feed/cases/', views.cases, name='cases'),

    path('feed/consultcases/', views.consultcases, name='consultcases'),

    path('feed/consultcases/<str:username>/',
         views.consultcases, name='consultcases'),

    path('feed/consultcases/methodology',
         views.methodology, name='methodology'),

    path('feed/consultcases/methodology/lock/',
         views.lock, name='lock'),

    path('feed/consultcases/methodology/encryption/',
         views.encryption, name='encryption'),

    path('feed/consultcases/methodology/encryption/encryption1/',
         views.encryption1, name='encryption1'),

    path('feed/consultcases/methodology/encryption/encryption1/disconnect/',
         views.disconnect, name='disconnect'),

    path('feed/consultcases/methodology/encryption/encryption1/unplug/',
         views.unplug, name='unplug'),

    path('feed/consultcases/methodology/encryption/encryption1/closeCloud/',
         views.closeCloud, name='closeCloud'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/',
         views.encryption2, name='encryption2'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/',
         views.encryption7, name='encryption7'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/',
         views.encryption8, name='encryption8'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/wanna1/',
         views.wanna1, name='wanna1'),

     path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/encuesta/',
         views.encuesta, name='encuesta'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/badRabbit/',
         views.badRabbit, name='badRabbit'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/ryuk/',
         views.ryuk, name='ryuk'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/shadeT/',
         views.shadeT, name='shadeT'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/jigsaw/',
         views.jigsaw, name='jigsaw'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/cryptolocker/',
         views.cryptolocker, name='cryptolocker'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/petya/',
         views.petya, name='petya'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/gandCrab/',
         views.gandCrab, name='gandCrab'),

     path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption7/encryption8/goldenEye/',
         views.goldenEye, name='goldenEye'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/',
         views.encryption3, name='encryption3'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/tools/',
         views.tools, name='tools'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/',
         views.encryption6, name='encryption6'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/consultcases2/',
         views.consultcases2, name='consultcases3'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/consultcases2/<str:username>/',
         views.consultcases2, name='consultcases3'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/consultcases2/survey',
         views.survey, name='survey'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/consultcases2/survey/<int:id>/',
         views.survey, name='survey'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/',
         views.encryption4, name='encryption4'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/scanning/',
         views.scanning, name='scanning'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/recover/',
         views.recover, name='recover'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/encryption5/',
         views.encryption5, name='encryption5'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/encryption5/copy/',
         views.copy, name='copy'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/encryption5/consultcases2/',
         views.consultcases2, name='consultcases2'),

    path('feed/consultcases/methodology/encryption/encryption1/encryption2/encryption3/encryption6/encryption4/encryption5/consultcases2/<str:username>/',
         views.consultcases2, name='consultcases2'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
