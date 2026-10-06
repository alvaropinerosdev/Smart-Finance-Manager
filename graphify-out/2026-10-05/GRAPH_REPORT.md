# Graph Report - Smart_Finance_Manager  (2026-10-05)

## Corpus Check
- 19 files · ~34,713 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 129 nodes · 165 edges · 16 communities (8 shown, 8 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 30 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `93addf41`
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

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 20 edges
2. `DomainValidationError` - 11 edges
3. `Expense` - 9 edges
4. `Income` - 9 edges
5. `FinancialRecord` - 8 edges
6. `User` - 7 edges
7. `Detailed Class Specifications` - 6 edges
8. `Smart Finance Manager` - 6 edges
9. `SmartFinanceError` - 5 edges
10. `test_smoke_domain_exceptions_import()` - 4 edges

## Surprising Connections (you probably didn't know these)
- ``entities/`` --references--> `FinancialRecord`  [INFERRED]
  Docs/Architecture.md → src/logic/entities/financial_record.py
- ``Expense` *(Derived from FinancialRecord)*` --references--> `Expense`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/expense.py
- `Architectural Notes` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- ``Expense` *(Derived from FinancialRecord)*` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- ``FinancialRecord` *(Abstract Base Class)*` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (16 total, 8 thin omitted)

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
Cohesion: 0.09
Nodes (23): 1. Core Domain Entities & Inheritance, 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, 5. Application Services & Utilities, `Category`, `Contribution`, Detailed Class Specifications (+15 more)

### Community 7 - "2. Engineering Incident & Lessons Learned (Interview Case Study)"
Cohesion: 0.25
Nodes (7): 1. Branch Strategy Overview, 2. Engineering Incident & Lessons Learned (Interview Case Study), 3. Key Takeaways for Technical Interviews, Corrective Action Taken, Git Workflow & Branching Strategy Guidelines, Technical Analysis & Root Cause, The Scenario

### Community 8 - "Expense"
Cohesion: 0.18
Nodes (13): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes, Expense, Concrete financial record representing an expense (negative cash flow).… (+5 more)

### Community 9 - "FinancialRecord"
Cohesion: 0.22
Nodes (11): ABC, datetime, DomainValidationError, Raised when an entity or business invariant validation fails., FinancialRecord, Decimal, FinancialRecord Entity Module. Defines the abstract base class for all monetary…, Return the signed monetary impact of the transaction. Must be implemented by… (+3 more)

### Community 11 - "expense.py"
Cohesion: 0.20
Nodes (7): logic_entities_expense, logic_entities_financial_record, logic_entities_income, Decimal, Expense Entity Module. Specializes FinancialRecord for outgoing monetary…, Return negative signed amount representing money outflow., Entities package exposing domain models for Smart Finance Manager.

## Knowledge Gaps
- **32 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+27 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 64 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `FinancialRecord` to `Expense`, `Architecture.md`, `Detailed Class Specifications`?**
  _High betweenness centrality (0.331) - this node is a cross-community bridge._
- **Why does `Detailed Class Specifications` connect `Detailed Class Specifications` to `Expense`?**
  _High betweenness centrality (0.171) - this node is a cross-community bridge._
- **Why does ``entities/`` connect `Architecture.md` to `FinancialRecord`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `FinancialRecord` (e.g. with ``entities/`` and `Architectural Notes`) actually correct?**
  _`FinancialRecord` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `DomainValidationError` (e.g. with `FinancialRecord` and `.__init__()`) actually correct?**
  _`DomainValidationError` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Expense` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Expense` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Income` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Income` has 5 INFERRED edges - model-reasoned connections that need verification._