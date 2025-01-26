class Task:
    def __init__(self, description, deadline):
        """Конструктор для инициализации задачи.

        :param description: Описание задачи.
        :param deadline: Срок выполнения задачи в формате 'YYYY-MM-DD'.
        """
        self.description = description
        self.deadline = deadline
        self.status = "not completed"

    def mark_as_completed(self):
        """Метод для отметки задачи как выполненной.
        """
        self.status = "completed"

    def __str__(self):
        """Метод для представления задачи в виде строки.
        """
        return f"Task(description='{self.description}', deadline='{self.deadline}', status='{self.status}')"

class Store:
    def __init__(self, name, address):
        """Конструктор для инициализации магазина.

        :param name: Название магазина.
        :param address: Адрес магазина.
        """
        self.name = name
        self.address = address
        self.items = {}  # Словарь с товарами и их ценами.

    def add_item(self, item_name, price):
        """Метод для добавления товара в ассортимент.

        :param item_name: Название товара.
        :param price: Цена товара.
        """
        if item_name in self.items:
            print(f"Товар '{item_name}' уже существует. Для обновления цены используйте метод update_price.")
        else:
            self.items[item_name] = price
            print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Метод для удаления товара из ассортимента.

        :param item_name: Название товара.
        """
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """
        Метод для получения цены товара по его названию.

        :param item_name: Название товара.
        :return: Цена товара или None, если товар не найден.
        """
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Метод для обновления цены товара.

        :param item_name: Название товара.
        :param new_price: Новая цена товара.
        """
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __str__(self):
        """Метод для представления магазина в виде строки."""
        return f"Store(name='{self.name}', address='{self.address}', items={self.items})"

def main():
    # Создание задач
    task1 = Task("Сделать отчет", "2025-01-30")
    task2 = Task("Подготовить презентацию", "2025-02-05")

    print(task1)
    task1.mark_as_completed()
    print(task1)

    print("\n--- Магазины ---\n")

    # Создание магазинов
    store1 = Store("Магазин у дома", "Москва, ул. Ленина, 1")
    store1.add_item("яблоки", 0.5)
    store1.add_item("бананы", 0.75)

    store2 = Store("Центральный магазин", "Санкт-Петербург, пр. Мира, 10")
    store2.add_item("хлеб", 1.2)
    store2.add_item("молоко", 0.9)
    store2.add_item("сыр", 2.5)

    store3 = Store("Гипермаркет", "Екатеринбург, ул. Свердлова, 5")
    store3.add_item("вода", 0.3)
    store3.add_item("сок", 1.0)

    # Тестирование методов
    print("\n--- Тестирование методов ---\n")
    print(store1.get_price("яблоки"))  # Вывод: 0.5
    store1.update_price("бананы", 0.8)
    print(store1.get_price("бананы"))  # Вывод: 0.8
    store1.remove_item("яблоки")
    print(store1.get_price("яблоки"))  # Вывод: None

    print("\n--- Вывод информации о магазинах ---\n")
    print(store1)
    print(store2)
    print(store3)

if __name__ == "__main__":
    main()
