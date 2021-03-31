from django.contrib import admin

# Register your models here.
from app01.models import Publisher,Book,Author,Goods

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Goods)