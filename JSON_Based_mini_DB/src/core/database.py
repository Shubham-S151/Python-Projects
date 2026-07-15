import os
from typing import Any, Dict, List

from src.core.storage import read_json, write_json
from src.core.schema_manager import validate
from src.config import DATA_DIR, SCHEMA_DIR

# 🔥 Use your advanced query system
from src.operations.query import advanced_filter


class Database:
    """
    Core JSON-based database engine.
    Each instance represents one collection.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.data_path = os.path.join(DATA_DIR, f"{db_name}.json")
        self.schema_path = os.path.join(SCHEMA_DIR, f"{db_name}_schema.json")

        self.schema = self.load_schema()

    # -------------------------
    # Internal helpers
    # -------------------------

    def _load_data(self) -> List[Dict[str, Any]]:
        """Always read fresh data from disk."""
        return read_json(self.data_path)

    def _write_data(self, data: List[Dict[str, Any]]) -> None:
        """Write data safely."""
        write_json(self.data_path, data)

    def load_schema(self) -> Dict[str, str]:
        """Load schema (must exist)."""
        if not os.path.exists(self.schema_path):
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")
        return read_json(self.schema_path)

    # -------------------------
    # CRUD operations
    # -------------------------

    def insert(self, record: Dict[str, Any]) -> None:
        print(f"Inside insert function in {__file__}")
        data = self._load_data()

        validate(self.schema, record)
        data.append(record)

        self._write_data(data)

    def find(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        data = self._load_data()
        return advanced_filter(data, query)

    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        data = self._load_data()
        updated_count = 0

        for i, record in enumerate(data):
            if advanced_filter([record], query):
                # 🔥 SAFE UPDATE: validate BEFORE mutating
                updated_record = {**record, **new_values}
                validate(self.schema, updated_record)

                data[i] = updated_record
                updated_count += 1

        if updated_count > 0:
            self._write_data(data)

        return updated_count

    def delete(self, query: Dict[str, Any]) -> int:
        data = self._load_data()

        new_data = [r for r in data if not advanced_filter([r], query)]
        deleted_count = len(data) - len(new_data)

        if deleted_count > 0:
            self._write_data(new_data)

        return deleted_count

    def count(self) -> int:
        return len(self._load_data())

    def show_all(self) -> List[Dict[str, Any]]:
        return self._load_data()