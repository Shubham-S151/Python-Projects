import os
import sys

# Root Path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Data Storage Path
DATA_DIR = os.path.join(ROOT_DIR,"data")

# Metadata Storage Path
META_DIR = os.path.join(ROOT_DIR,"metadata")

# Schema Details Paths
SCHEMA_DIR = os.path.join(ROOT_DIR,"schemas")

# Code Directory Paths
SOURCE_DIR = os.path.join(ROOT_DIR, "src")
CORE_DIR = os.path.join(SOURCE_DIR, "core")
OPERATION_DIR = os.path.join(SOURCE_DIR, "operations")
UTILS_DIR = os.path.join(SOURCE_DIR, "utils")

# Ensure directories exist
for path in [DATA_DIR, SCHEMA_DIR, META_DIR]:
    os.makedirs(path, exist_ok=True)
    
# Creating Base Data Structure
class DataStructure:
    """
    Defines the structure of a collection in the JSON database.
    
    Attributes:
        col_names (Tuple[str, ...]): Column names for the collection
        data_types (Dict[str, Type]): Data type mapping for each column
        database (str): Name of the database/collection
        ncolumns (int): Number of columns
    """
    def __init__(self, col_names: tuple[str, ...], data_types: dict[str, type], database: str):
        if len(col_names) != len(data_types):
            raise ValueError("Length of column names and data_types must match")
        self.col_names = col_names
        self.data_types = data_types
        self.database = database
        self.ncolumns = len(col_names)

    def info(self):
        """Prints basic information about the collection structure."""
        print(f"Database Name    : {self.database}")
        print(f"No. of Columns   : {self.ncolumns}")
        print(f"Column Names     : {self.col_names}")
        print(f"Column Data Types: {self.data_types}")


# -------------------------------
# Example Usage
# -------------------------------

if __name__ == "__main__":
    # Example collection definition
    ds = DataStructure(
        col_names=("id", "name", "age", "email"),
        data_types={"id": int, "name": str, "age": int, "email": str},
        database="users"
    )
    ds.info()