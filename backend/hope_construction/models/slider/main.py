from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hope_construction.models.files.main import FilesHCModel
from backend.settings import DATABASE_NAMES


class SliderHCModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="s_hc_id",
    )
    title = models.CharField(
        verbose_name="Title", max_length=225, db_column="s_hc_title", blank=True, null=True,
    )
    subTitle = models.CharField(
        verbose_name="Sub Title", max_length=225, db_column="s_hc_sub_title", blank=True, null=True,
    )
    description = models.TextField(
        verbose_name="Description", db_column="s_hc_description", blank=True, null=True,
    )
    linkText = models.CharField(
        verbose_name="Link Text", max_length=50, db_column="s_hc_link_text", blank=True, null=True,
    )
    link = models.URLField(
        verbose_name="Link", db_column="s_hc_link", blank=True, null=True,
    )
    image = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        db_column="s_hc_image", null=True,
        related_name="Slider_HC_Model_image"
    )
    # image = models.PositiveIntegerField(
    #     db_column="s_hc_image", null=True, default=0)
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="s_hc_created_by", null=True,
        related_name="Slider_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="s_hc_updated_by", null=True,
        related_name="Slider_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="s_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="s_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        data = self.title or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("SliderHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_sliders'
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = (
            'id', 'title', 'subTitle', 'description', 'link', 'linkText', 'image', 'createdBy', 'updatedBy', 'creationDate', 'updateDate'
        )
