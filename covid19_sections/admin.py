from django.contrib import admin
from .models import Fact, Myth, Prevention, Helpline, Country


admin.site.register(Fact)
admin.site.register(Myth)
admin.site.register(Prevention)
admin.site.register(Helpline)
admin.site.register(Country)
