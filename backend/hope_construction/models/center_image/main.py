from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hope_construction.models.files.main import FilesHCModel
from backend.settings import DATABASE_NAMES


class CenterImageHCModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="ci_hc_id")
    centerImage = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="CenterImage", db_column="ci_hc_center_image",
        null=True, related_name="Center_Image_HC_Model_centerImage"
    )
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="ci_hc_created_by", null=True,
        related_name="Center_Image_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="ci_hc_updated_by", null=True,
        related_name="Center_Image_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="ci_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="ci_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        return f"{self.id}~{self.centerImage} =>> {self.centerImage}"

    def get_absolute_url(self):
        return reverse("CenterImageHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_center_mages'
        verbose_name = "Center Image"
        verbose_name_plural = "Center Images"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = ('id', 'centerImage', 'createdBy',
                  'updatedBy', 'creationDate', 'updateDate')
