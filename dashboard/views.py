from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

@login_required
@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        if request.user.is_superuser:
            

           
            orders = self.get_orders()
            products = self.get_products()

            
            filtered_orders = self.filter_orders(orders)
            filtered_products = self.filter_products(products)

          
            orders_page = self.paginate_orders(request, filtered_orders)
            products_page = self.paginate_products(request, filtered_products)

            context = {
                'orders': orders_page,
                'products': products_page,
               
            }
        elif request.user.is_staff:
            

            context = {
                
            }
        else:
            
            return HttpResponse("You do not have permission to access this page.")

        return render(request, 'dashboard/dashboard.html', context)

    def get_orders(self):
        
        return []

    def get_products(self):
        
        return []

    def filter_orders(self, orders):
        
        return orders

    def filter_products(self, products):
        
        return products

    def paginate_orders(self, request, orders):
       
        paginator = Paginator(orders, per_page=10)
        page_number = request.GET.get('page')
        orders_page = paginator.get_page(page_number)
        return orders_page

    def paginate_products(self, request, products):
       
        paginator = Paginator(products, per_page=10)
        page_number = request.GET.get('page')
        products_page = paginator.get_page(page_number)
        return products_page
 
def admin_dashboard(request):
    
    return render(request, 'dashboard/admin_dashboard.html')

from django.shortcuts import render

def shipping_dashboard(request):
    
    return render(request, 'dashboard/shipping_dashboard.html')
