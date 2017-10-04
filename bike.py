class bike(object):
    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.miles = 0
    def displayInfo(self):
        print "Bike price is {} max speed is {} and total mile is {}".format(self.price, self.maxSpeed, self.miles)
    def ride(self):
        print "Riding~"
        #print self
        self.miles += 10
        print "Mile count: {}".format(self.miles)
    def reverse(self):
        print "Reversing..."
        if self.miles >= 5:
            self.miles -= 5
        print "Mile count: {}".format(self.miles)

bike1 = bike('100','20mph')
bike2 = bike('100','20mph')
bike3 = bike('100','20mph')


bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()