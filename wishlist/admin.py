from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin class for wishlist.
    """
    list_display = ('username',)
    search_fields = ('username',)
    list_filter = ('username',)


admin.site.register(Wishlist, WishlistAdmin)