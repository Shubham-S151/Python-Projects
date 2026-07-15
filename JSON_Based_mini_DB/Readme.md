# JSON-Based Mini Database System

---

## Project Overview

This project is a **JSON-based mini database engine** built in Python.
It simulates basic functionalities of a NoSQL database system such as:

* Data storage using JSON files
* CRUD operations (Create, Read, Update, Delete)
* Query-based search
* Schema validation
* Modular architecture

The goal of this project is to understand **backend system design fundamentals**, including data handling, abstraction, and modular programming.

---

## Architecture Overview

The project follows a **layered modular architecture**, separating responsibilities into distinct components:

```
User Interface (CLI)
        ↓
Database Engine (Core Layer)
        ↓
Operations Layer (CRUD + Query)
        ↓
Storage Layer (File Handling)
        ↓
JSON Files (Persistent Storage)
```

### Key Design Principles

* **Separation of Concerns**: Each module has a single responsibility
* **Modularity**: Components are reusable and independent
* **Scalability**: Easy to extend with new features (indexing, caching, etc.)
* **Maintainability**: Clean structure for debugging and updates

---

## 📁 Project Structure

```
JSON_Based_mini_DB/

├── data/
│   └── *.json                 # Stores actual records
│
├── schemas/
│   └── *_schema.json         # Defines structure of collections
│
├── metadata/
│   └── db_meta.json          # Stores database-related info
│
├── src/
│   ├── core/
│   │   ├── database.py
│   │   ├── storage.py
│   │   └── schema_manager.py
│   │
│   ├── operations/
│   │   ├── crud.py
│   │   └── query.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   ├── config.py
│   └── main.py
│
└── README.md
```

---

## Module & File Responsibilities

---

### 🔹 `main.py`

**Role:** Entry point of the application

**Responsibilities:**

* Handles CLI interaction
* Takes user input
* Calls database methods

---

### 🔹 `config.py`

**Role:** Central configuration file

**Responsibilities:**

* Stores file paths (data, schema, metadata)
* Global constants
* Environment configuration

---

## Core Layer

---

### 🔹 `core/database.py`

**Role:** Main database engine (controller)

**Class:** `Database`

**Responsibilities:**

* Acts as an interface between user and system
* Routes operations to appropriate modules

**Key Methods:**

* `insert(collection, data)`
* `find(collection, query)`
* `update(collection, query, new_data)`
* `delete(collection, query)`

---

### 🔹 `core/storage.py`

**Role:** Handles file operations

**Functions:**

* `read_json(file_path)`
* `write_json(file_path, data)`

**Responsibilities:**

* Reading JSON data from disk
* Writing updated data back to disk

---

### 🔹 `core/schema_manager.py`

**Role:** Validates data structure

**Functions:**

* `validate(schema, data)`

**Responsibilities:**

* Ensures inserted/updated data follows schema rules
* Prevents invalid data storage

---

## Operations Layer

---

### 🔹 `operations/crud.py`

**Role:** Implements CRUD logic

**Functions:**

* `insert_record(collection, data)`
* `update_record(collection, query, new_data)`
* `delete_record(collection, query)`

**Responsibilities:**

* Applies business logic
* Interacts with storage layer

---

### 🔹 `operations/query.py`

**Role:** Handles searching and filtering

**Functions:**

* `match_query(record, query)`
* `filter_records(records, query)`

**Responsibilities:**

* Evaluates conditions (e.g., equality, greater than)
* Returns matching results

---

## Utility Layer

---

### 🔹 `utils/helpers.py`

**Role:** Common helper functions

**Examples:**

* ID generation
* Data formatting
* Logging helpers

---

## Data Layer

---

### 🔹 `data/`

* Stores all records in JSON format
* Each file represents a collection (like a table)

Example:

```
users.json
products.json
```

---

### 🔹 `schemas/`

* Defines structure of collections

Example schema:

```
{
  "name": "string",
  "age": "int",
  "email": "string"
}
```

---

### 🔹 `metadata/`

* Stores database-level information

Example:

* list of collections
* schema mappings

---

## Features Implemented

* JSON-based persistent storage
* Modular database architecture
* CRUD operations
* Query filtering system
* Schema validation

---

## Future Enhancements

* Indexing for faster search
* Query language support (like MongoDB operators)
* CLI improvements
* Logging system
* Basic transaction support

---

## Conclusion

This project demonstrates how a simple JSON file system can be abstracted into a **mini database engine**, providing insights into:

* Backend architecture
* Data management
* System design thinking

---