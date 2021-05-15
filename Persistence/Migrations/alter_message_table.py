from .Migration import Migration
from playhouse.migrate import migrate, SqliteMigrator
from peewee import TextField

class AlterMessageTableMigration(Migration):

    def migrate(self):
        migrator = SqliteMigrator(self._conn)

        migrate(
            migrator.add_column("message", 'file_name', TextField(null = True))
        )


