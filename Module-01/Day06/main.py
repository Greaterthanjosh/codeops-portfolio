# day06/main.py

# 1. SRP Violation - Split Report class into 3 focused classes

class ReportBuilder:
    def build(self):
        return "Report content created"


class ReportSaver:
    def save(self, report):
        print(f"Saving report: {report}")


class ReportEmailer:
    def email(self, report):
        print(f"Emailing report: {report}")


print("\n1. SRP Example")

report = ReportBuilder().build()

ReportSaver().save(report)
ReportEmailer().email(report)



# 2. OCP Refactoring - Shape Area Calculation

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def print_area(shape):
    print(shape.area())


print("\n2. OCP Example")

print_area(Circle(5))
print_area(Square(4))
print_area(Triangle(3, 6))



# 3. Singleton Pattern - AppSettings

class AppSettings:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppSettings, cls).__new__(cls)
            cls._instance.currency = "ETB"

        return cls._instance


print("\n3. Singleton Example")

settings1 = AppSettings()
settings2 = AppSettings()

print(settings1.currency)

print(settings1 is settings2)



# 4. Factory Pattern - ShapeFactory

class ShapeFactory:

    @staticmethod
    def create(kind):

        if kind == "circle":
            return Circle(10)

        elif kind == "square":
            return Square(5)

        elif kind == "triangle":
            return Triangle(4, 8)

        else:
            raise ValueError("Unknown shape")


print("\n4. Factory Example")

shape = ShapeFactory.create("circle")

print(shape.area())



# 5. Observer Pattern - NewsAgency

class NewsAgency:

    def __init__(self):
        self.subscribers = []


    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)


    def notify(self, news):

        for subscriber in self.subscribers:
            subscriber.update(news)



class EmailSubscriber:

    def update(self, news):
        print(f"Email subscriber received: {news}")



class SMSSubscriber:

    def update(self, news):
        print(f"SMS subscriber received: {news}")



print("\n5. Observer Example")


agency = NewsAgency()

email_user = EmailSubscriber()
sms_user = SMSSubscriber()


agency.subscribe(email_user)
agency.subscribe(sms_user)


agency.notify("New health AI platform launched!")