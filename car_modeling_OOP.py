class Car:
    def __init__(self, capacity=20, delta=5, velocity=0):
        self.capacity = capacity
        self.delta = delta
        self.velocity = velocity

    def speedUP(self, delta):
        try:
            if(delta <= 0):
                raise Exception("No number below or equal to zero is allowed")

            if(delta > self.capacity):
                raise Exception(
                    "Maximum capacity set is " + str(self.capacity))

            if (self.velocity + delta) <= self.capacity:
                self.delta = delta
                self.velocity += self.delta
                return self.velocity
            else:
                self.velocity = self.capacity
                raise Exception(
                    "The maximum capacity you can accelerate is " + str(self.capacity))
        except Exception as error:
            print('\nCaught this error: ' + str(error))
            return self.velocity

    def brake(self, delta):
        try:
            if(delta <= 0):
                raise Exception("No number below or equal to zero is allowed")

            if(delta > self.capacity):
                raise Exception(
                    "Maximum capacity set is " + str(self.capacity))

            if (self.velocity - self.delta) > 0:
                self.delta = delta
                self.velocity -= self.delta
                return self.velocity
            else:
                self.velocity = 0
                raise Exception("You can't break less than zero")
        except Exception as error:
            print('\nCaught this error: ' + str(error))
            return self.velocity


if __name__ == '__main__':
    c1 = Car(180)

    for _ in range(25):
        # 179 -> 180
        print(c1.speedUP(12))

    for _ in range(10):
        print(c1.brake(delta=20))
