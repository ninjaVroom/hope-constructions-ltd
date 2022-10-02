from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hope_construction.models.files.main import FilesHCModel
from backend.settings import DATABASE_NAMES


class TestimonialHCModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="t_hc_id",
    )
    quoteAuthorName = models.CharField(
        verbose_name="Quote Author Name", max_length=225, db_column="t_hc_quote_author_name", blank=True, null=True,
    )
    quoteAuthorImage = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Quote Author Image", db_column="t_hc_quote_author_image", null=True, blank=True,
        related_name="Testimonial_HC_Model_quoteAuthorImage"
    )
    # quoteAuthorImage = models.PositiveIntegerField(
    #     db_column="t_hc_quote_author_image", null=True, default=0)
    quoteAuthorTitle = models.CharField(
        verbose_name="Quote Author Title", max_length=225, db_column="t_hc_quote_author_title", blank=True, null=True,
    )
    quoteText = models.TextField(
        verbose_name="Quote Text", db_column="t_hc_quote_text", blank=True, null=True,
    )
    image = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Image", db_column="t_hc_image", null=True, blank=True,
        related_name="Testimonial_HC_Model_image"
    )
    # image = models.PositiveIntegerField(
    #     db_column="t_hc_image", null=True, default=0)
    video = models.OneToOneField(
        FilesHCModel, on_delete=models.CASCADE,
        verbose_name="Video", db_column="t_hc_video", null=True, blank=True,
        related_name="Testimonial_HC_Model_video"
    )
    # video = models.PositiveIntegerField(
    #     db_column="t_hc_video", null=True, default=0)
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="t_hc_created_by", null=True,
        related_name="Testimonial_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="t_hc_updated_by", null=True,
        related_name="Testimonial_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="t_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="t_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        data = self.quoteAuthorName or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("TestimonialHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_testimonial'
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = (
            'id', 'quoteAuthorName', 'quoteAuthorImage', 'quoteAuthorTitle', 'quoteText',
            'image', 'video', 'createdBy', 'updatedBy', 'creationDate', 'updateDate'
        )
