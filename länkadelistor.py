#1

class OneList:
    def __init__(self):
        self.head = None

    def insort(self, value):
        new_node = {"value": value, "next": None}

        if not self.head or value < self.head["value"]:
            new_node["next"] = self.head
            self.head = new_node
            return

        current = self.head
        while current["next"] and current["next"]["value"] < value:
            current = current["next"]

        new_node["next"] = current["next"]
        current["next"] = new_node

    def display(self):
        current = self.head
        while current:
            print(current["value"], end=" -> ")
            current = current["next"]
        print("None")


if __name__ == "__main__":
    # Skapa en ny länkad lista
    my_list = OneList()

    my_list.insort(5)
    my_list.insort(3)
    my_list.insort(7)
    my_list.insort(1)
    my_list.insort(6)

    my_list.display()

