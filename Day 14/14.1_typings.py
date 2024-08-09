from typing import List, Dict, Optional, Set, Tuple, Any, Union, Callable

# ---------- ТИПИЗАЦИЯ
print("----- ТИПИЗАЦИЯ -----")


# Типизация переменных
age: int = 25
name: str = "John"
is_married: bool = False
height: float = 1.75

products: list = ["apple", "banana", "cherry"]
participants: set = {"John", "Alice", "Bob"}
chess_board_columns: tuple = ("a", "b", "c", "d", "e", "f", "g", "h")
marks: dict = {"math": 5, "english": 4, "history": 3}

customer_id: int | str = "123"  # может принимать значения int или str


# Типизация используя библиотеку typing
interests: List[str] \
    = ["music", "reading", "travelling", "cooking"]  # список, который может содержать значения типа str
party_participants: Set[str] = {"John", "Alice", "Bob"}  # сет, который может содержать значения типа str
chess_board_column_names: Tuple[str, str, str, str, str, str, str, str] \
    = ("a", "b", "c", "d", "e", "f", "g", "h")  # кортеж, который должен содержать 8 значений типа str
person: Dict[str, int] = {"height": 178, "age": 25}  # может содержать ключи типа str и значения типа int

file: Any = 'any'  # может принимать любые значения
file_id: Union[int, str] = 123  # может принимать значения int или str
specialization: Optional[str] = None  # может принимать значение None или указанного типа (str)
