# Class Diagram Design

## Introduction

The following diagram represents the **Class Diagram (UML)** of **Smart Finance Manager - Version 1**.

This model defines the object-oriented structure of the system's domain and architecture. It illustrates the classes, attributes, methods, inheritance hierarchies, and relationships between components across the logic, intermediaries, and services layers.

![Class Diagram](Images/Class%20Diagram.png)

### Main Classes

- **User**: Central entity representing the application user. Acts as the logical owner of categories, records, goals, and reports.
- **FinancialRecord**: Abstract base class representing any financial movement. Specialized into concrete `Income` and `Expense` classes.
- **Income**: Specialization of `FinancialRecord` representing incoming funds (positive signed amount).
- **Expense**: Specialization of `FinancialRecord` representing outgoing expenditures (negative signed amount).
- **Category**: Classifies financial records into custom or system-default categories.
- **Goal**: Represents financial targets set by users, tracking accumulated savings and deadlines.
- **Contribution**: Represents individual financial allocations deposited toward a savings goal.
- **FinancialReport**: Stores generated periodic financial summaries, aggregating transactional records.
- **ModificationHistory**: Polymorphic audit entity tracking granular property changes across system records.
- **Statistics**: Service-layer component responsible for computing balances, category aggregations, and goal progress.
- **ExcelExporter**: Service-layer utility responsible for converting reports, goals, and records into Excel spreadsheets.

### Class Relationships & Associations

| Relationship | Type / Notation | Description |
|---|---|---|
| User → FinancialRecord | Association | A user creates, owns, and manages their financial records. |
| User → Category | Association | A user creates and customizes their classification categories. |
| User → Goal | Association | A user defines and maintains their financial goals. |
| User → FinancialReport | Association | A user generates and queries periodic financial reports. |
| Category → FinancialRecord | Association | A category classifies transactions via `FinancialRecord.category_id`. |
| Goal → Contribution | Composition / Aggregation | A goal accumulates contributions via `Contribution.goal_id`. |
| FinancialRecord → ModificationHistory | Association (Audits) | Modifications to financial records are tracked in history logs. |
| Goal → ModificationHistory | Association (Audits) | Changes to financial goals are tracked in history logs. |
| FinancialReport → FinancialRecord | Dependency / Association (`summarizes`) | Reports consolidate and summarize financial transactions. |
| FinancialReport → ModificationHistory | Dependency / Association (`audits`) | Reports can query and audit recorded modifications. |
| Statistics → FinancialRecord | Dependency / Service | Computes balances, category totals, and monthly trends from records. |
| Statistics → Goal | Dependency / Service | Calculates progress ratios and completion metrics for goals. |
| ExcelExporter → FinancialReport | Dependency / Service | Exports structured financial reports into formatted Excel files. |
| ExcelExporter → Goal | Dependency / Service | Exports savings goals and progress data into Excel spreadsheets. |
| FinancialRecord △─ Income | Inheritance (Generalization / Realization) | `Income` inherits common attributes and behavior, returning a positive signed amount. |
| FinancialRecord △─ Expense | Inheritance (Generalization / Realization) | `Expense` inherits common attributes and behavior, returning a negative signed amount. |

### Architectural Notes

- **Inheritance Hierarchy**: `FinancialRecord` serves as an abstract base class. It is not instantiated directly; concrete instances are either `Income` or `Expense`.
- **Domain Entities vs. Service Components**: Classes such as `User`, `Category`, `FinancialRecord`, `Goal`, `Contribution`, `FinancialReport`, and `ModificationHistory` represent core **Domain Entities**. Conversely, `Statistics` and `ExcelExporter` represent **Application Services / Utilities** (non-persisted computational and export helpers).
- **Audit & Polymorphism**: `ModificationHistory` uses a polymorphic link (`record_type` + `record_id`) allowing unified change tracking without duplicating audit infrastructure across domain entities.
- **Soft Deletion**: Entities implement a `deleted_at` attribute, allowing safe logical deletion (`soft_delete()`, `is_active()`) while preserving audit integrity and historical accuracy.

---

## Detailed Class Specifications

This section details the attributes, methods, and responsibilities for each class in the model.

### 1. Core Domain Entities & Inheritance

