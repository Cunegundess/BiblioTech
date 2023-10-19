from django.apps import apps
from django.db.models import Q

def pesquisar(consulta):
    resultados = []
    modelos = apps.get_app_config('API').get_models()
    
    for modelo in modelos:
        campos = [campo.name for campo in modelo._meta.fields if campo.get_internal_type() == 'CharField']
        q_objects = Q()

        for campo in campos:
            q_objects |= Q(**{campo + '__icontains': consulta})

        resultados.extend(list(modelo.objects.filter(q_objects)))

    return resultados