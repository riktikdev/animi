from django.shortcuts import render


def handler400(request, exception):
    return render(request, "main/status_codes/400.html", status=400)


def handler403(request, exception):
    return render(request, "main/status_codes/403.html", status=403)


def handler404(request, exception):
    return render(request, "main/status_codes/404.html", status=404)


def handler500(request):
    return render(request, "main/status_codes/500.html", status=500)