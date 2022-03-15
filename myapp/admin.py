from django.contrib import admin
from .models import Contact,User,Product,Wishlist,Cart,Transaction

# Register your models here.
#admin.site.register(Contact)
#admin.site.register(User)
#admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Transaction)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","email","usertype")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name","product_price")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email")
    
# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ("product_name",)
