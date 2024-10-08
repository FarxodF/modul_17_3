from sqlalchemy.schema import CreateTable
from aapp.DZ.db import Base, engine
from aapp.models.user import User
from aapp.models.task import Task


Base.metadata.create_all(bind=engine)  # Печать SQL-запросов для создания таблиц
print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))




# from DZ_17_2.DZ.db import Base, engine
#
#
# def initialize_database():
#     Base.metadata.create_all(bind=engine)
#     print_sql_queries()
#
#
# if __name__ == "__main__":
#     initialize_database()