from reservations.models import Reservation, Table
from orders.models import Order, Menu, Order_Items
from staff_scheduling.models import TimeOffRequest, Staff

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
            status='Received'
        )
        for item_id in item_ids:
            menu_item = Menu.objects.get(menu_item_ID=item_id)
            Order_Items.objects.create(order_ID=order, item_ID=menu_item)
        return order

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