class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient}  successfully!")
        else:
            print("Yo ass broke mah'niggah!!")


class personalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        self.account_balance -= amount
        print(f"{amount} KES worth of airtime purchased successfully.")


class businessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer.")


personal = personalMpesa(2000, 768669149, 4051475)
personal.send_money(1000, 727623740)
personal.buy_airtime(150)

business = businessMpesa(2000, 727623740, 4051475)
business.receive_payment(1000)
