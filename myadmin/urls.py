#后台管理子路由文件
from django.urls import path
from myadmin.views import index,waitui
from django.urls import path


urlpatterns = [
    path('', index.index,name="myadmin_index"),

    path('waitui/<int:pIndex>', waitui.index,name="myadmin_waitui_index"),
    path('waitui/add', waitui.add,name="myadmin_waitui_add"),
    path('waitui/inset', waitui.insert,name="myadmin_waitui_insert"),
    path('waitui/delete/<int:wid>', waitui.delete,name="myadmin_waitui_delete"),
    path('waitui/edit/<int:wid>', waitui.edit,name="myadmin_waitui_edit"),
    path('waitui/update/<int:wid>', waitui.update,name="myadmin_waitui_update"),
    path('waitui/export', waitui.export,name="myadmin_waitui_export"),

    path('login', index.login, name="myadmin_login"),
    path('dologin', index.dologin, name="myadmin_dologin"),
    path('logout', index.logout, name="myadmin_logout"),
]
