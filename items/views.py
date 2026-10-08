from django.shortcuts import render, redirect
from .models import LostItem


def report_lost(request):

    if request.method == "POST":
        item_name = request.POST.get("item_name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        date_lost = request.POST.get("date_lost")
        location_lost = request.POST.get("location_lost")
        image = request.FILES.get("image")

        LostItem.objects.create(
            user=request.user,
            item_name=item_name,
            category=category,
            description=description,
            date_lost=date_lost,
            location_lost=location_lost,
            image=image
        )

        return redirect("lost_items")

    return render(request, "items/report_lost.html")


def lost_items_list(request):
    items = LostItem.objects.all().order_by("-created_at")

    return render(request, "items/lost_items.html", {
        "items": items
    })