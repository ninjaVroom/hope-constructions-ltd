from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from backend.settings import DATABASE_NAMES


class MessageHCModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="m_hc_id",
    )
    fullName = models.CharField(
        verbose_name="Full Name", max_length=225, db_column="m_hc_fullname", blank=True, null=True,
    )
    email = models.CharField(
        verbose_name="Email Address", max_length=225, db_column="m_hc_email", blank=True, null=True,
    )
    subject = models.CharField(
        verbose_name="Subject", max_length=225, db_column="m_hc_subject", blank=True, null=True,
    )
    message = models.TextField(
        verbose_name="Message", db_column="m_hc_message", blank=True, null=True,
    )
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="m_hc_created_by", null=True,
        related_name="Message_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="m_hc_updated_by", null=True,
        related_name="Message_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="m_hc_creation_date", null=False, auto_now=True
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="m_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        data = self.subject or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("MessageHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'hc_message'
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = (
            'id', 'fullName', 'email', 'subject', 'message', 'createdBy', 'updatedBy', 'creationDate', 'updateDate'
        )