#### `FinancialRecord` *(Abstract Base Class)*
The general abstraction for any financial movement. It encapsulates common transactional fields and defines common validation and lifecycle behaviors.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique identifier for the movement. |
| `user_id` | `UUID` | The owning user identifier. |
| `category_id` | `UUID` | Associated classification category. |
| `type` | `RecordType` | Discriminator indicator (`INCOME` or `EXPENSE`). |
| `amount` | `Decimal` | Monetary value of the transaction. |
| `currency` | `str` | ISO 4217 three-letter currency code (e.g., `'USD'`). |
| `description` | `Optional[str]` | Optional narrative description or notes. |
| `payment_method` | `Optional[str]` | Medium used (e.g., `'Cash'`, `'Debit Card'`). |
| `location` | `Optional[str]` | Physical or vendor location. |
| `transaction_datetime` | `datetime` | Date and time when the movement took place. |
| `created_at` | `datetime` | Audit timestamp when the record was created. |
| `updated_at` | `datetime` | Audit timestamp when the record was last modified. |
| `deleted_at` | `Optional[datetime]` | Timestamp for soft deletion (`None` if active). |

##### Key Methods:
- `signed_amount() -> Decimal`: Abstract or virtual method returning the signed financial impact (positive for income, negative for expense).
- `validate_category() -> bool`: Ensures the assigned category matches the transaction type.
- `update_details(...) -> None`: Updates mutable attributes while updating audit metadata.
- `is_in_period(start_date: date, end_date: date) -> bool`: Checks whether the transaction occurred within a given date range.
- `soft_delete() -> None`: Sets `deleted_at` to mark the record as logically deleted.
- `is_active() -> bool`: Returns `True` if `deleted_at` is `None`.

---

#### `Income` *(Derived from FinancialRecord)*
Represents a cash inflow. Specializes `FinancialRecord` by establishing the record type as income.

- **Inherits**: All attributes and common lifecycle methods from `FinancialRecord`.
- **Specialization**:
  - Sets `type = RecordType.INCOME`.
  - `signed_amount() -> Decimal`: Returns the amount as a positive value (`+amount`).

---

#### `Expense` *(Derived from FinancialRecord)*
Represents a cash outflow. Specializes `FinancialRecord` by establishing the record type as expense.

- **Inherits**: All attributes and common lifecycle methods from `FinancialRecord`.
- **Specialization**:
  - Sets `type = RecordType.EXPENSE`.
  - `signed_amount() -> Decimal`: Returns the amount as a negative value (`-amount`).

---

### 2. User & Classification Domain

#### `User`
The central root entity representing registered system users. Serves as the logical owner of all categories, movements, savings goals, and reports.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique user account identifier. |
| `created_at` | `datetime` | Registration timestamp. |
| `updated_at` | `datetime` | Last profile update timestamp. |

---

#### `Category`
Provides classification labels to categorize income and expenses for organization and reporting.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique category identifier. |
| `user_id` | `UUID` | Identifier of the user who owns this category. |
| `name` | `str` | Name of the category (e.g., "Salary", "Food"). |
| `type` | `RecordType` | Type of records accepted (`INCOME` or `EXPENSE`). |
| `is_default` | `bool` | Flag indicating whether this is a system preset category. |
| `created_at` | `datetime` | Creation timestamp. |
| `updated_at` | `datetime` | Last modification timestamp. |
| `deleted_at` | `Optional[datetime]` | Timestamp for soft deletion. |

##### Key Methods:
- `rename(new_name: str) -> None`: Updates the category title with validation.
- `accepts(record_type: RecordType) -> bool`: Verifies whether a given transaction type matches the category.
- `soft_delete() -> None`: Flags the category as inactive.
- `is_active() -> bool`: Validates if the category is currently active.

---

### 3. Goals & Savings Domain

#### `Goal`
Represents user-defined financial savings targets, tracking deadlines and progress.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique goal identifier. |
| `user_id` | `UUID` | Identifier of the owning user. |
| `name` | `str` | Title or description of the goal. |
| `target_amount` | `Decimal` | Target savings amount. |
| `target_date` | `date` | Target completion deadline. |
| `currency` | `str` | ISO 4217 currency code. |
| `created_at` | `datetime` | Goal creation timestamp. |
| `updated_at` | `datetime` | Last update timestamp. |
| `deleted_at` | `Optional[datetime]` | Soft delete timestamp. |

