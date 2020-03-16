from django.contrib import admin
from .models import Fact, Myth, Prevention


admin.site.register(Fact)
admin.site.register(Myth)
admin.site.register(Prevention)
