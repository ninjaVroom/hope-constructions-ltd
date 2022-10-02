import hashlib
import os
from typing import Any, Dict, Tuple
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from backend.settings import DATABASE_NAMES


def renameFile(instance, oldName: str):
    # print({"oldName": oldName, "instance": instance, "instance.id": instance.id})
    # print({"instance.meetingEventId": instance.meetingEventId})
    fileId: int = instance.id
    oldFileName, ext = os.path.splitext(oldName)
    newFileName = hashlib.md5(oldFileName.encode())
    newFileName = newFileName.hexdigest()
    return f"file-manager/{fileId}/{newFileName}{ext}"


class FileType(models.IntegerChoices):
    image = 1, 'Video'
    video = 2, 'Image'
    CM = 3, 'Center Image'
class FilesHCModel(models.Model):
    id = models.AutoField(primary_key=True, db_column="f_hc_id")
    attachment = models.FileField(
        db_column="f_hc_attachment",
        default=None, upload_to=renameFile,
    )
    _attachment: str = ''

    def _get_new_attachment(self):
        return self._attachment

    def _set_new_attachment(self, value):
        self._attachment = value

    new_attachment = property(_get_new_attachment, _set_new_attachment)
    filename = models.CharField(
        'Filename', max_length=1000, db_column="f_hc_filename", blank=True, null=True)
    fileType = models.PositiveSmallIntegerField(
        blank=False, null=True, db_column="f_hc_file_type",
        choices=FileType.choices, default=FileType.image
    )
    createdBy = models.ForeignKey(
        User, verbose_name="Created By",
        on_delete=models.CASCADE,
        db_column="f_hc_created_by", null=True,
        related_name="Files_HC_Model_createdBy"
    )
    updatedBy = models.ForeignKey(
        User, verbose_name="Updated By",
        on_delete=models.CASCADE,
        db_column="f_hc_updated_by", null=True,
        related_name="Files_HC_Model_updatedBy"
    )
    creationDate = models.DateTimeField(
        verbose_name="Creation Date", db_column="f_hc_creation_date", null=False,
    )
    updateDate = models.DateTimeField(
        verbose_name="Update Date", db_column="f_hc_update_date", null=False, auto_now=True
    )

    def __str__(self):
        return f"{self.id}~{self.filename} =>> {self.attachment}"

    def get_absolute_url(self):
        return reverse("FilesHCModel_detail", kwargs={"pk": self.pk})
        
    def clean(self) -> None:
        if self.id is None:
            if self.fileType == 3:
                raise ValidationError(
                    _('%(projectId)s already exists. Please update existing image'),
                    params={'projectId': "Service Center Image"},
                )
        else: 
            if self.id == 10 and self.fileType != 3:
                raise ValidationError(
                    _('%(projectId)s can only have a file type of Center Image'),
                    params={'projectId': "Service Center Image"},
                )
        return super().clean()

    # def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]:
    #     if self.id is not None and self.id == 10 and self.fileType == 3:
    #             return tuple()
    #     return super().delete(using, keep_parents)

    class Meta:
        managed = False
        db_table = 'hc_files'
        verbose_name = "File"
        verbose_name_plural = "Files"

    class MetaDb:
        database_name = DATABASE_NAMES[0]
        fields = ('id', 'attachment', 'filename', 'fileType',
            'createdBy', 'updatedBy', 'creationDate', 'updateDate')

