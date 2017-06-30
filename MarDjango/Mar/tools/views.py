from django.shortcuts import render
from django.http import HttpResponse
import requests, json

# 引入我们创建的表单类
from .forms import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            loginUrl = 'http://test.sis.1course.cn/api/MemberShip/Login'
            loginData = {"Name": "mar01", "Password": "aaaaaa"}

            session = requests.session()
            session.post(loginUrl, loginData)
            noticeUrl = form.cleaned_data['a']
            noticeData = form.cleaned_data['b']

            noticeData = eval(noticeData)

            content = session.post(noticeUrl, json = noticeData)

            return HttpResponse(content.text)

    else:  # 当正常访问时
        form = AddForm()

    return render(request, 'index.html', {'form': form})
