from typing import Any, Dict, List

def match_query(record: Dict[str, Any], query: Dict[str, Any]) -> bool:
    """
    Check if a record matches the query.

    Args:
        record (Dict[str, Any]): A single database record
        query (Dict[str, Any]): Query to match against (field -> value)

    Returns:
        bool: True if record matches query, False otherwise
    """
    for field, value in query.items():
        if field not in record:
            return False
        if record[field] != value:
            return False
    return True

def filter_records(records: List[Dict[str, Any]], query: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Return a list of records matching the query.

    Args:
        records (List[Dict[str, Any]]): List of all records
        query (Dict[str, Any]): Query to filter records

    Returns:
        List[Dict[str, Any]]: Filtered records
    """
    return [record for record in records if match_query(record, query)]

def advanced_filter(records: List[Dict[str, Any]], query: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Supports advanced queries (e.g., operators like >, <, contains)
    
    Example query:
    {
        "age": {"$gt": 20},
        "name": {"$contains": "Ali"}
    }
    """
    filtered = []

    for record in records:
        match = True
        for field, condition in query.items():
            if field not in record:
                match = False
                break

            # Example: exact match
            if isinstance(condition, dict):
                for op, val in condition.items():
                    if op == "$gt" and not (record[field] > val):
                        match = False
                    elif op == "$lt" and not (record[field] < val):
                        match = False
                    elif op == "$contains" and val not in str(record[field]):
                        match = False
            else:
                if record[field] != condition:
                    match = False

            if not match:
                break

        if match:
            filtered.append(record)

    return filtered

if __name__ == "__main__":
    sample_records = [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 22},
    ]

    query1 = {"age": 25}
    query2 = {"name": {"$contains": "li"}}

    print("Exact match:", filter_records(sample_records, query1))
    print("Advanced match:", advanced_filter(sample_records, query2))