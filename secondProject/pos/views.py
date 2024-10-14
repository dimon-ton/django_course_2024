from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from openpyxl import Workbook, load_workbook

# Create your views here.

def test_pos(req):
    return HttpResponse("<h1>test_pos</h1>")


def AllTable(req):
    try:
        all_table = Table.objects.all()
    except Table.DoesNotExist:
        all_table = None

    context = {"all_table": all_table}

    return render(req, "pos/all-tables.html", context)


def OrdersMenu(req, table_id):
    try:
        table = Table.objects.get(id=table_id)
    except Table.DoesNotExist:
        table = None

    
    all_category = Category.objects.all()
    all_menu = Menu.objects.all()

    if req.method == "POST":
        data = req.POST.copy()

        order_menu = OrderMenu.objects.create(
            table=table, status="Pending"
            )
        
        selected_menu = data.getlist("menu")
        counts = data.getlist("count")

        total_price = 0
        items_data = []

        for i, menu_id in enumerate(selected_menu):
            menu = Menu.objects.get(id=menu_id)
            count = int(counts[i])

            item_total = menu.price * count

            total_price += item_total

            OrderMenuItem.objects.create(
                order_menu=order_menu,
                menu=menu,
                count=count,
                item_total=item_total
            )

            items_data.append({
                "รายการอาหาร": menu.name,
                "จํานวน": count,
                "ราคา": item_total,
                "เวลา": order_menu.order_time
            })

        total_price = float(data.get("total_buyer_price"))
        vat = float(data.get("vat"))
        final_price_with_vat = float(data.get("final_price_with_vat"))

        order_menu.total_buyer_price = total_price
        order_menu.vat = vat
        order_menu.final_price_with_vat = final_price_with_vat

        order_menu.save()


        # save data into Excel

        wb = Workbook()
        ws = wb.active


        # insert excel header first

        header = ["รายการอาหาร", "จำนวน", "ราคา", "เวลา", "โต๊ะ", "vat"]
        ws.append(header)
        
        for row in items_data:
            row_data = list(row.values())
            row_data.extend([table.number, order_menu.vat])

            
            ws.append(row_data)


        wb.save("order.xlsx")

        context = {"order_menu": order_menu}

        return render(req, "pos/sum-order-menu.html", context)
    
    context = {"table":table, "all_category": all_category, "all_menu": all_menu}
    return render(req, "pos/order-menu.html", context)

     