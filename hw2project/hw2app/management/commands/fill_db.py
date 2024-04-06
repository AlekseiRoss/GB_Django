from abc import ABC
from django.core.management.base import BaseCommand
from hw2app.models import Client, Product, Order
from django.utils import timezone
from datetime import timedelta
import random


class Command(BaseCommand, ABC):
    def handle(self, *args, **kwargs):
        # Создаем клиента
        client = Client.objects.create(
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            address="123 Main St",
        )
        client.save()  # Явное сохранение клиента

        # Определяем текущую дату
        current_date = timezone.now()
        # Определяем даты добавления для каждого продукта
        today = current_date
        fify_d_ago = current_date - timedelta(days=50)
        twenty_d_ago = current_date - timedelta(days=20)
        two_d_ago = current_date - timedelta(days=2)
        # Список имен продуктов и дат добавления
        products_names = ['potato', 'apple', 'pineapple', 'tomato', 'banana']
        product_dates = [today, two_d_ago, fify_d_ago, twenty_d_ago]

        products = []
        # Создаем 10 продуктов
        for _ in range(10):
            product_data = {
                "name": random.choice(products_names),
                "description": "Description",
                "price": 1,
                "quantity": 1,
                "added_date": random.choice(product_dates)
            }
            product = Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity'],
                added_date=product_data['added_date']
            )
            products.append(product)

        # Создаем 3 заказа
        for _ in range(3):
            # Создаем новый заказ для клиента
            order = Order.objects.create(client=client, order_date=timezone.now(),
                                         total_amount=0)

            # Случайное количество продуктов от 3 до 5
            # Ограничиваем максимальное количество продуктов
            num_products = random.randint(2, min(5, len(products)))

            # Выбираем случайные продукты из массива products
            selected_products = random.sample(products, num_products)

            # Добавляем выбранные продукты в заказ и обновляем общую сумму заказа
            for prod in selected_products:
                order.products.add(prod)
                order.total_amount += prod.price
            order.save()  # Сохраняем заказ
