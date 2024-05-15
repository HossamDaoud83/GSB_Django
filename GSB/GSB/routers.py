class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'students':
            return 'students_db'
        elif model._meta.app_label == 'professors':
            return 'professors_db'
        elif model._meta.app_label == 'home':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'students':
            return db == 'students_db'
        elif app_label == 'professors':
            return db == 'professors_db'
        elif app_label == 'home':
            return db == 'default'
        return None
