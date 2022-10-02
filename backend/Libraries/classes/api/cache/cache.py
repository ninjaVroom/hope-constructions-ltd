

from datetime import datetime
from typing import Any
from Libraries.classes.api.cache.dataclasses.main import CachedDataClass


class CacheDatabase(object):
    items: list[CachedDataClass] = []

    def __init__(self,):
        super(CacheDatabase, self).__init__()

    def setItem(self, item: Any):
        _item = CachedDataClass(data=item, time=datetime.now())
        if _item not in self.items:
            # print({"_item": _item})
            self.items.append(_item)

        self.loop_time()

    @property
    def getItems(self):
        # print({"__self.items__": self.items})
        self.loop_time()

        return self.items

    def getItem(self, id: int):
        # print({"__self.items__": self.items})
        items = [item for item in self.items if item.data.id == id]
        if len(items) > 0:
            item = items[0]
            self._check_time(time=item.time, id=id)
            return item

    def loop_time(self):
        for item in self.items:
            self._check_time(time=item.time, id=item.data.id)

    def _check_time(self, time: datetime, id: int):
        date = datetime.now()

        difference = date - time
        if difference.seconds > 120:
            self.items = [item for item in self.items if item.data.id != id]