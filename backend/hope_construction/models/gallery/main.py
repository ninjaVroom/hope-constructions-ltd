from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hope_construction.models.files.main import FilesHCModel
from backend.settings import DATABASE_NAMES


class GalleryHCModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="g_hc_id")
    attachment = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Attachment", db_column="t_hc_attachment",
        null=True, related_name="Gallery_HC_Model_attachment"
    )
    # attachment = models.PositiveIntegerField(
    #     db_column="t_hc_attachment", null=True, default=0)
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="g_hc_created_by", null=True,
        related_name="Gallery_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="g_hc_updated_by", null=True,
        related_name="Gallery_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="g_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="g_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        return f"{self.id}~{self.attachment} =>> {self.attachment}"

    def get_absolute_url(self):
        return reverse("GalleryHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_galleries'
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = ('id', 'attachment', 'createdBy',
                  'updatedBy', 'creationDate', 'updateDate')
