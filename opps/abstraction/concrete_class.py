from opps.abstraction.Abstraction import Vehicle


class Car(Vehicle):
    def start(self):
        print('car engine started')
    def stop(self):
        print('car engine stopped')
class Bus(Vehicle):
    def start(self):
        print('bus engine started')
    def stop(self):
        print('bus engine stopped')
    def on(self):
        print('bus on')
b = Bus()
b.on()