from django.shortcuts import render
from .models import (
    Pessoa, Ocupacao, InstituicaoEnsino, AreaSaber, Curso,
    Turma, Disciplina, Matricula, Avaliacao, Frequencia,
    Turnos, Cidade, Ocorrencia, CursoDisciplina, AvaliacaoTipo
)

def index(request):
    context = {
        'pessoas': Pessoa.objects.all(),
        'ocupacoes': Ocupacao.objects.all(),
        'instituicoes': InstituicaoEnsino.objects.all(),
        'areas': AreaSaber.objects.all(),
        'cursos': Curso.objects.all(),
        'turmas': Turma.objects.all(),
        'disciplinas': Disciplina.objects.all(),
        'matriculas': Matricula.objects.all(),
        'avaliacoes': Avaliacao.objects.all(),
        'frequencias': Frequencia.objects.all(),
        'turnos': Turnos.objects.all(),
        'cidades': Cidade.objects.all(),
        'ocorrencias': Ocorrencia.objects.all(),
        'cursos_disciplinas': CursoDisciplina.objects.all(),
        'tipos_avaliacao': AvaliacaoTipo.objects.all(),
    }
    return render(request, 'core/index.html', context)
