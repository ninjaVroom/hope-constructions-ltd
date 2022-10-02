from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hope_construction.models.files.main import FilesHCModel
from backend.settings import DATABASE_NAMES


class ServiceHCModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="s_hc_id",
    )
    title = models.CharField(
        verbose_name="Title", max_length=225, db_column="s_hc_title", blank=True, null=True,
    )
    text = models.TextField(
        verbose_name="Text", db_column="s_hc_text", blank=True, null=True,
    )
    image = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Image", db_column="s_hc_image", null=True,
        related_name="Service_HC_Model_image"
    )
    # image = models.PositiveIntegerField(
    #     db_column="s_hc_image", null=True, default=0)
    icon = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        db_column="s_hc_icon", null=True,
        related_name="Service_HC_Model_icon"
    )
    # icon = models.PositiveIntegerField(
    #     db_column="s_hc_icon", null=True, default=0)
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="s_hc_created_by", null=True,
        related_name="Service_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="s_hc_updated_by", null=True,
        related_name="Service_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="s_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="s_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        data = self.text or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("ServiceHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_services'
        verbose_name = "Service"
        verbose_name_plural = "Our Services"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = (
            'id', 'title', 'text', 'image', 'icon', 'createdBy', 'updatedBy', 'creationDate', 'updateDate'
        )