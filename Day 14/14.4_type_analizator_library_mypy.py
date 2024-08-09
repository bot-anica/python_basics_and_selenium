from typing import List, Dict, Set, Tuple

# Для проверки типов используется библиотека mypy
# mypy path/to/file.py
# mypy Day\ 14/14.4_type_analizator_library_mypy.py

# ---------- АНАЛИЗАТОР ТИПОВ С ПОМОЩЬЮ БИБЛИОТЕКИ mypy
print("----- АНАЛИЗАТОР ТИПОВ С ПОМОЩЬЮ БИБЛИОТЕКИ mypy -----")


interests: List[str] = ["music", "reading", 123, "cooking", True]
party_participants: Set[str] = {"John", False, "Bob"}
chess_board_column_names: Tuple[str, str, str, str, str, str, str, str] = (1, 2, 3, 4, 5, 6, 7, 8)
person: Dict[str, int] = {"height": "178", "age": 25}
