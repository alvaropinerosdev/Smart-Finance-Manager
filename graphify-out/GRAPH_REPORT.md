# Graph Report - Smart_Finance_Manager  (2026-10-01)

## Corpus Check
- 6 files · ~33,617 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 66 nodes · 67 edges · 11 communities (9 shown, 2 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7d86a02c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- Goal
- Smart Finance Manager
- Architecture.md
- Detailed Class Specifications
- rules/graphify.md
- workflows/graphify.md
- 1. Core Domain Entities & Inheritance
- Class Diagram Design
- 5. Application Services & Utilities
- 4. Reporting & Audit Domain

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 8 edges
2. `User` - 7 edges
3. `Detailed Class Specifications` - 6 edges
4. `Smart Finance Manager` - 6 edges
5. `Smart Finance Manager — System Architecture` - 4 edges
6. `3. Components` - 4 edges
7. `4. Intermediaries` - 4 edges
8. `Class Diagram Design` - 4 edges
9. `Introduction` - 4 edges
10. `1. Core Domain Entities & Inheritance` - 4 edges

## Surprising Connections (you probably didn't know these)
- `User` --implements--> `PostgreSQL`  [INFERRED]
  Docs/DataBase.md → README.md
- `Smart Finance Manager` --references--> `User`  [INFERRED]
  README.md → Docs/DataBase.md
- `Console Scope V1` --conceptually_related_to--> `FinancialRecord`  [INFERRED]
  README.md → Docs/DataBase.md
- `Database UML` --references--> `User`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md
- `Database UML` --references--> `FinancialRecord`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (11 total, 2 thin omitted)

### Community 0 - "FinancialRecord"
Cohesion: 0.32
Nodes (8): Category, Expense, FinancialRecord, FinancialReport, Income, Soft Delete, User, Database UML

### Community 1 - "Goal"
Cohesion: 0.40
Nodes (5): Contribution, Goal, ModificationHistory, Polymorphic History, Console Scope V1

### Community 2 - "Smart Finance Manager"
Cohesion: 0.40
Nodes (5): Smart Finance Manager, Docker, PostgreSQL, Pytest, Python

### Community 3 - "Architecture.md"
Cohesion: 0.14
Nodes (13): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries (+5 more)

### Community 4 - "Detailed Class Specifications"
Cohesion: 0.22
Nodes (9): 2. User & Classification Domain, 3. Goals & Savings Domain, `Category`, `Contribution`, Detailed Class Specifications, `Goal`, Key Methods:, Key Methods: (+1 more)

### Community 7 - "1. Core Domain Entities & Inheritance"
Cohesion: 0.40
Nodes (5): 1. Core Domain Entities & Inheritance, `Expense` *(Derived from FinancialRecord)*, `FinancialRecord` *(Abstract Base Class)*, `Income` *(Derived from FinancialRecord)*, Key Methods:

### Community 8 - "Class Diagram Design"
Cohesion: 0.29
Nodes (6): Architectural Notes, Class Diagram Design, Class Relationships & Associations, Implementation & Mapping Guidelines, Introduction, Main Classes

### Community 9 - "5. Application Services & Utilities"
Cohesion: 0.40
Nodes (5): 5. Application Services & Utilities, `ExcelExporter` *(Service / Export Utility)*, Key Responsibilities:, Key Responsibilities & Methods:, `Statistics` *(Service / Calculation Component)*

### Community 10 - "4. Reporting & Audit Domain"
Cohesion: 0.50
Nodes (4): 4. Reporting & Audit Domain, `FinancialReport`, Key Methods:, `ModificationHistory`

## Knowledge Gaps
- **34 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+29 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 39 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Detailed Class Specifications` connect `Detailed Class Specifications` to `Class Diagram Design`, `5. Application Services & Utilities`, `4. Reporting & Audit Domain`, `1. Core Domain Entities & Inheritance`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **Why does `Class Diagram Design` connect `Class Diagram Design` to `Detailed Class Specifications`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Why does `1. Core Domain Entities & Inheritance` connect `1. Core Domain Entities & Inheritance` to `Detailed Class Specifications`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `User` (e.g. with `PostgreSQL` and `Smart Finance Manager`) actually correct?**
  _`User` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _34 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Architecture.md` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._