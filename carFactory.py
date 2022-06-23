from battery.battery import Battery
from battery.spindler import Spindler
from battery.nubbin import Nubbin
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car

class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        newCar = Car(engine, battery)
        return newCar
    

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        newCar = Car(engine, battery)
        return newCar

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = Spindler(last_service_date, current_date)
        newCar = Car(engine, battery)
        return newCar
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        newCar = Car(engine, battery)
        return newCar

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        newCar = Car(engine, battery)
        return newCar