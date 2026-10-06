# Graph Report - Smart_Finance_Manager  (2026-10-05)

## Corpus Check
- 14 files · ~35,302 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 159 nodes · 254 edges · 12 communities (10 shown, 2 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dc59a7a0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- exceptions.py
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- 2. Engineering Incident & Lessons Learned (Interview Case Study)
- Expense
- FinancialRecord
- expense.py
- Income
- .test_cannot_instantiate_abstract_base_class

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 24 edges
2. `Income` - 18 edges
3. `Expense` - 14 edges
4. `DomainValidationError` - 13 edges
5. `TestFinancialRecordValidation` - 11 edges
6. `FinancialRecord` - 8 edges
7. `User` - 7 edges
8. `Detailed Class Specifications` - 6 edges
9. `Smart Finance Manager` - 6 edges
10. `SmartFinanceError` - 5 edges

## Surprising Connections (you probably didn't know these)
- ``entities/`` --references--> `FinancialRecord`  [INFERRED]
  Docs/Architecture.md → src/logic/entities/financial_record.py
- ``Expense` *(Derived from FinancialRecord)*` --references--> `Expense`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/expense.py
- `Architectural Notes` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- `Implementation & Mapping Guidelines` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- `Main Classes` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (12 total, 2 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "exceptions.py"
Cohesion: 0.20
Nodes (9): Exception, Base Exceptions for Smart Finance Manager, Base exception for all domain and application errors., SmartFinanceError, Smoke test to verify that the testing environment, test runner, and project…, Verify that pytest is functioning properly., Verify that domain exceptions in src can be imported and instantiated., test_smoke_domain_exceptions_import() (+1 more)

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Detailed Class Specifications"
Cohesion: 0.11
Nodes (18): 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, 5. Application Services & Utilities, `Category`, `Contribution`, Detailed Class Specifications, `ExcelExporter` *(Service / Export Utility)* (+10 more)

### Community 7 - "2. Engineering Incident & Lessons Learned (Interview Case Study)"
Cohesion: 0.25
Nodes (7): 1. Branch Strategy Overview, 2. Engineering Incident & Lessons Learned (Interview Case Study), 3. Key Takeaways for Technical Interviews, Corrective Action Taken, Git Workflow & Branching Strategy Guidelines, Technical Analysis & Root Cause, The Scenario

### Community 8 - "Expense"
Cohesion: 0.31
Nodes (8): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes, Expense, Concrete financial record representing an expense (negative cash flow).…

### Community 9 - "FinancialRecord"
Cohesion: 0.16
Nodes (16): ABC, 1. Core Domain Entities & Inheritance, `Expense` *(Derived from FinancialRecord)*, `FinancialRecord` *(Abstract Base Class)*, `Income` *(Derived from FinancialRecord)*, Key Methods:, DomainValidationError, Raised when an entity or business invariant validation fails. (+8 more)

### Community 11 - "expense.py"
Cohesion: 0.15
Nodes (10): logic_entities_expense, logic_entities_financial_record, logic_entities_income, Decimal, Expense Entity Module. Specializes FinancialRecord for outgoing monetary…, Return negative signed amount representing money outflow., Decimal, Income Entity Module. Specializes FinancialRecord for incoming monetary… (+2 more)

### Community 16 - "Income"
Cohesion: 0.12
Nodes (20): decimal, fixture, logic_entities, parametrize, pytest, Income, Concrete financial record representing an income (positive cash flow). Inherits…, sys (+12 more)

### Community 17 - ".test_cannot_instantiate_abstract_base_class"
Cohesion: 0.50
Nodes (3): Tests ensuring FinancialRecord behaves as an abstract base class., FinancialRecord is abstract and cannot be instantiated directly., TestFinancialRecordABC

## Knowledge Gaps
- **32 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+27 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 70 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `FinancialRecord` to `Architecture.md`, `Expense`, `expense.py`, `Income`, `.test_cannot_instantiate_abstract_base_class`?**
  _High betweenness centrality (0.319) - this node is a cross-community bridge._
- **Why does `Detailed Class Specifications` connect `Detailed Class Specifications` to `Expense`, `FinancialRecord`?**
  _High betweenness centrality (0.161) - this node is a cross-community bridge._
- **Why does `Income` connect `Income` to `Expense`, `FinancialRecord`, `expense.py`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `FinancialRecord` (e.g. with ``entities/`` and `Architectural Notes`) actually correct?**
  _`FinancialRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `Income` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Income` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Expense` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Expense` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _32 weakly-connected nodes found - possible documentation gaps or missing edges._