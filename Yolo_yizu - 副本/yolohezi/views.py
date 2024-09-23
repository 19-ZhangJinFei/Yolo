from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 硬编码检查用户名和密码
        if username == 'admin' and password == '123':
            # 登录成功，您可以在这里进行重定向到某个页面
            return redirect('/success/')
        else:
            # 登录失败，显示错误消息
            error_message = "用户名或密码输入错误，请重新输入"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # GET 请求，仅渲染登录表单
        return render(request, 'login.html')

#跳转到实时告警也页面
#from .models import Alarm  # 假设有一个Alarm模型用于存储告警数据
def logout(request):
    # 删除session值
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']

    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp


# Create your views here.

class Test(APIView):
    @swagger_auto_schema(operation_summary="测试项目", tags=['测试项目/测试'])
    def get(self, request):
        return
