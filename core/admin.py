from django.contrib import admin
from .models import (
    Ocupacao, Cidade, Pessoa, InstituicaoEnsino, AreaSaber, Curso,
    Turma, Disciplina, Matricula, AvaliacaoTipo, Avaliacao,
    Frequencia, Turnos, Ocorrencia, CursoDisciplina
)

# --- Inlines ---

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

# --- ModelAdmin Customizations ---

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline, MatriculaInline]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'ocupacao')
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

# --- Outros registros simples ---
admin.site.register(Turma)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turnos)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(Matricula)