##### Key Methods:
- `add_contribution(contribution: Contribution) -> None`: Registers a deposit toward this goal.
- `total_contributed() -> Decimal`: Computes total accumulated savings from all contributions.
- `remaining_amount() -> Decimal`: Calculates the remaining amount needed to reach the target.
- `progress_percentage() -> float`: Returns completion percentage toward the target amount.
- `get_status() -> GoalStatus`: Returns the goal status (e.g., `IN_PROGRESS`, `COMPLETED`, `OVERDUE`).
- `update_details(...) -> None`: Updates target parameters.
- `soft_delete() -> None`: Logically deletes the goal.

---

#### `Contribution`
Represents an individual monetary deposit or allocation allocated toward a specific goal.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique contribution identifier. |
| `goal_id` | `UUID` | Associated savings goal identifier. |
| `amount` | `Decimal` | Contributed amount. |
| `currency` | `str` | ISO 4217 currency code. |
| `contribution_date` | `datetime` | Date and time when the contribution occurred. |
| `created_at` | `datetime` | Creation timestamp. |
| `updated_at` | `datetime` | Last update timestamp. |
| `deleted_at` | `Optional[datetime]` | Soft delete timestamp. |

---

### 4. Reporting & Audit Domain

#### `FinancialReport`
Stores aggregated financial statements and analytical snapshots for a specific user and timeframe.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique report identifier. |
| `user_id` | `UUID` | Owning user identifier. |
| `period_start` | `date` | Start date of the reporting timeframe. |
| `period_end` | `date` | End date of the reporting timeframe. |
| `generated_at` | `datetime` | Timestamp when calculations were executed. |
| `report_data` | `dict` / `JSON` | Structured computed summary (totals, category breakdown, net balance). |

##### Key Methods:
- `generate(records: list[FinancialRecord]) -> None`: Generates summary calculations based on transaction records.
- `get_section(name: str) -> Any`: Retrieves a specific analytical block from `report_data`.

---

#### `ModificationHistory`
Polymorphic audit model tracking historical field modifications on critical domain entities.

| Attribute | Type | Description |
|---|---|---|
| `id` | `UUID` | Unique audit entry identifier. |
| `record_type` | `str` | Target entity class name (e.g., `'FinancialRecord'`, `'Goal'`). |
| `record_id` | `UUID` | Primary key of the modified entity. |
| `field_name` | `str` | Database/class attribute modified. |
| `old_value` | `Optional[str]` | Previous attribute value. |
| `new_value` | `Optional[str]` | Updated attribute value. |
| `modified_at` | `datetime` | Timestamp of the change. |
| `expires_at` | `Optional[datetime]` | Optional audit retention expiration date. |

---

### 5. Application Services & Utilities

#### `Statistics` *(Service / Calculation Component)*
A domain calculation service that computes aggregate metrics without maintaining persistence state.

##### Key Responsibilities & Methods:
- `calculate_balance(records: list[FinancialRecord]) -> Decimal`: Computes net total balance (incomes minus expenses).
- `get_category_totals(records: list[FinancialRecord]) -> dict[str, Decimal]`: Groups transactions by category and calculates subtotals.
- `calculate_monthly_trend(records: list[FinancialRecord]) -> dict`: Analyzes income and expense trends across months.
- `calculate_goal_progress(goal: Goal) -> float`: Evaluates goal performance and timeline progress.

---

#### `ExcelExporter` *(Service / Export Utility)*
An infrastructure-facing service responsible for serializing domain models into styled Microsoft Excel (`.xlsx`) files.

##### Key Responsibilities:
- `export_financial_records(records: list[FinancialRecord], filepath: str) -> None`: Exports transactional records.
- `export_goals(goals: list[Goal], filepath: str) -> None`: Exports savings goals, targets, and contribution histories.
- `export_report(report: FinancialReport, filepath: str) -> None`: Exports generated financial summaries and balance reports.

---

## Implementation & Mapping Guidelines

1. **Relational Database Mapping**:
   - Primary domain entities map directly to database tables: `User`, `Category`, `FinancialRecord`, `Goal`, `Contribution`, `FinancialReport`, and `ModificationHistory`.
   - **Single Table Inheritance**: `FinancialRecord` uses a `type` column (`'INCOME'` or `'EXPENSE'`) in the database. In the Python application layer, object-oriented instantiation maps rows to concrete `Income` or `Expense` subclasses.
2. **Services vs. Entities**:
   - `Statistics` and `ExcelExporter` are strictly stateless services or utility classes within `src/logic/calculations/` and `src/utils/`, not database tables.
3. **Decoupled Business Logic**:
   - Entities encapsulate validation and state logic independently of SQL queries or PostgreSQL drivers, ensuring compliance with the project architecture.
