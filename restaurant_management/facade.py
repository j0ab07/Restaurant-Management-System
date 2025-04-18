from reservations.models import Reservation
from orders.models import Order
from staff_scheduling.models import TimeOffRequest

class RestaurantFacade:
    @staticmethod
    def submit_reservation(customer_name, table_number, date_time, number_of_guests):
        return Reservation.objects.create(
            customer_name=customer_name,
            table_number=table_number,
            date_time=date_time,
            number_of_guests=number_of_guests,
            status='Confirmed'
        )

    @staticmethod
    def place_order(table_number, items_ordered, quantity, special_requests):
        order = Order.objects.create(
            table_number=table_number,
            quantity=quantity,
            special_requests=special_requests,
            status='Received'
        )
        order.items_ordered.set(items_ordered)
        return order

class SchedulingFacade:
    @staticmethod
    def request_time_off(staff_id, start_date, end_date, reason):
        return TimeOffRequest.objects.create(
            staff_id=staff_id,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status='Pending'
        )