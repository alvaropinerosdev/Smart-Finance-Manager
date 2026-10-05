# Graph Report - Smart_Finance_Manager  (2026-10-04)

## Corpus Check
- 16 files · ~34,141 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .ini 1)

## Summary
- 94 nodes · 89 edges · 17 communities (8 shown, 9 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `db844cc5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- SmartFinanceError
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- 2. Engineering Incident & Lessons Learned (Interview Case Study)
- Class Diagram Design
- 5. Application Services & Utilities
- 1. Core Domain Entities & Inheritance

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 8 edges
2. `User` - 7 edges
3. `Detailed Class Specifications` - 6 edges
4. `Smart Finance Manager` - 6 edges
5. `SmartFinanceError` - 5 edges
6. `DomainValidationError` - 4 edges
7. `test_smoke_domain_exceptions_import()` - 4 edges
8. `Smart Finance Manager — System Architecture` - 4 edges
9. `3. Components` - 4 edges
10. `4. Intermediaries` - 4 edges

## Surprising Connections (you probably didn't know these)
- `User` --implements--> `PostgreSQL`  [INFERRED]
  Docs/DataBase.md → README.md
- `test_smoke_domain_exceptions_import()` --uses--> `SmartFinanceError`  [INFERRED]
  tests/unit/test_smoke.py → src/exceptions.py
- `test_smoke_domain_exceptions_import()` --uses--> `DomainValidationError`  [INFERRED]
  tests/unit/test_smoke.py → src/exceptions.py
- `Database UML` --references--> `FinancialRecord`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md
- `Console Scope V1` --conceptually_related_to--> `FinancialRecord`  [INFERRED]
  README.md → Docs/DataBase.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (17 total, 9 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "SmartFinanceError"
Cohesion: 0.19
Nodes (11): Exception, DomainValidationError, Base Exceptions for Smart Finance Manager, Raised when an entity or business invariant validation fails., Base exception for all domain and application errors., SmartFinanceError, Smoke test to verify that the testing environment, test runner, and project…, Verify that pytest is functioning properly. (+3 more)

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Detailed Class Specifications"
Cohesion: 0.15
Nodes (13): 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, `Category`, `Contribution`, Detailed Class Specifications, `FinancialReport`, `Goal` (+5 more)

### Community 7 - "2. Engineering Incident & Lessons Learned (Interview Case Study)"
Cohesion: 0.25
Nodes (7): 1. Branch Strategy Overview, 2. Engineering Incident & Lessons Learned (Interview Case Study), 3. Key Takeaways for Technical Interviews, Corrective Action Taken, Git Workflow & Branching Strategy Guidelines, Technical Analysis & Root Cause, The Scenario

### Community 8 - "Class Diagram Design"
Cohesion: 0.29
Nodes (6): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes

### Community 9 - "5. Application Services & Utilities"
Cohesion: 0.40
Nodes (5): 5. Application Services & Utilities, `ExcelExporter` *(Service / Export Utility)*, Key Responsibilities:, Key Responsibilities & Methods:, `Statistics` *(Service / Calculation Component)*

### Community 16 - "1. Core Domain Entities & Inheritance"
Cohesion: 0.40
Nodes (5): 1. Core Domain Entities & Inheritance, `Expense` *(Derived from FinancialRecord)*, `FinancialRecord` *(Abstract Base Class)*, `Income` *(Derived from FinancialRecord)*, Key Methods:

## Knowledge Gaps
- **39 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+34 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 59 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Detailed Class Specifications` connect `Detailed Class Specifications` to `Class Diagram Design`, `1. Core Domain Entities & Inheritance`, `5. Application Services & Utilities`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Why does `Class Diagram Design` connect `Class Diagram Design` to `Detailed Class Specifications`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `1. Core Domain Entities & Inheritance` connect `1. Core Domain Entities & Inheritance` to `Detailed Class Specifications`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `User` (e.g. with `PostgreSQL` and `Smart Finance Manager`) actually correct?**
  _`User` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _39 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Architecture.md` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._