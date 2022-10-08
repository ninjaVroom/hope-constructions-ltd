from django.contrib import admin
from hope_construction.models.gallery.main import GalleryHCModel


@admin.register(GalleryHCModel)
class GalleryHCAdmin(admin.ModelAdmin):
    list_display = GalleryHCModel.MetaDb.fields
    list_filter = ("creationDate", "updateDate")
    list_display_links = list_display
    # readonly_fields = ('date',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()

    def get_queryset(self, request):
        return super().get_queryset(request)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, **kwargs)
