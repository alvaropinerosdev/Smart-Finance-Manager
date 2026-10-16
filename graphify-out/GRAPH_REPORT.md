# Graph Report - Smart_Finance_Manager  (2026-10-15)

## Corpus Check
- 17 files · ~37,407 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 247 nodes · 469 edges · 17 communities (10 shown, 7 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 78 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e18f510b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- test_smoke.py
- Category
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- Git Workflow & Branching Strategy Guidelines
- logic_entities_expense
- DomainValidationError
- logic_entities_income
- Expense
- User
- datetime
- uuid
- .signed_amount
- Income

## God Nodes (most connected - your core abstractions)
1. `Category` - 35 edges
2. `DomainValidationError` - 27 edges
3. `User` - 27 edges
4. `FinancialRecord` - 24 edges
5. `Income` - 18 edges
6. `Expense` - 14 edges
7. `TestFinancialRecordValidation` - 11 edges
8. `TestCategoryValidation` - 11 edges
9. `TestUserEntity` - 9 edges
10. `TestUserValidation` - 9 edges

## Surprising Connections (you probably didn't know these)
- ``entities/`` --references--> `FinancialRecord`  [INFERRED]
  Docs/Architecture.md → src/logic/entities/financial_record.py
- ``User`` --references--> `User`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/user.py
- `Architectural Notes` --references--> `Category`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/category.py
- ``Category`` --references--> `Category`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/category.py
- `Implementation & Mapping Guidelines` --references--> `Category`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/category.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (17 total, 7 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "test_smoke.py"
Cohesion: 0.33
Nodes (5): Smoke test to verify that the testing environment, test runner, and project…, Verify that pytest is functioning properly., Verify that domain exceptions in src can be imported and instantiated., test_smoke_domain_exceptions_import(), test_smoke_environment()

### Community 2 - "Category"
Cohesion: 0.11
Nodes (17): Category, Check whether this category accepts the given record type ('INCOME' or…, Domain entity representing transaction categories for financial classification., datetime, fixture, UUID, Unit tests for User and Category entities., Tests validating User domain invariants and error handling. (+9 more)

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Detailed Class Specifications"
Cohesion: 0.09
Nodes (23): 1. Core Domain Entities & Inheritance, 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, 5. Application Services & Utilities, `Category`, `Contribution`, Detailed Class Specifications (+15 more)

### Community 7 - "Git Workflow & Branching Strategy Guidelines"
Cohesion: 0.17
Nodes (11): 1. Branch Strategy Overview, 2. Engineering Incident & Lessons Learned (Interview Case Study), 3. Key Takeaways for Technical Interviews, 4. Strict Sub-Branch Integration Protocol (Preventing Involuntary Merges to `main`), Corrective Action Taken, Git Workflow & Branching Strategy Guidelines, Mandatory Rule: `v1` Exclusivity, Operational Checklist to Prevent Recurrence: (+3 more)

### Community 9 - "DomainValidationError"
Cohesion: 0.08
Nodes (24): ABC, Exception, logic_entities_financial_record, DomainValidationError, Base Exceptions for Smart Finance Manager, Raised when an entity or business invariant validation fails., Base exception for all domain and application errors., SmartFinanceError (+16 more)

### Community 11 - "Expense"
Cohesion: 0.14
Nodes (12): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes, Mark category as soft deleted and refresh timestamps., Return True if category is currently active (not soft deleted). (+4 more)

### Community 12 - "User"
Cohesion: 0.15
Nodes (7): datetime, UUID, Root domain entity representing registered system users. Acts as the logical…, Update the updated_at timestamp to the specified datetime or the current UTC…, User, Tests verifying User entity lifecycle and behavior., TestUserEntity

### Community 16 - "Income"
Cohesion: 0.11
Nodes (23): decimal, logic_entities, parametrize, pytest, Income, Concrete financial record representing an income (positive cash flow). Inherits…, sys, datetime (+15 more)

## Knowledge Gaps
- **34 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+29 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 89 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `DomainValidationError` to `Expense`, `Income`, `Architecture.md`, `Detailed Class Specifications`?**
  _High betweenness centrality (0.192) - this node is a cross-community bridge._
- **Why does `DomainValidationError` connect `DomainValidationError` to `Income`, `test_smoke.py`, `Category`, `User`?**
  _High betweenness centrality (0.183) - this node is a cross-community bridge._
- **Why does `Category` connect `Category` to `DomainValidationError`, `Expense`, `Detailed Class Specifications`?**
  _High betweenness centrality (0.168) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `Category` (e.g. with `Architectural Notes` and ``Category``) actually correct?**
  _`Category` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `DomainValidationError` (e.g. with `Category` and `FinancialRecord`) actually correct?**
  _`DomainValidationError` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `User` (e.g. with `Architectural Notes` and `Implementation & Mapping Guidelines`) actually correct?**
  _`User` has 17 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _34 weakly-connected nodes found - possible documentation gaps or missing edges._