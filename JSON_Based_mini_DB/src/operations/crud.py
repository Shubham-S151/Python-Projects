from typing import Any, Dict, List
from src.core.database import Database


def insert_record(db: Database, record: Dict[str, Any]) -> None:
    """
    Insert a new record.
    Raises exception if it fails.
    """
    db.insert(record)


def find_records(db: Database, query: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Return records matching query.
    """
    return db.find(query)


def update_records(db: Database, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
    """
    Update records and return number of updated entries.
    """
    return db.update(query, new_values)


def delete_records(db: Database, query: Dict[str, Any]) -> int:
    """
    Delete records and return number of deleted entries.
    """
    return db.delete(query)


def count_records(db: Database) -> int:
    return db.count()


def show_all_records(db: Database) -> List[Dict[str, Any]]:
    """
    Return all records.
    """
    return db.show_all()