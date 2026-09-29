# Database Design

## Introduction

The following diagram represents the **Entity-Relationship Diagram (ERD)** of **Smart Finance Manager - Version 1 Data Model**.

This model defines the core structure of the system’s database. It includes the main entities, their attributes, primary keys, foreign keys, and the relationships between them.

![Database UML Diagram](Images/database_uml.png)

### Main Entities

- **User**: Central entity that represents the system users. All other main entities belong to a user.
- **FinancialRecord**: Stores all financial transactions (both income and expenses). It is specialized into **Income** and **Expense**.
- **Category**: Allows users to classify their financial records.
- **Goal**: Represents financial goals set by the user.
- **Contribution**: Records the amounts contributed toward a specific goal.
- **FinancialReport**: Stores generated financial reports for a specific period.
- **ModificationHistory**: Keeps a history of changes made to important records (polymorphic relationship).

### Relationships

| Relationship                        | Cardinality | Description                                      |
|-------------------------------------|-------------|--------------------------------------------------|
| User → FinancialRecord              | 1 : N       | A user can have many financial records           |
| User → Category                     | 1 : N       | A user can create many categories                |
| User → Goal                         | 1 : N       | A user can create many goals                     |
| User → FinancialReport              | 1 : N       | A user can generate many financial reports       |
| Category → FinancialRecord          | N : 1       | A category can be used in many financial records |
| Goal → Contribution                 | 1 : N       | A goal can receive many contributions            |
| FinancialRecord → ModificationHistory | 1 : N     | A financial record can have many change records  |
| Goal → ModificationHistory          | 1 : N       | A goal can have many change records              |

### Special Notes

- **Inheritance**: `FinancialRecord` is specialized into `Income` and `Expense` using the `type` field.
- **ModificationHistory** is a polymorphic table (uses `record_type` + `record_id`) to track changes on different entities.
- Soft delete is implemented in several tables through the `deleted_at` field.

---

## Detailed Table Specifications

This section provides the complete data dictionary and structural definition for each table in **Smart Finance Manager - Version 1**. All primary keys utilize `UUID` to guarantee uniqueness and distributed scalability.

### 1. User & Classification Domain

#### `User`
The root entity representing system accounts. All transactional and personal data belongs to a specific user.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the user account. |
| `created_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Audit timestamp when the user registered. |
| `updated_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Audit timestamp when the user profile was last updated. |

---

#### `Category`
Represents classification labels used to categorize financial transactions for budgeting and analytical summaries.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the category. |
| `user_id` | `UUID` | `FOREIGN KEY (User.id)`, `NOT NULL` | The user who owns this custom category. |
| `name` | `VARCHAR(100)` | `NOT NULL` | Human-readable name of the category (e.g., "Food", "Salary"). |
| `type` | `RECORD_TYPE` | `NOT NULL` | Restricts category usage to either `'INCOME'` or `'EXPENSE'`. |
| `is_default` | `BOOLEAN` | `NOT NULL`, `DEFAULT FALSE` | Flag indicating whether this is a system-provided preset category. |
| `created_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Timestamp when the category was created. |
| `updated_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Timestamp of the last category update. |
| `deleted_at` | `TIMESTAMP` | `NULLABLE` | Soft delete timestamp (`NULL` indicates active category). |

---

### 2. Transaction Domain & Specializations

#### `FinancialRecord`
The core transactional ledger storing all financial movements. Implements a **Single Table Inheritance** pattern where the `type` field differentiates income from expenses.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the financial transaction. |
| `user_id` | `UUID` | `FOREIGN KEY (User.id)`, `NOT NULL` | The user who registered this financial record. |
| `category_id` | `UUID` | `FOREIGN KEY (Category.id)`, `NOT NULL` | Associated classification category. |
| `type` | `RECORD_TYPE` | `NOT NULL` | Transaction discriminator: `'INCOME'` or `'EXPENSE'`. |
| `amount` | `DECIMAL(12, 2)` | `NOT NULL`, `CHECK (amount > 0)` | Monetary value of the transaction. |
| `currency` | `CHAR(3)` | `NOT NULL` | ISO 4217 three-letter currency code (e.g., `'USD'`, `'COP'`). |
| `description` | `VARCHAR(255)` | `NULLABLE` | Optional descriptive note or merchant details. |
| `payment_method` | `VARCHAR(50)` | `NULLABLE` | Medium used (e.g., `'Cash'`, `'Debit Card'`, `'Transfer'`). |
| `location` | `VARCHAR(100)` | `NULLABLE` | Physical or merchant location where transaction occurred. |
| `transaction_datetime` | `TIMESTAMP` | `NOT NULL` | Effective date and time when the transaction took place. |
| `created_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Record creation audit timestamp. |
| `updated_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Last modification audit timestamp. |
| `deleted_at` | `TIMESTAMP` | `NULLABLE` | Soft delete timestamp (`NULL` indicates active record). |

