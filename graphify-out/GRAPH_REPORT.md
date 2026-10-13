# Graph Report - Smart_Finance_Manager  (2026-10-12)

## Corpus Check
- 16 files · ~36,136 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 197 nodes · 323 edges · 13 communities (9 shown, 4 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 55 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6b6ee876`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- test_user_category.py
- User
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- Git Workflow & Branching Strategy Guidelines
- logic_entities_expense
- FinancialRecord
- logic_entities_income
- Income
- UUID

## God Nodes (most connected - your core abstractions)
1. `User` - 26 edges
2. `FinancialRecord` - 24 edges
3. `DomainValidationError` - 19 edges
4. `Income` - 18 edges
5. `Expense` - 14 edges
6. `TestFinancialRecordValidation` - 11 edges
7. `TestUserValidation` - 9 edges
8. `TestUserEntity` - 8 edges
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

## Communities (13 total, 4 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "test_user_category.py"
Cohesion: 0.12
Nodes (15): datetime, Exception, logic_entities, pytest, Base Exceptions for Smart Finance Manager, Base exception for all domain and application errors., SmartFinanceError, sys (+7 more)

### Community 2 - "User"
Cohesion: 0.10
Nodes (11): datetime, UUID, User Entity Module. Defines the root user entity for Smart Finance Manager., Root domain entity representing registered system users. Acts as the logical…, Update the updated_at timestamp to the specified datetime or the current UTC…, User, Tests verifying User entity lifecycle and behavior., Tests validating User domain invariants and error handling. (+3 more)

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

### Community 11 - "Income"
Cohesion: 0.13
Nodes (18): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes, logic_entities_financial_record, Expense (+10 more)

### Community 16 - "UUID"
Cohesion: 0.12
Nodes (18): decimal, fixture, parametrize, datetime, UUID, Unit tests for FinancialRecord, Income, and Expense entities., Tests verifying validation invariants on financial records., Tests ensuring FinancialRecord behaves as an abstract base class. (+10 more)

## Knowledge Gaps
- **34 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+29 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 79 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `FinancialRecord` to `Income`, `UUID`, `Architecture.md`?**
  _High betweenness centrality (0.240) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `FinancialRecord`, `Income`, `Detailed Class Specifications`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **Why does `DomainValidationError` connect `FinancialRecord` to `UUID`, `test_user_category.py`, `User`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `User` (e.g. with `Architectural Notes` and `Implementation & Mapping Guidelines`) actually correct?**
  _`User` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `FinancialRecord` (e.g. with ``entities/`` and `Architectural Notes`) actually correct?**
  _`FinancialRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `DomainValidationError` (e.g. with `FinancialRecord` and `User`) actually correct?**
  _`DomainValidationError` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `Income` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Income` has 13 INFERRED edges - model-reasoned connections that need verification._