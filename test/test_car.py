import unittest
from datetime import datetime

from battery.nubbin import Nubbin
from battery.spindler import Spindler
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = Nubbin(last_service_date, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = Nubbin(last_service_date, today)
        self.assertFalse(car.needs_service())



class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        car = Spindler(last_service_date, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        car = Spindler(last_service_date, today)
        self.assertFalse(car.needs_service())


class TestCapulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestSternman(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        warning_light_on = True

        car = SternmanEngine(warning_light_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False

        car = SternmanEngine(warning_light_on)
        self.assertFalse(car.needs_service())


class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class TestCarrigan(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        tire_wear = [1, 0.2, 0, 2]

        tire = Carrigan(tire_wear)
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0, 0, 0.4, 0.8]

        tire = Carrigan(tire_wear)
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        tire_wear = [1, 0.9, 0.5, 0.8]

        tire = Octoprime(tire_wear)
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tire_wear = [1, 0.5, 0.5, 0.9]

        tire = Octoprime(tire_wear)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
