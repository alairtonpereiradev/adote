from django.contrib import admin
# importando as tabelas para o portal admin
from .models import Raca, Tag, Cor, Pet

# cadastrar tabelas na pagina admin
admin.site.register(Raca)
admin.site.register(Tag)
admin.site.register(Cor)
admin.site.register(Pet)
