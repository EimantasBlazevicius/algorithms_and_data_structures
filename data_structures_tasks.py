from typing import List
from collections import deque
import abc
import time

# Task 1
class BooksStack:
    def __init__(self,
                 stack_name: str,
                 category: str = None):
        self.stack_name = stack_name
        self.category = category
        self.stack: List[str] = []

    def add_new_book(self, title: str):
        self.stack.append(title)

    def get_book(self):
        return self.stack.pop()

    def all_books(self) -> List[str]:
        return self.stack

    def __add__(self, second_stack):
        new = BooksStack(stack_name=self.stack_name, category=self.category)
        new.stack = self.stack + second_stack.stack
        return new

    # comparision
    def __gt__(self, second_stack):
        return len(self.stack) > len(second_stack.stack)

    def __lt__(self, second_stack):
        return len(self.stack) < len(second_stack.stack)

    def __ge__(self, second_stack):
        return len(self.stack) >= len(second_stack.stack)

    def __le__(self, second_stack):
        return len(self.stack) <= len(second_stack.stack)

    def __str__(self):
        return f"Stack: {self.stack_name} with category of books: {self.category}"

    def __repr__(self):
        books = ' '.join(self.stack)
        return f"stack_name:{self.stack_name} \ncategory:  {self.category} \nbooks: {books}"

    def __len__(self):
        return len(self.stack)


my_books = BooksStack("My Stack of Books", "Natural")
my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

# print(my_books.all_books())
# print(my_books.get_book())
# print(my_books.all_books())

her_books = BooksStack("Her Stack of Books", "Natural")
her_books.add_new_book("Horses")
my_books = my_books + her_books

# print(my_books.all_books())
# print(my_books > her_books)
# print(my_books <= her_books)
# print(my_books)
# print(repr(my_books))
# print(len(my_books))


# Task 2

class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class Woman(Client):
    def __str__(self) -> str:
        return f"Madam {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self) -> str:
        return f"Mr {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Task 2.2
class FifoList:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop(0)


# Task 2.3
class CashRegister:
    def __init__(self):
        self.queue = FifoList()

    def add_client(self, client: Client):
        self.queue.append(client)
        # print(f"{client} join the queue")

    def process(self) -> Client:
        client = self.queue.pop()
        # print(f"Processing {client}")


class FasterCashRegister(CashRegister):

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def process(self):
        client = self.queue.popleft()
        # print(f"Processing {client}")


client1 = Woman("Anna", "Johnson")
client2 = Man("John", "Smith")
client3 = Child("Chris", "Novak")

cr = CashRegister()
cr.add_client(client1)
cr.add_client(client2)
cr.add_client(client3)

cr.process()
cr.process()
cr.process()


# Task 2.5
start1 = time.perf_counter()
cashier = CashRegister()
for _ in range(10000):
    cashier.add_client(client1)
for _ in range(10000):
    cashier.process()
finish1 = time.perf_counter()
run_time1 = round(finish1 - start1, 2)
# --------------------------------------
start2 = time.perf_counter()
cashier2 = FasterCashRegister()
for _ in range(10000):
    cashier2.add_client(client1)
for _ in range(10000):
    cashier2.process()
finish2 = time.perf_counter()
run_time2 = round(finish2 - start2, 2)

print(f"Normal ran for {run_time1}, second ran for {run_time2}")
