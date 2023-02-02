class Cart:
    def __init__(self):
        self.item_list = []
        self.c = 0
        self.k = 0
        self.counted = []

    def add_item(self, items):
        self.item_list.append(items)

    def remove_item(self, items):
        self.item_list.remove(items)

    def display_cart(self):
        print(self.item_list)

    def counts(self):
        for i in range(len(self.item_list)):
            if self.item_list[i] not in self.item_list[i:]:
                print(f"{self.item_list[i]} = {self.item_list.count(self.item_list[i])}")
            if self.item_list[i] in self.item_list[i + 1:]:
                if self.item_list[i] not in self.counted:
                    continue
            print(f"{self.item_list[i]} = {self.item_list.count(self.item_list[i])}")

    def duplicates(self):
        print("DuplicatesFound:")
        for i in range(len(self.item_list)):
            if self.item_list[i] in self.item_list[i + 1:]:
                continue
            print(f"\t{self.item_list[i]} = {self.item_list.count(self.item_list[i])}")

    def no_duplicates(self):
        for i in range(len(self.item_list)):
            if self.item_list[i] not in self.item_list[i + 1:]:
                if self.item_list.count(self.item_list[i]) == 1:
                    print(f"No Duplicates Found:\n\t{self.item_list[i]} = {self.item_list.count(self.item_list[i])}")


class Item:
    def __init__(self):
        self.items = {
            'Fruits': ['Apple', 'Banana', 'Oranges', 'Tangerine'],
            'Meat': ['Beef'],
            'Vegetables': ['Carrots', 'Cucumbers'],
        }

if __name__ == '__main__':
    cart = Cart()
    item = Item()
    cart.add_item(item.items['Fruits'][0])
    cart.add_item(item.items['Fruits'][0])
    cart.add_item(item.items['Fruits'][1])
    cart.add_item(item.items['Fruits'][1])
    # cart.add_item(item.items['Fruits'][3])
    cart.add_item(item.items['Fruits'][3])
    cart.add_item("Fish")
    cart.add_item("Banana")
    cart.add_item("Banana")
    cart.add_item("Fish")
    cart.add_item("Oranges")
    cart.add_item("Oranges")
    cart.add_item("Oranges")
    cart.add_item("Oranges")
    cart.add_item("Oranges")
    cart.add_item("Oranges")
    cart.add_item("Oranges")
    # cart.counts()
    cart.no_duplicates()
    cart.duplicates()
    cart.display_cart()
