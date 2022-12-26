import uuid

from django.db.models import Q
from django.shortcuts import render, redirect

from app01.models import *


def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        res = User.objects.filter(Q(account=user, password=pwd) | Q(phone=user, password=pwd))
        if len(res) == 1:
            # 设置session
            request.session["user"] = user
            # 获取跳到登陆页面之前的URL
            next_url = request.GET.get("next")
            # 如果有，就跳转回登陆之前的URL
            if next_url:
                return redirect(next_url)
            # 否则默认跳转到index页面
            else:
                return redirect("/index/")
        error_msg = "用户名或密码错误"
    return render(request, "login.html", {"error_msg": error_msg})


def logout(request):
    request.session.flush()
    return redirect("login.html")


def wang_guan_list(request):
    lt = User.objects.filter(role='2')
    return render(request, 'wang_guan_list.html', {"wang_guan_list": lt})


def wang_guan_edit(request, wang_guan_id):
    user = User.objects.filter(pk=wang_guan_id).first()
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        password = request.POST.get('password')
        User.objects.filter(pk=wang_guan_id).update(name=name, role=2, password=password, u_age=age, sex=sex,
                                                    phone=phone,
                                                    note=note)
        return redirect('wang_guan_list')

    return render(request, 'wang_guan_edit.html', {"user": user})


def wang_guan_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        password = request.POST.get('password')
        u_id = uuid.uuid4()

        User.objects.create(name=name, role=2, account=u_id, password=password, u_age=age, sex=sex, phone=phone,
                            note=note)
        return redirect('wang_guan_list')
    return render(request, 'wang_guan_add.html')


def wang_guan_del(request, wang_guan_id):
    User.objects.filter(pk=wang_guan_id).delete()
    return redirect('wang_guan_list')


def hui_yuan_list(request):
    lt = User.objects.filter(role='3')
    return render(request, 'hui_yuan_list.html', {"hui_yuan_list": lt})


def hui_yuan_edit(request, hui_yuan_id):
    user = User.objects.filter(pk=hui_yuan_id).first()
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        User.objects.filter(pk=hui_yuan_id).update(name=name, role=3, u_age=age, sex=sex,
                                                   phone=phone,
                                                   note=note)
        return redirect('hui_yuan_list')

    return render(request, 'hui_yuan_edit.html', {"user": user})


def hui_yuan_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        u_id = uuid.uuid4()

        User.objects.create(name=name, role=3, account=u_id, u_age=age, sex=sex, phone=phone,
                            note=note)
        return redirect('hui_yuan_list')
    return render(request, 'hui_yuan_add.html')


def hui_yuan_del(request, hui_yuan_id):
    User.objects.filter(pk=hui_yuan_id).delete()
    return redirect('hui_yuan_list')


def get_query(request, **kwargs):
    action = kwargs.get('action')
    _id = kwargs.get('_id')
    if action == 'wang_guan' or action == "hui_yuan":
        user = User.objects.filter(pk=_id).first()
    else:
        user = User.objects.filter(pk=_id).first()

    return render(request, 'user_query.html', {"user": user})
