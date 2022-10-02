from typing import Any
from datetime import datetime
from dataclasses import dataclass


@dataclass
class CachedDataClass:
    time: datetime
    data: Any
