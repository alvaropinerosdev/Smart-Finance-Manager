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

# 4. Intermediaries

`intermediaries/` acts as a coordination layer between the different parts of the system.

```text
intermediaries/
├── validators/
├── mappers/
└── router/
```

The logic and services do not communicate directly with each other. The intermediaries control and coordinate the flow between both parts.

---

## 4.1 Validators

`validators/` is responsible for validating inputs before they reach the logic layer.

Responsibility:

```text
input
  ↓
validator
  ↓
valid / invalid
```

Validators must not contain financial domain logic.

Their purpose is to validate the structure, types, formats, and input conditions corresponding to their responsibility.

---

## 4.2 Mappers

`mappers/` transforms information between the representations used by the different layers.

For example:

```text
external data
     ↓
   Mapper
     ↓
Entity
```

And later:

```text
Entity
   ↓
Mapper
   ↓
persistence data
```

Mappers must not contain business rules.

Their responsibility is to transform data between representations.

---

## 4.3 Router

The `router/` coordinates use cases and controls the flow between components.

For example, a conceptual operation for registering an expense could follow:

```text
input
  ↓
validator
  ↓
mapper
  ↓
router
  ↓
logic
  ↓
router
  ↓
mapper
  ↓
service
```

The router coordinates the flow but must not implement business rules.

If a decision belongs to the financial domain, it must be implemented in `logic/`.

---

# 5. Services

`services/` contains the communication with PostgreSQL and the persistence of information.

```text
services/
├── connection.py
└── ...
```

This layer will be implemented later, after completing the system logic.

Its responsibilities will include:

* establishing connections with PostgreSQL;
* executing SQL queries;
* inserting data;
* retrieving data;
* updating data;
* deleting data or performing soft deletes;
* handling persistence operations.

Services are the only layer that should directly know the details of PostgreSQL and SQL.

Queries must use parameters, avoiding unsafe SQL construction through string concatenation.

Conceptually:

```text
Logic
   ↑
Intermediaries
   ↑
Services
   ↓
PostgreSQL
```

The logic layer must not contain SQL.
