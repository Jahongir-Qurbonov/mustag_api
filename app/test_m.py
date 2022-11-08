from app.db_models import FileModel
from app.database import db


db.create_tables([FileModel, ])

file1_name = 'test42112.mp3'

# try:
#     file1 = FileModel(filename=file1_name)
#     # file1.save()
# except Exception as e:
#     print(e)
# else:
#     print(f"Successfully: {file1}")
# finally:
#     # print('finally')
#     pass

# print(file1_name)

q = FileModel.get_or_none(m_id='48920c0b-1139-42ef-993c-bd10846ac60c')
print(q)
