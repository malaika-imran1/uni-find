from django.shortcuts import render


def report_lost(request):
    return render(request, 'items/report_lost.html')