from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hope_construction.models.files.main import FilesHCModel
from backend.settings import DATABASE_NAMES


class LogoHCModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="b_hc_id")
    logoLight = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Logo Light", db_column="t_hc_logo_light",
        null=True, related_name="Logo_HC_Model_logoLight"
    )
    logoDark = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Logo Light", db_column="t_hc_logo_dark",
        null=True, related_name="Logo_HC_Model_logoDark"
    )
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="b_hc_created_by", null=True,
        related_name="Logo_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="b_hc_updated_by", null=True,
        related_name="Logo_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="b_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="b_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        return f"{self.id}~{self.logoLight} =>> {self.logoDark}"

    def get_absolute_url(self):
        return reverse("LogoHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_logos'
        verbose_name = "Logo"
        verbose_name_plural = "Logos"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = ('id', 'logoLight', 'logoDark', 'createdBy',
                  'updatedBy', 'creationDate', 'updateDate')
