from django.shortcuts import render
from django.views import View
from hw2app.models import Client, Product, Order
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum


class ProductsClientView(View):
    def get(self, request, client_id):
        # Получаем клиента по его идентификатору
        client = Client.objects.get(pk=client_id)

        # Получаем все заказы клиента
        orders = Order.objects.filter(client=client)

        # Определяем текущую дату
        current_date = timezone.now()

        # Заказы клиента за последнюю неделю
        week_ago = current_date - timedelta(days=7)

        # Заказы клиента за последний месяц
        month_ago = current_date - timedelta(days=30)

        # Заказы клиента за последний год
        year_ago = current_date - timedelta(days=365)

        # Получаем уникальные продукты из всех заказов клиента за каждый период
        products_week = set()
        products_month = set()
        products_year = set()

        for order in orders:
            products = order.products.all()
            for product in products:
                if product.added_date >= week_ago:
                    products_week.add(product)
                if product.added_date >= month_ago:
                    products_month.add(product)
                if product.added_date >= year_ago:
                    products_year.add(product)

        # Создаем список кортежей с товарами, их количеством и общей суммой
        product_list_week = []
        for product in products_week:
            count = sum(order.products.filter(name=product.name, added_date__gte=week_ago).count() for order in orders)
            total_amount = sum(order.products.filter(name=product.name, added_date__gte=week_ago).aggregate(Sum('price'))['price__sum'] or 0 for order in orders)
            product_list_week.append((product, count, total_amount))

        product_list_month = []
        for product in products_month:
            count = sum(order.products.filter(name=product.name, added_date__gte=month_ago).count() for order in orders)
            total_amount = sum(order.products.filter(name=product.name, added_date__gte=month_ago).aggregate(Sum('price'))['price__sum'] or 0 for order in orders)
            product_list_month.append((product, count, total_amount))

        product_list_year = []
        for product in products_year:
            count = sum(order.products.filter(name=product.name, added_date__gte=year_ago).count() for order in orders)
            total_amount = sum(order.products.filter(name=product.name, added_date__gte=year_ago).aggregate(Sum('price'))['price__sum'] or 0 for order in orders)
            product_list_year.append((product, count, total_amount))

        # Передаем данные в шаблон и рендерим его
        return render(request, 'products_of_client.html', {
            'client': client,
            'products_week': product_list_week,
            'products_month': product_list_month,
            'products_year': product_list_year,
        })
