import re
from typing import List


def create_heading_id(text: str) -> str:
    return "-".join(text.lower().split())


def create_class_name(text: str) -> str:
    return "m2d-" + "-".join(text.lower().split("_"))


def convert_docstring_to_dict(text: str) -> List[dict]:
    sections = re.split(r"\n\n", text.strip())
    result = []
    for section in sections:
        key_match = re.match(r"-\s+(\w+)\s+\(([^)]+)\):\s*([\s\S]*)", section)
        if key_match:
            key = key_match.group(1)
            prop_type = key_match.group(2)
            description = key_match.group(3).strip()
            res = {"name": key, "type": prop_type, "description": description}
            result.append(res)

    return result
