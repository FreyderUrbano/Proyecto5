from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CasesForm, MetodologiaForm, EncuestaForm
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

# ********************************************************************************************
# Vista del menu principal
# ********************************************************************************************
# Paso 6 de M
# ********************************************************************************************

# GoldenEye



@login_required
def goldenEye(request):
    return render(request, 'methods/goldenEye.html')

# GandCrab


@login_required
def gandCrab(request):
    return render(request, 'methods/gandCrab.html')

# petya


@login_required
def petya(request):
    return render(request, 'methods/petya.html')

# cryptolocker


@login_required
def cryptolocker(request):
    return render(request, 'methods/cryptolocker.html')

# Jigsaw


@login_required
def jigsaw(request):
    return render(request, 'methods/jigsaw.html')

# Shade / Troldesh


@login_required
def shadeT(request):
    return render(request, 'methods/shadeT.html')

# Ryuk


@login_required
def ryuk(request):
    return render(request, 'methods/ryuk.html')

# Bad Rabbit


@login_required
def badRabbit(request):
    return render(request, 'methods/badRabbit.html')

# Wannacry


@login_required
def wanna1(request):
    return render(request, 'methods/wanna1.html')


@login_required
def encryption6(request):
    return render(request, 'encrypted/encryption6.html')


@login_required
def copy(request):
    return render(request, 'encryptedstep6/copy.html')


# ********************************************************************************************
# Paso 5 de Metodologia
# ********************************************************************************************


@login_required
def encryption5(request):
    return render(request, 'encrypted/encryption5.html')


@login_required
def scanning(request):
    return render(request, 'encryptedstep5/scanning.html')


@login_required
def recover(request):
    return render(request, 'encryptedstep5/recover.html')


# ********************************************************************************************
# Paso 4 de Metodologia
# ********************************************************************************************

@login_required
def encryption4(request):
    return render(request, 'encrypted/encryption4.html')


# ********************************************************************************************
# Paso 3 de Metodologia
# ********************************************************************************************


@login_required
def tools(request):
    return render(request, 'encryptedstep3/tools.html')


@login_required
def encryption3(request):
    return render(request, 'encrypted/encryption3.html')

# ********************************************************************************************
# Paso 3 de Metodologia
# ********************************************************************************************


@login_required
def encryption7(request):
    return render(request, 'encrypted/encryption7.html')


@login_required
def encryption8(request):
    return render(request, 'encrypted/encryption8.html')

# ********************************************************************************************
# Paso 2 de Metodologia
# ********************************************************************************************


@login_required
def encryption2(request):
    return render(request, 'encrypted/encryption2.html')

# ********************************************************************************************
# Paso 1 de Metodologia
# ********************************************************************************************


@login_required
def encryption1(request):
    return render(request, 'encrypted/encryption1.html')


@login_required
def closeCloud(request):
    return render(request, 'encryptedstep2/closeCloud.html')


@login_required
def unplug(request):
    return render(request, 'encryptedstep2/unplug.html')


@login_required
def disconnect(request):
    return render(request, 'encryptedstep2/disconnect.html')


# ********************************************************************************************
# Paso Metodologia Cifrado
# ********************************************************************************************


@login_required
def encryption(request):
    return render(request, 'encrypted/encryption.html')


@login_required
def lock(request):
    return render(request, 'lockstep/lock.html')


@login_required
def feed(request):
    return render(request, 'azul/feed.html')


# ********************************************************************************************
#   Vista del usuario extendido
# ********************************************************************************************

def profile(request):
    return render(request, 'azul/profile.html')


# ********************************************************************************************
#   Vista de el registro de casos
# ********************************************************************************************

@login_required(login_url='login')
def cases(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    form = CasesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        case = form.save(commit=False)
        case.user = current_user
        case.save()
        messages.success(request, 'Guardado con Exito')
        return redirect('feed')
    return render(request, 'azul/cases.html', {'form': form})


@login_required(login_url='login')
def encuesta(request):
    
    form = EncuestaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Guardado con Exito')
        return redirect('feed')
    return render(request, 'methods/encuesta.html', {'form': form})
#   Vista de la consulta de casos

#         # Barra de Busqueda nitempresa ransomware
#         queryset = request.GET.get("buscar")
#         if queryset:
#             cases = Case.objects.filter(
#                 Q(name__icontains=queryset) |
#                 Q(ransomware__icontains=queryset) |
#                 Q(nitempresa__icontains=queryset)
#             ).distinct()


# ********************************************************************************************
# Vista de consulta de casos
# ********************************************************************************************




@login_required(login_url='login')
def consultcases(request, username=None):
    # Consulata la Bitacora de Casos
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        cases = Case.cases.all()
    else:
        cases = current_user.cases.all()
        user = current_user
    return render(request, 'azul/consultcases.html', {'user': user, 'cases': cases})


@login_required(login_url='login')
def consultcases2(request, username=None):
    # Consulata la Bitacora de Casos
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        cases = Case.cases.all()
    else:
        cases = current_user.cases.all()
        user = current_user
    return render(request, 'azul/consultcases2.html', {'user': user, 'cases': cases})


# ********************************************************************************************
#   Vista de la Metodología
# ********************************************************************************************


@login_required(login_url='login')
def methodology(request):
    rasomware = ["Cifrado", "Bloqueo"]
    return render(request, 'azul/methodology.html', {'rasomware': rasomware})


# ********************************************************************************************
# Vista del registro de encuesta de (metadología)
# ********************************************************************************************

@login_required(login_url='login')
def regmethodo(request, id):
    cas = get_object_or_404(Case, id=id)
    if id and id != cas.id:
        case = Case.objects.get(id=id)
        cases = Case.cases.all()
    else:
        cases = Case.objects.all().filter(id=id)
        case = cas
    return render(request, '', {'case': case, 'cases': cases})


# ********************************************************************************************
# Vista del registro de encuesta de (metadología)
# ********************************************************************************************

@login_required(login_url='login')
def survey(request, id):
    cas = get_object_or_404(Case, id=id)
    form = MetodologiaForm(request.POST or None, request.FILES or None)
    if id and id != cas.id:
        case = Case.objects.get(id=id)
        cases = Case.cases.all()
    else:
        cases = Case.objects.all().filter(id=id)
        case = cas
        if form.is_valid():
            form.save()
            messages.success(request, 'Guardado con exito')
            return redirect('feed')

    return render(request, 'encryptedstep3/survey.html', {'case': case, 'cases': cases, 'form': form})


# @login_required
# def cases(request):
#     current_user = get_object_or_404(User, pk=request.user.pk)
#     form = CasesForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         case = form.save(commit=False)
#         case.user = current_user
#         case.save()
#         messages.success(request, 'Guardado con Exito')
#         return redirect('feed')
#     return render(request, 'azul/cases.html', {'form': form})


# copia
# @login_required
# def survey(request, id):
#     cas = get_object_or_404(Case, id=id)
#     if id and id != cas.id:
#         case = Case.objects.get(id=id)
#         cases = Case.cases.all()
#     else:
#         cases = Case.objects.all().filter(id=id)
#         case = cas

#     return render(request, 'encryptedstep3/survey.html', {'case': case, 'cases': cases})
