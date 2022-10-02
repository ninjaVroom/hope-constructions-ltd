from django.contrib import admin
from hope_construction.models.files.main import FilesHCModel


@admin.register(FilesHCModel)
class FilesHCAdmin(admin.ModelAdmin):
    list_display = FilesHCModel.MetaDb.fields
    list_display_links = list_display
    list_filter = list_display
    search_fields = ("filename",)
    # readonly_fields = ('date',)
    list_per_page = 25

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        if obj.fileType == 3:  # type: ignore
            return 
        obj.delete()

    def get_queryset(self, request):
        return super().get_queryset(request)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, **kwargs)
