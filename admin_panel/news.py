from sqladmin import ModelView
from models.news import News


class NewsAdmin(ModelView, model = News):
    column_list = ['id','title', 'text', 'created_at', 'student_id', 'view']
    icon = "fa-solid fa-envelope"
    name_plural = 'Yangiliklar'
    # category = 'Admin qism'
    # name = 'Yangiliklar'
    # can_delete = False