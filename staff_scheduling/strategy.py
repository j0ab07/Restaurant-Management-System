from abc import ABC, abstractmethod

# Abstract base class for time-off request processing strategies
class TimeOffStrategy(ABC):
    @abstractmethod
    def process_request(self, request):
        pass

# Strategy to approve time-off requests
class ApproveStrategy(TimeOffStrategy):
    def process_request(self, request):
        request.status = 'Approved'
        request.save()

# Strategy to deny time-off requests
class DenyStrategy(TimeOffStrategy):
    def process_request(self, request):
        request.status = 'Denied'
        request.save()