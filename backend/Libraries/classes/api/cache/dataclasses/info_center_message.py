from dataclasses import dataclass
from typing import Any
from Libraries.classes.api.cache.dataclasses.main import CachedDataClass


@dataclass
class CachedInfoCenterMessageModelDataClass(CachedDataClass):
    # from db_models_plus_database_3.models.messaging.message.main import MessagingMessageModel
    data: Any # MessagingMessageModel
