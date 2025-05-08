from fastapi import FastAPI
from sqladmin import Admin
from admin_panel.news import NewsAdmin
from admin_panel.students import StudentAdmin
from database_connect import engine

app = FastAPI(docs_url='/')


admin = Admin(app, engine=engine)

admin.add_model_view(NewsAdmin)
admin.add_model_view(StudentAdmin)



