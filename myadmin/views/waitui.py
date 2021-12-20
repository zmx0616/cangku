from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Waitui
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import xlwt
import re


def index(request,pIndex=1):
    permisssion_list=request.session["permisssion_list"]
    current_path=request.path_info#当前访问路径
    flag=False
    for permisssion in permisssion_list:
        permisssion="^%s$"%permisssion
        ret=re.match(permisssion,current_path)
        if ret:
            flag=True
            wmod = Waitui.objects
            wlist = wmod.all()
            context = {"waituilist": wlist}
            # 获取并判断搜索条件
            kw = request.GET.get("keyword", None)
            mywhere = []
            if kw:
                wlist = wlist.filter(Q(ridername__contains=kw) | Q(username__contains=kw))
                mywhere.append('keyword=' + kw)
            # 获取、判断并封装状态status搜索条件
            status = request.GET.get('status', '')
            if status != '':
                wlist = wlist.filter(status=status)
                mywhere.append("status=" + status)

            # 执行分页处理
            pIndex = int(pIndex)
            page = Paginator(wlist, 5)  # 以每页5条数据分页
            maxpages = page.num_pages  # 获取最大页数
            # 判断当前页是否越界
            if pIndex > maxpages:
                pIndex = maxpages
            if pIndex < 1:
                pIndex = 1
            list2 = page.page(pIndex)  # 获取当前页数据
            plist = page.page_range  # 获取页码列表信息
            context = {"waituilist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}

            return render(request, "myadmin/waitui/index.html", context)
    if not flag:
        return HttpResponse("无访问权限")


def add(request):
    permisssion_list=request.session["permisssion_list"]
    current_path=request.path_info#当前访问路径

    if current_path in permisssion_list:
        return render(request,"myadmin/waitui/add.html")
    else:
        return HttpResponse("无访问权限")


def insert(request):
    '''执行信息添加'''
    try:
        ob = Waitui()
        ob.username = request.POST['username']
        ob.datetime1 = request.POST['datetime1']
        ob.ridername = request.POST['ridername']
        ob.riderphone = request.POST['riderphone']
        ob.city = request.POST['city']
        ob.company = request.POST['company']
        ob.detailes = request.POST['detailes']
        ob.onboarding = request.POST['onboarding']
        ob.onboardtime = request.POST['onboardtime']
        ob.save()
        context = {'info': "添加成功！"}
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败！"}
    return render(request, "myadmin/info.html", context)

def delete(request,wid=0):
    '''执行信息删除'''
    try:
        ob = Waitui.objects.get(id=wid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myadmin/info.html",context)

def edit(request,wid=0):
    '''加载信息编辑表单'''
    permisssion_list=request.session["permisssion_list"]
    current_path=request.path_info#当前访问路径
    flag=False
    for permisssion in permisssion_list:
        permisssion="^%s$"%permisssion
        ret=re.match(permisssion,current_path)
        if ret:
            flag=True
            try:
                ob = Waitui.objects.get(id=wid)
                context = {'chengdu':ob}
                return render(request,"myadmin/waitui/edit.html",context)
            except Exception as err:
                print(err)
                context = {'info':"没有找到要修改的信息！"}
                return render(request,"myadmin/info.html",context)
    if not flag:
        return HttpResponse("无访问权限")



def update(request,wid):
    '''执行信息编辑'''
    try:
        ob = Waitui.objects.get(id=wid)
        ob.threedays = request.POST['threedays']
        ob.sevendays = request.POST['sevendays']
        ob.sevenonjob = request.POST['sevenonjob']
        ob.fifitydays = request.POST['fifitydays']
        ob.fifityonjob = request.POST['fifityonjob']
        ob.save()
        context = {'info':"修改成功！"}
    except Exception as err:
        print(err)
        context = {'info':"修改失败！"}
    return render(request,"myadmin/info.html",context)

def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="abc.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Waitui')
    # Sheet header, first row

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # 表头内容
    columns = ['username','datetime1','ridername','riderphone','city','company','detailes','onboarding','onboardtime','threedays','threeonjob','sevendays']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # 获取数据库数据
    rows = Waitui.objects.all().values_list('username','datetime1','ridername','riderphone','city','company','detailes','onboarding','onboardtime','threedays','threeonjob','sevendays')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
