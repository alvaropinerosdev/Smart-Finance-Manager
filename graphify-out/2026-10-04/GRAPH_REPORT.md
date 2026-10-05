# Graph Report - Smart_Finance_Manager  (2026-10-03)

## Corpus Check
- 14 files · ~33,648 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 80 nodes · 74 edges · 16 communities (7 shown, 9 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fd1193a3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- SmartFinanceError
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- 1. Core Domain Entities & Inheritance
- Class Diagram Design
- 5. Application Services & Utilities

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 8 edges
2. `User` - 7 edges
3. `Detailed Class Specifications` - 6 edges
4. `Smart Finance Manager` - 6 edges
5. `SmartFinanceError` - 4 edges
6. `Smart Finance Manager — System Architecture` - 4 edges
7. `3. Components` - 4 edges
8. `4. Intermediaries` - 4 edges
9. `Class Diagram Design` - 4 edges
10. `Introduction` - 4 edges

## Surprising Connections (you probably didn't know these)
- `User` --implements--> `PostgreSQL`  [INFERRED]
  Docs/DataBase.md → README.md
- `Database UML` --references--> `FinancialRecord`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md
- `Console Scope V1` --conceptually_related_to--> `FinancialRecord`  [INFERRED]
  README.md → Docs/DataBase.md
- `Database UML` --references--> `User`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md
- `Smart Finance Manager` --references--> `User`  [INFERRED]
  README.md → Docs/DataBase.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (16 total, 9 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.15
Nodes (18): Category, Contribution, Expense, FinancialRecord, FinancialReport, Goal, Income, ModificationHistory (+10 more)

### Community 1 - "SmartFinanceError"
Cohesion: 0.33
Nodes (6): Exception, DomainValidationError, Base Exceptions for Smart Finance Manager, Raised when an entity or business invariant validation fails., Base exception for all domain and application errors., SmartFinanceError

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Detailed Class Specifications"
Cohesion: 0.15
Nodes (13): 2. User & Classification Domain, 3. Goals & Savings Domain, 4. Reporting & Audit Domain, `Category`, `Contribution`, Detailed Class Specifications, `FinancialReport`, `Goal` (+5 more)

### Community 7 - "1. Core Domain Entities & Inheritance"
Cohesion: 0.40
Nodes (5): 1. Core Domain Entities & Inheritance, `Expense` *(Derived from FinancialRecord)*, `FinancialRecord` *(Abstract Base Class)*, `Income` *(Derived from FinancialRecord)*, Key Methods:

### Community 8 - "Class Diagram Design"
Cohesion: 0.29
Nodes (6): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes

### Community 9 - "5. Application Services & Utilities"
Cohesion: 0.40
Nodes (5): 5. Application Services & Utilities, `ExcelExporter` *(Service / Export Utility)*, Key Responsibilities:, Key Responsibilities & Methods:, `Statistics` *(Service / Calculation Component)*

## Knowledge Gaps
- **34 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+29 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 50 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Detailed Class Specifications` connect `Detailed Class Specifications` to `Class Diagram Design`, `5. Application Services & Utilities`, `1. Core Domain Entities & Inheritance`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Why does `Class Diagram Design` connect `Class Diagram Design` to `Detailed Class Specifications`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `1. Core Domain Entities & Inheritance` connect `1. Core Domain Entities & Inheritance` to `Detailed Class Specifications`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `User` (e.g. with `PostgreSQL` and `Smart Finance Manager`) actually correct?**
  _`User` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _34 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Architecture.md` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._