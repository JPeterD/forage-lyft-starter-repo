from datetime import datetime

from battery.battery import Battery


class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

        if service_threshold_date < self.current_date:
            return True
        else:
            return False
