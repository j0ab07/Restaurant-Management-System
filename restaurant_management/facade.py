from reservations.models import Reservation, Table
from orders.models import Order, Menu, OrderItem
from staff_scheduling.models import TimeOffRequest, Staff

# Facade for restaurant-related operations
class RestaurantFacade:
    @staticmethod
    def submit_reservation(customer_name, customer_email, table_id, date, time, number_of_guests):
        table = Table.objects.get(table_id=table_id)
        return Reservation.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            table_ID=table,
            date=date,
            time=time,
            number_of_guests=number_of_guests,
            status='Confirmed'
        )

    @staticmethod
    def place_order(table_id, staff_id, item_ids, special_requests):
        table = Table.objects.get(table_id=table_id)
        staff = Staff.objects.get(id=staff_id)
        order = Order.objects.create(
            table_ID=table,
            staff_ID=staff,
            special_requests=special_requests,
            status='pending'
        )
        for item_id in item_ids:
            menu_item = Menu.objects.get(menu_id=item_id)
            OrderItem.objects.create(order_id=order, menu_id=menu_item)
        return order

# Facade for scheduling-related operations
class SchedulingFacade:
    @staticmethod
    def request_time_off(staff_id, start_date, end_date, reason):
        staff = Staff.objects.get(id=staff_id)
        return TimeOffRequest.objects.create(
            staff=staff,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status='Pending'
        )