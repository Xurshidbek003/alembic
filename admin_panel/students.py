from sqladmin import ModelView
from models.students import Students


class StudentAdmin(ModelView, model = Students):
    column_list = ['id','name', 'age', 'email', 'address', 'image']
    icon = "fa-solid fa-graduation-cap"
    name_plural = 'Talabalar'
    column_searchable_list = ['name']
    column_sortable_list = ['id', 'name']