# Private variables
class car:
    __color = 'Black' # Private variable
    def __start(self): #Private method
        print("car is started..........")
    def stop(self):
        print("Car is stopped..........")
cr=car()
cr.stop() # only stop is available from car class because it the only one which is not private