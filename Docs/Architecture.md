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

