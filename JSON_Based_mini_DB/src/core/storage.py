import json
import os
import tempfile
from typing import Any, Dict, List


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Read JSON data from a file.

    Returns:
        List of records (must be a list of dicts)
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Ensure structure is correct
        if not isinstance(data, list):
            raise ValueError(f"Invalid data format in {file_path}: expected a list")

        return data

    except json.JSONDecodeError as e:
        raise ValueError(f"Corrupted JSON in {file_path}: {e}")


def write_json(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Write JSON safely using atomic write.

    Prevents corruption if program crashes mid-write.
    """
    dir_name = os.path.dirname(file_path)

    try:
        # Write to temp file first
        with tempfile.NamedTemporaryFile(
            "w",
            delete=False,
            dir=dir_name,
            encoding="utf-8"
        ) as tmp_file:
            json.dump(data, tmp_file, indent=4)
            temp_name = tmp_file.name

        # Atomically replace original file
        os.replace(temp_name, file_path)

    except Exception as e:
        raise IOError(f"Failed to write JSON to {file_path}: {e}")


def append_json(file_path: str, record: Dict[str, Any]) -> None:
    """
    Append a record (safe but still O(n)).
    """
    data = read_json(file_path)
    data.append(record)
    write_json(file_path, data)


def clear_json(file_path: str) -> None:
    """Delete all records safely."""
    write_json(file_path, [])