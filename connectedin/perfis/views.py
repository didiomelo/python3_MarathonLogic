from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from perfis.models import Perfil, Convite

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required
def index(request):
	print(request.user.username) #novo
	print(request.user.email) #novo
	print(request.user.has_perm('perfis.add_convite')) #novo
	return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request) })

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

#@permission_required('perfis.add_convite', raise_exception=True)
#@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfis.html', {'perfis' : perfil, 'perfil_logado' : get_perfil_logado(request), 'ja_eh_contato' : ja_eh_contato })

@login_required
def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
    # realizando redirecionamento
	return redirect('index')

@login_required
def get_perfil_logado(request):
	return request.user.Perfil