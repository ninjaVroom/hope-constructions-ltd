from django.contrib import admin
from django import forms
from hope_construction.models.contact_info.main import ContactInfoHCModel


class ContactInfoHCForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactInfoHCForm, self).__init__(*args, **kwargs)

        self.fields['whatsapp'].label = "Enter Whatsapp link [e.g. https://wa.me/country_code phone_number] {https://wa.me/+233101010101}"

    class Meta:
        model = ContactInfoHCModel
        fields = '__all__'

@admin.register(ContactInfoHCModel)
class ContactInfoHCAdmin(admin.ModelAdmin):
    list_display = ContactInfoHCModel.MetaDb.fields
    list_display_links = list_display
    list_filter = ("creationDate", "updateDate")
    search_fields = (
        "location", "email", "phone", "whatsapp", "facebook", "twitter", 
        "instagram", "mondayToFriday", "saturday", "sundayAndHolidays",
    )
    # readonly_fields = ('date',)
    list_per_page = 25

    form = ContactInfoHCForm

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
