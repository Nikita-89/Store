class Store():
    def __init__(self, name, adress, items):
        self.name = name
        self.adress = adress
        self.items = items

    def add_product (self, name, price):
        self.items[name] = price
        print(f"Добавлен товар {name} с ценой {price}")

    def show_product_list(self):
        if self.items:
            print("Список товаров: ")
            for name, price in self.items.items():
                print(f"{name}: {price} руб.")
        else:
            print("Список пуст")

    def remove_product(self, name):
        if name in self.items:
            self.items.pop(name)
            print(f"Товар {name} удалён из списка.")
        else:
            print(f"Товар {name} не найден.")

    def get_price(self, name, price):
        if name in self.items:
            print(f"Товар {name} стоит {price}")
        else:
            print(f"Товар не найден")

    def update_price(self, name, new_price):
        if name in self.items:
            old_price = self.items[name]
            self.items[name] = new_price
            print(f"Товар {name} с новой ценой {new_price}, старая цена была {old_price} ")
        else:
            print(f"Товара нет в списке")

st_Magazin = Store("Булочная№1", "ул.Ветеранов д.10", {})

st_Magazin.add_product ('Пирог с картошкой', 0.5)
st_Magazin.add_product('Яблочный пирог', 1.4)
st_Magazin.add_product('Вишневый пирог', 1.8)
st_Magazin.remove_product('Пирог с картошкой')
st_Magazin.show_product_list()
st_Magazin.update_price('Пирог с картошкой', 0.2)