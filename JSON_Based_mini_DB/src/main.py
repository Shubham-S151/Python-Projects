import os
import sys
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.database import Database
from src.operations.crud import (
    insert_record,
    find_records,
    update_records,
    delete_records,
    show_all_records
)


def print_menu():
    print("\n===== JSON Mini Database =====")
    print("1. Insert Record")
    print("2. Find Records")
    print("3. Update Records")
    print("4. Delete Records")
    print("5. Show All Records")
    print("6. Exit")


def parse_input():
    """
    Converts user input like:
    name=Alice age=25

    Into:
    {"name": "Alice", "age": 25}
    """
    raw = input("Enter key=value pairs (space separated): ").strip()

    record = {}

    if not raw:
        return record

    for pair in raw.split(): 
        if "=" not in pair:
            print(f"Skipping invalid input: {pair}")
            continue

        key, value = pair.split("=", 1)

        # Basic type inference
        if value.isdigit():
            value = int(value)
        elif value.replace(".", "", 1).isdigit():
            value = float(value)

        record[key] = value

    return record


def main():
    db_name = input("Enter collection/database name: ").strip()
    db = Database(db_name)

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                record = parse_input()
                insert_record(db, record)
                print("✔ Record inserted successfully")

            elif choice == "2":
                query = parse_input()
                results = find_records(db, query)
                print(f"\n✔ Found {len(results)} record(s):")
                for r in results:
                    print(r)

            elif choice == "3":
                print("Enter query:")
                query = parse_input()

                print("Enter new values:")
                new_values = parse_input()

                count = update_records(db, query, new_values)
                print(f"✔ Updated {count} record(s)")

            elif choice == "4":
                query = parse_input()
                count = delete_records(db, query)
                print(f"✔ Deleted {count} record(s)")

            elif choice == "5":
                records = show_all_records(db)
                print(f"\n✔ Total records: {len(records)}")
                for r in records:
                    print(r)

            elif choice == "6":
                print("Exiting database...")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()