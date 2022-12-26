from django.utils.deprecation import MiddlewareMixin


class AuthMD(MiddlewareMixin):
    white_list = ['/login/', ]  # 白名单
    black_list = ['/black/', ]  # 黑名单

    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse

        next_url = request.path_info
        print(request.path_info, request.get_full_path())

        if next_url in self.white_list or request.session.get("user"):
            return
        elif next_url in self.black_list:
            return HttpResponse('This is an illegal URL')
        else:
            return redirect("/login/?next={}".format(next_url))