from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from backend.settings import DATABASE_NAMES


class AboutHCModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="a_hc_id",
    )
    text = models.TextField(
        verbose_name="Text", db_column="a_hc_text", blank=True, null=True,
    )
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="a_hc_created_by", null=True,
        related_name="About_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="a_hc_updated_by", null=True,
        related_name="About_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="a_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="a_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        data = self.text or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("AboutHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_about'
        verbose_name = "About"
        verbose_name_plural = "About Us"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = (
            'id', 'text', 'createdBy', 'updatedBy', 'creationDate', 'updateDate'
        )