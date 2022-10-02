from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from backend.settings import DATABASE_NAMES


class ContactInfoHCModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="ci_hc_id",
    )
    location = models.CharField(
        verbose_name="Location", max_length=225, db_column="ci_hc_location", blank=True, null=True,
    )
    email = models.EmailField(
        verbose_name="Email", max_length=225, db_column="ci_hc_email", blank=True, null=True,
    )
    phone = models.CharField(
        verbose_name="Phone", max_length=225, db_column="ci_hc_phone", blank=True, null=True,
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp", max_length=225, db_column="ci_hc_whatsapp", blank=True, null=True,
    )
    facebook = models.URLField(
        verbose_name="Facebook", max_length=225, db_column="ci_hc_facebook", blank=True, null=True,
    )
    twitter = models.URLField(
        verbose_name="Twitter", db_column="ci_hc_twitter", blank=True, null=True,
    )
    instagram = models.URLField(
        verbose_name="Instagram", db_column="ci_hc_instagram", blank=True, null=True,
    )
    workingHours = models.TextField(
        verbose_name="Working Hours", db_column="ci_hc_working_hours", blank=True, null=True,
    )
    mondayToFriday = models.CharField(
        verbose_name="Monday To Friday Time", max_length=225, db_column="ci_hc_monday_to_friday", blank=True, null=True,
    )
    saturday = models.CharField(
        verbose_name="Saturday", max_length=225, db_column="ci_hc_saturday", blank=True, null=True,
    )
    sundayAndHolidays = models.CharField(
        verbose_name="Sundays and Holidays", max_length=225, db_column="ci_hc_sunday_and_holidays", blank=True, null=True,
    )
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="ci_hc_created_by", null=True,
        related_name="ContactInfo_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="ci_hc_updated_by", null=True,
        related_name="ContactInfo_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="ci_hc_creation_date", null=False, auto_now=True
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="ci_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        data = self.location or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("ContactInfoHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_contact_info'
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Infos"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = (
            'id', 'location', 'email', 'phone', 'whatsapp', 'facebook',
            'twitter', 'instagram', 'mondayToFriday', 'workingHours', 'saturday',
            'sundayAndHolidays', 'createdBy', 'updatedBy', 'creationDate', 'updateDate'
        )
