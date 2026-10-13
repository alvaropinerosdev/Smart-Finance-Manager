# Graph Report - Smart_Finance_Manager  (2026-10-05)

## Corpus Check
- 14 files · ~35,512 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 163 nodes · 258 edges · 11 communities (9 shown, 2 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `06f65290`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- test_smoke.py
- 5. Application Services & Utilities
- Architecture.md
- Expense
- rules/graphify.md
- workflows/graphify.md
- Git Workflow & Branching Strategy Guidelines
- FinancialRecord
- expense.py
- Income

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
- `Architectural Notes` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- ``Expense` *(Derived from FinancialRecord)*` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- ``FinancialRecord` *(Abstract Base Class)*` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py
- `Implementation & Mapping Guidelines` --references--> `FinancialRecord`  [INFERRED]
  Docs/ClassDiagram.md → src/logic/entities/financial_record.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (11 total, 2 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "test_smoke.py"
Cohesion: 0.33
Nodes (5): Smoke test to verify that the testing environment, test runner, and project…, Verify that pytest is functioning properly., Verify that domain exceptions in src can be imported and instantiated., test_smoke_domain_exceptions_import(), test_smoke_environment()

### Community 2 - "5. Application Services & Utilities"
Cohesion: 0.40
Nodes (5): 5. Application Services & Utilities, `ExcelExporter` *(Service / Export Utility)*, Key Responsibilities:, Key Responsibilities & Methods:, `Statistics` *(Service / Calculation Component)*

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Expense"
Cohesion: 0.09
Nodes (26): 1. Core Domain Entities & Inheritance, 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, Architectural Notes, `Category`, Class Diagram Design, Class Relationships & Associations (+18 more)

### Community 7 - "Git Workflow & Branching Strategy Guidelines"
Cohesion: 0.17
Nodes (11): 1. Branch Strategy Overview, 2. Engineering Incident & Lessons Learned (Interview Case Study), 3. Key Takeaways for Technical Interviews, 4. Strict Sub-Branch Integration Protocol (Preventing Involuntary Merges to `main`), Corrective Action Taken, Git Workflow & Branching Strategy Guidelines, Mandatory Rule: `v1` Exclusivity, Operational Checklist to Prevent Recurrence: (+3 more)

### Community 9 - "FinancialRecord"
Cohesion: 0.16
Nodes (15): ABC, Exception, DomainValidationError, Base Exceptions for Smart Finance Manager, Raised when an entity or business invariant validation fails., Base exception for all domain and application errors., SmartFinanceError, FinancialRecord (+7 more)

### Community 11 - "expense.py"
Cohesion: 0.15
Nodes (10): logic_entities_expense, logic_entities_financial_record, logic_entities_income, Decimal, Expense Entity Module. Specializes FinancialRecord for outgoing monetary…, Return negative signed amount representing money outflow., Decimal, Income Entity Module. Specializes FinancialRecord for incoming monetary… (+2 more)

### Community 16 - "Income"
Cohesion: 0.11
Nodes (23): decimal, fixture, logic_entities, parametrize, pytest, Income, Concrete financial record representing an income (positive cash flow). Inherits…, sys (+15 more)

## Knowledge Gaps
- **35 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+30 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 73 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `FinancialRecord` to `expense.py`, `Income`, `Architecture.md`, `Expense`?**
  _High betweenness centrality (0.303) - this node is a cross-community bridge._
- **Why does `Detailed Class Specifications` connect `Expense` to `5. Application Services & Utilities`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Why does `Income` connect `Income` to `FinancialRecord`, `expense.py`, `Expense`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `FinancialRecord` (e.g. with ``entities/`` and `Architectural Notes`) actually correct?**
  _`FinancialRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `Income` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Income` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Expense` (e.g. with `Architectural Notes` and `Class Relationships & Associations`) actually correct?**
  _`Expense` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _35 weakly-connected nodes found - possible documentation gaps or missing edges._