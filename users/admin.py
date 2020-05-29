from django.contrib import admin
from .models import Users, Address, AddressUsers, Orders

admin.site.register(Users)
admin.site.register(Address)
admin.site.register(AddressUsers)
admin.site.register(Orders)
