class fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def show(self):
        print(f"My favourite fruit is a {self.name}" f" and it costs {self.price}." f" It is usually color {self.color} when ripe.")


myobj = fruits("mango", 30, "yellow")
myobj2 = fruits("orange", 30, "orange")
myobj3 = fruits("apple", 50, "red")
myobj.show()
myobj2.show()
myobj3.show()


