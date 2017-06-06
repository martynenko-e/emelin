from django.contrib import admin
from models import Info, ServiceCategory, Service, Discount, Gallery, Article, OpeningHours
# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address")
    list_editable = ("phone", "address")


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "show_on_main")
    list_editable = ("show_on_main",)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "time", "price", "category", "gender")
    list_editable = ("name", "time", "price", "gender")
    list_filter = ('category',)


class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ("id", "weekday_from", "weekday_to", "from_hour", "from_hour")
    list_editable = ("weekday_from", "weekday_to", "from_hour", "from_hour")


admin.site.register(Info, InfoAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OpeningHours, OpeningHoursAdmin)
admin.site.register(Discount)
admin.site.register(Gallery)
admin.site.register(Article)

admin.site.site_title = "Emelin - Admin"
admin.site.site_header = "Admin - Emelin"