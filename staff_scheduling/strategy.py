from abc import ABC, abstractmethod

class TimeOffStrategy(ABC):
    @abstractmethod
    def process_request(self, request):
        pass

class ApproveStrategy(TimeOffStrategy):
    def process_request(self, request):
        request.status = 'Approved'
        request.save()

class DenyStrategy(TimeOffStrategy):
    def process_request(self, request):
        request.status = 'Denied'
        request.save()