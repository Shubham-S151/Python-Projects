import json
from typing import Any, Dict, List

# Safe mapping instead of eval()
TYPE_MAP = {
    "int": int,
    "str": str,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict
}


def validate(schema: Dict[str, str], record: Dict[str, Any], strict: bool = True) -> None:
    """
    Validate a single record against the provided schema.

    Args:
        schema: Field name -> type mapping
        record: Record to validate
        strict: If True, disallow extra fields

    Raises:
        ValueError if validation fails
    """
    print(f"Inside validate_function in {__file__}")
    schema = schema[0]
    print("schema:",schema)
    # Check for missing fields
    for field, field_type in schema.items():
        if field not in record:
            raise ValueError(f"Missing required field: {field}")

        expected_type = TYPE_MAP.get(field_type)
        if expected_type is None:
            raise ValueError(f"Unsupported type in schema: {field_type}")

        if not isinstance(record[field], expected_type):
            raise ValueError(
                f"Field '{field}' expected type {expected_type.__name__}, "
                f"got {type(record[field]).__name__}"
            )

    # Optional: block extra fields
    if strict:
        for key in record:
            if key not in schema:
                raise ValueError(f"Unexpected field: {key}")


def validate_records(schema: Dict[str, str], records: List[Dict[str, Any]]) -> None:
    """Validate multiple records."""
    for record in records:
        validate(schema, record)


def load_schema(schema_path: str) -> Dict[str, str]:
    """Load schema JSON file."""
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)