from typing import Any
from backend.settings import BASE_DIR, DEBUG

def app_debug_printer(origin: str, description: str, output: Any,):
    """
        - origin is `__file__` where  `app_debug_printer` is called
    """
    

    if DEBUG:
        return print("APP_DEBUG ::", {
            "description": description,
            "output": output,
            "origin": origin.replace(BASE_DIR.__str__(), "...")
        })