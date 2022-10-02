from django.db import models

class Db1Router:
    databaseName = 'hope_construction_ltd'

    def db_for_read(self, model, **hints):
        # print("database_1_database_name=>", model.MetaDb.database_name) # type: ignore
        if hasattr(model, 'MetaDb'):
            if model.MetaDb.database_name is self.databaseName: # type: ignore
                return self.databaseName
        return None

    def db_for_write(self, model: models.Model, **hints):
        # print("database_1_database_name=>", model.MetaDb.database_name) # type: ignore
        if hasattr(model, 'MetaDb'):
            if model.MetaDb.database_name is self.databaseName: # type: ignore
                return self.databaseName
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
