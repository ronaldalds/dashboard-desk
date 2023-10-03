from django.contrib import admin
from .models import *

# Register your models here.

class TecnicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'chat_id', 'status')
    list_filter = ('status',)
    search_fields = ['nome',]


class TipoOSAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    search_fields = ['tipo',]


class TecnicosMensagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'sla', 'cod_os', 'data_envio', 'status')
    list_filter = ('chat_id',)
    search_fields = ['chat_id',]


class TempoSLAAdmin(admin.ModelAdmin):
    list_display = ('id', 'sla')
    search_fields = ['sla',]


class SLA_OSAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_tipo_os', 'sla', 'status')
    list_filter = ('sla', 'status',)


class InformacoesOSAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_tipo_os', 'nome')
    list_filter = ('id_tipo_os',)


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_envio')
    list_filter = ('data_envio',)


admin.site.register(Tecnicos, TecnicosAdmin)
admin.site.register(TiposOS, TipoOSAdmin)
admin.site.register(TecnicosMensagem, TecnicosMensagemAdmin)
admin.site.register(TempoSLA, TempoSLAAdmin)
admin.site.register(SLA_OS, SLA_OSAdmin)
admin.site.register(InformacoesOS, InformacoesOSAdmin)
admin.site.register(Log, LogAdmin)
