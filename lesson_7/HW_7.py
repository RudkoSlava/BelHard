
class Phone:
    brand : str
    model : str
    issue_year : int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f'Звонит {name}')

    def get_info(self):
        info_c = (self.brand, self.model, self.issue_year)
        return info_c

    def __str__(self):
        return (
            '{\n'
            f'  Бренд : {self.brand}, \n'
            f'  Модель : {self.model}, \n'
            f'  Год выпуска : {self.issue_year} \n'
            '}'
        )

telephon1 = Phone(brand='Apple', model='16 Pro', issue_year=2024)
telephon1.receive_call("Slava")
print(Phone.get_info(telephon1))
print(telephon1)
