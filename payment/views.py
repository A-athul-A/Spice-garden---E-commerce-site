from django.shortcuts import render,redirect
from cart.models import CartItem
import uuid
from . models import Payment_details
from datetime import date
# Create your views here.


# --------- date generation ---------
today = date.today()
order_date = date.today()
if today.day < 23:
       
    new_date  = str(today.day + 5)
    odm = str(today.month)
    ody = str(today.year)
    delivery_date = ody + "-" + odm + "-" + new_date
      
else:
    if today.month == 12:
        new_year = today.year + 1
        new_date = 5
        new_month = 1
        odt = str(new_date)
        odm = str(new_month)
        ody = str(new_year)
        delivery_date = ody + "-" + odm + "-" + odt
          
    else:   
        new_date = 1
        new_month = today.month + 1
        odt = str(new_date)
        odm = str(new_month)
        ody = str(today.year)
        delivery_date = ody + "-" + odm + "-" + odt 


# --------- payment section -------------

def payment_opt(request):

    obj = CartItem.objects.all()
    totals = []
    pro_quant = {}
    for i in obj:  
        totals.append(i.total)    
              
   
    data = {"total":totals[-1],"items":pro_quant,"del_date":delivery_date}

    return render(request,'payment.html',data)




def pay_success(request):
    users = request.user
    user = users.first_name
    unique_id = str(uuid.uuid4())
    obj = CartItem.objects.all()
    totals = []
    pro_quant = {}
    for i in obj:
        totals.append(i.total)    
        pro_quant[i.product.product_name] = i.quantity 

    total = totals[-1]

    if request.method == "POST":
        add = request.POST.get('addr')
        mb = request.POST.get('mob')
        pin = request.POST.get('pn')
        meth = request.POST.get('tab')
        orders = Payment_details.objects.create(
            user=user,
            address=add,
            mobile=mb,
            Pin=pin,
            products=pro_quant,
            amount = total,
            pay_method=meth,
            order_id = unique_id,
            o_date = order_date,
            d_date = delivery_date
            )
        orders.save()    

        obj.delete()
        return render(request,'success.html',{'trans_id': unique_id})


# -------- view orders ------

def orders(request):
    users = request.user
    # valid = ""
    flag = 1
    first_name = users.first_name

    orders = Payment_details.objects.filter(user=first_name)

    # print("today type ",type(today.day))
    # li = ""
    # for i in orders:
    #         li = i.d_date
            
    

    # print("list ",li)
    
    # print("last",li[-1])
    # print("scnd",li[-2])

    # if li[-2] != "-":
    #         dd_date = int(str(li[-2]) + str(li[-1]))
    #         print("hello")
    #         print(type(li[-2]))
    # else:
    #     dd_date = int(li[-1])

    # print(" -2 --- ",(li[-2]))
    # print(" -1 --- ",(li[-1]))
    # print("ddd ",dd_date)



    # if dd_date == today.day:
    #     msg = "Delivery today"
    #     flag = 2
        
    #     print("dt ",dd_date, "td ", today.day )
    # elif dd_date > today.day:
    #      flag = 3
    #      msg = "delivered"
            
    return render(request,"orders.html",{"data":orders,"flag":flag})

  