##### Specialization Subtypes:
- **`Income`**: Virtual specialization entity representing cash inflows where `type = 'INCOME'`.
- **`Expense`**: Virtual specialization entity representing cash outflows where `type = 'EXPENSE'`.

---

### 3. Goals & Savings Domain

#### `Goal`
Stores user-defined financial savings targets, deadlines, and milestones.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the savings goal. |
| `user_id` | `UUID` | `FOREIGN KEY (User.id)`, `NOT NULL` | The user who defined this financial goal. |
| `name` | `VARCHAR(150)` | `NOT NULL` | Name or title of the goal (e.g., "Emergency Fund", "New Laptop"). |
| `target_amount` | `DECIMAL(12, 2)` | `NOT NULL`, `CHECK (target_amount > 0)` | Target total amount required to fulfill the goal. |
| `target_date` | `DATE` | `NOT NULL` | Target completion deadline date. |
| `currency` | `CHAR(3)` | `NOT NULL` | ISO 4217 currency code for the target amount. |
| `created_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Goal registration timestamp. |
| `updated_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Last update timestamp. |
| `deleted_at` | `TIMESTAMP` | `NULLABLE` | Soft delete timestamp (`NULL` indicates active goal). |

---

#### `Contribution`
Records individual deposits or financial allocations specifically committed toward achieving a savings goal.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the contribution deposit. |
| `goal_id` | `UUID` | `FOREIGN KEY (Goal.id)`, `NOT NULL` | The specific goal receiving this contribution. |
| `amount` | `DECIMAL(12, 2)` | `NOT NULL`, `CHECK (amount > 0)` | Contributed monetary amount. |
| `currency` | `CHAR(3)` | `NOT NULL` | Currency code matching the target goal currency. |
| `contribution_date` | `TIMESTAMP` | `NOT NULL` | Date and time when the allocation occurred. |
| `created_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Record creation timestamp. |
| `updated_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Last update timestamp. |
| `deleted_at` | `TIMESTAMP` | `NULLABLE` | Soft delete timestamp (`NULL` indicates active contribution). |

---

### 4. Reporting & Audit Domain

#### `FinancialReport`
Stores generated periodic financial summaries, balance statements, and statistical reports for fast retrieval.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the generated report instance. |
| `user_id` | `UUID` | `FOREIGN KEY (User.id)`, `NOT NULL` | The user for whom the report was computed. |
| `period_start` | `DATE` | `NOT NULL` | Starting date of the reporting timeframe. |
| `period_end` | `DATE` | `NOT NULL` | Ending date of the reporting timeframe. |
| `generated_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Exact timestamp when the calculations were executed. |
| `report_data` | `JSONB` | `NOT NULL` | Structured JSON containing computed balances, category aggregations, and trends. |

---

#### `ModificationHistory`
A flexible **polymorphic audit table** that tracks historical changes made to critical entities (`FinancialRecord`, `Goal`), allowing traceability without duplicating audit infrastructure.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | `PRIMARY KEY` | Unique identifier for the audit event. |
| `record_type` | `VARCHAR(50)` | `NOT NULL` | Target entity class name (e.g., `'FinancialRecord'`, `'Goal'`). |
| `record_id` | `UUID` | `NOT NULL` | The `id` of the specific entity instance modified. |
| `field_name` | `VARCHAR(50)` | `NOT NULL` | Name of the database column modified (e.g., `'amount'`, `'name'`). |
| `old_value` | `TEXT` | `NULLABLE` | Value before the change (converted to text representation). |
| `new_value` | `TEXT` | `NULLABLE` | New value as text representation |
| `modified_at` | `TIMESTAMP` | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP` | Timestamp when the modification took place. |
| `expires_at` | `TIMESTAMP` | `NULLABLE` | Optional retention expiration date for automated audit log pruning. |