# Smart Finance Manager — System Architecture

## 1. Architecture Objective

The architecture of Smart Finance Manager will be designed to keep the responsibilities of the system separated and allow the project to grow without constantly modifying existing components.

The main architectural decision is to separate **business logic** from **data persistence**.

The first stage of development will focus on building the complete business logic without depending on PostgreSQL. PostgreSQL persistence and the corresponding services will be implemented afterward.

The architecture must allow the business logic to operate independently of the database.

---

## 2. Main Structure

The proposed structure inside `src/` will be:

```text
src/
├── logic/
│   ├── entities/
│   ├── rules/
│   └── calculations/
│
├── intermediaries/
│   ├── validators/
│   ├── mappers/
│   └── router/
│
├── services/
│   ├── connection.py
│   └── ...
│
├── adapters/
│
└── exceptions.py
```

`container.py` is excluded from the current definition and will be evaluated later, once the dependency management strategy has been defined.

## 3. Components

### 3.1 Logic

`logic/` contains the core of the system and represents the domain logic of Smart Finance Manager.

This layer must be independent of PostgreSQL and persistence details.

```text
logic/
├── entities/
├── rules/
└── calculations/
```

### `entities/`

Contains the domain entities implemented using object-oriented programming.

The entities represent the main objects of the system.

They include:

```text
User
Category
FinancialRecord
Income
Expense
Goal
Contribution
FinancialReport
ModificationHistory
```

`FinancialRecord` is the base class from which the following classes derive:

```text
FinancialRecord
├── Income
└── Expense
```

The entities belong to the domain and must not directly depend on PostgreSQL.

---

### `rules/`

Contains the business rules of the system.

Its responsibility is to represent the conditions that must be satisfied for domain operations to be valid.

Business rules belong to `logic/` and must not depend on SQL queries or PostgreSQL.

