from django.contrib import admin
from .models import Cat, Feeding,Toy
from .models import Owner
from .models import Adoption
# Register your models here
admin.site.register(Cat)
admin.site.register(Owner)
admin.site.register(Adoption)
admin.site.register(Feeding)
admin.site.register(Toy)

