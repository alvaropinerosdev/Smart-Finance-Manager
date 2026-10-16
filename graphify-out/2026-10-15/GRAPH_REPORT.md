# Graph Report - Smart_Finance_Manager  (2026-10-13)

## Corpus Check
- 16 files · ~36,198 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 204 nodes · 355 edges · 16 communities (10 shown, 6 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 56 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `06ad798b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- exceptions.py
- User
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- Git Workflow & Branching Strategy Guidelines
- logic_entities_expense
- FinancialRecord
- logic_entities_income
- Expense
- user.py
- datetime
- uuid
- Income

## God Nodes (most connected - your core abstractions)
1. `User` - 27 edges
2. `FinancialRecord` - 24 edges
3. `DomainValidationError` - 19 edges
4. `Income` - 18 edges
5. `Expense` - 14 edges
6. `TestFinancialRecordValidation` - 11 edges
7. `TestUserEntity` - 9 edges
8. `TestUserValidation` - 9 edges
9. `FinancialRecord` - 8 edges
10. `User` - 7 edges

## Surprising Connections (you probably didn't know these)
- ``entities/`` --references--> `FinancialRecord`  [INFERRED]
  Docs/Architecture.md → src/logic/entities/financial_record.py
- ``User`` --references--> `User`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/user.py
- ``Expense` *(Derived from FinancialRecord)*` --references--> `Expense`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/expense.py
- `Architectural Notes` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- `Implementation & Mapping Guidelines` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (16 total, 6 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "exceptions.py"
Cohesion: 0.20
Nodes (9): Exception, Base Exceptions for Smart Finance Manager, Base exception for all domain and application errors., SmartFinanceError, Smoke test to verify that the testing environment, test runner, and project…, Verify that pytest is functioning properly., Verify that domain exceptions in src can be imported and instantiated., test_smoke_domain_exceptions_import() (+1 more)

### Community 2 - "User"
Cohesion: 0.14
Nodes (15): pytest, Root domain entity representing registered system users. Acts as the logical…, User, sys, datetime, fixture, UUID, Unit tests for User and Category entities. (+7 more)

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Detailed Class Specifications"
Cohesion: 0.11
Nodes (18): 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, 5. Application Services & Utilities, `Category`, `Contribution`, Detailed Class Specifications, `ExcelExporter` *(Service / Export Utility)* (+10 more)

### Community 7 - "Git Workflow & Branching Strategy Guidelines"
Cohesion: 0.17
Nodes (11): 1. Branch Strategy Overview, 2. Engineering Incident & Lessons Learned (Interview Case Study), 3. Key Takeaways for Technical Interviews, 4. Strict Sub-Branch Integration Protocol (Preventing Involuntary Merges to `main`), Corrective Action Taken, Git Workflow & Branching Strategy Guidelines, Mandatory Rule: `v1` Exclusivity, Operational Checklist to Prevent Recurrence: (+3 more)

### Community 9 - "FinancialRecord"
Cohesion: 0.17
Nodes (15): ABC, 1. Core Domain Entities & Inheritance, `Expense` *(Derived from FinancialRecord)*, `FinancialRecord` *(Abstract Base Class)*, `Income` *(Derived from FinancialRecord)*, Key Methods:, DomainValidationError, Raised when an entity or business invariant validation fails. (+7 more)

### Community 11 - "Expense"
Cohesion: 0.12
Nodes (16): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes, logic_entities_financial_record, Expense (+8 more)

### Community 12 - "user.py"
Cohesion: 0.27
Nodes (5): datetime, UUID, User Entity Module. Defines the root user entity for Smart Finance Manager., Update the updated_at timestamp to the specified datetime or the current UTC…, typing

### Community 16 - "Income"
Cohesion: 0.11
Nodes (21): decimal, logic_entities, parametrize, Income, Concrete financial record representing an income (positive cash flow). Inherits…, datetime, fixture, UUID (+13 more)

## Knowledge Gaps
- **34 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+29 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 79 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `FinancialRecord` to `Expense`, `Income`, `Architecture.md`?**
  _High betweenness centrality (0.228) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `FinancialRecord`, `Expense`, `Detailed Class Specifications`, `user.py`?**
  _High betweenness centrality (0.175) - this node is a cross-community bridge._
- **Why does `DomainValidationError` connect `FinancialRecord` to `Income`, `exceptions.py`, `User`, `user.py`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `User` (e.g. with `Architectural Notes` and `Implementation & Mapping Guidelines`) actually correct?**
  _`User` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `FinancialRecord` (e.g. with ``entities/`` and `Architectural Notes`) actually correct?**
  _`FinancialRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `DomainValidationError` (e.g. with `FinancialRecord` and `User`) actually correct?**
  _`DomainValidationError` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `Income` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Income` has 13 INFERRED edges - model-reasoned connections that need verification._