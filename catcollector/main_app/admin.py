from django.contrib import admin
from .models import Cat
from .models import Owner
from .models import Adoption
# Register your models here
admin.site.register(Cat)
admin.site.register(Owner)
admin.site.register(Adoption)
