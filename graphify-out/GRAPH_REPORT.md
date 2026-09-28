# Graph Report - Smart_Finance_Manager  (2026-09-28)

## Corpus Check
- Corpus is ~21,916 words - fits in a single context window. You may not need a graph.

## Summary
- 18 nodes · 23 edges · 3 communities
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.9)
- Token cost: 1,500 input · 900 output

## Community Hubs (Navigation)
- Core Financial Domain
- Audit & History
- Architecture & Stack

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 8 edges
2. `User` - 7 edges
3. `Smart Finance Manager` - 6 edges
4. `Goal` - 4 edges
5. `Console Scope V1` - 3 edges
6. `ModificationHistory` - 3 edges
7. `PostgreSQL` - 2 edges
8. `Category` - 2 edges
9. `Database UML` - 2 edges
10. `Python` - 1 edges

## Surprising Connections (you probably didn't know these)
- `User` --implements--> `PostgreSQL`  [INFERRED]
  Docs/DataBase.md → README.md
- `Smart Finance Manager` --references--> `User`  [INFERRED]
  README.md → Docs/DataBase.md
- `Console Scope V1` --conceptually_related_to--> `FinancialRecord`  [INFERRED]
  README.md → Docs/DataBase.md
- `Console Scope V1` --conceptually_related_to--> `Goal`  [INFERRED]
  README.md → Docs/DataBase.md
- `Database UML` --references--> `User`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (3 total, 0 thin omitted)

### Community 0 - "Core Financial Domain"
Cohesion: 0.32
Nodes (8): Category, Expense, FinancialRecord, FinancialReport, Income, Soft Delete, User, Database UML

### Community 1 - "Audit & History"
Cohesion: 0.40
Nodes (5): Contribution, Goal, ModificationHistory, Polymorphic History, Console Scope V1

### Community 2 - "Architecture & Stack"
Cohesion: 0.40
Nodes (5): Smart Finance Manager, Docker, PostgreSQL, Pytest, Python

## Knowledge Gaps
- **7 isolated node(s):** `Python`, `Docker`, `Pytest`, `Income`, `Expense` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `Core Financial Domain` to `Audit & History`?**
  _High betweenness centrality (0.442) - this node is a cross-community bridge._
- **Why does `User` connect `Core Financial Domain` to `Audit & History`, `Architecture & Stack`?**
  _High betweenness centrality (0.420) - this node is a cross-community bridge._
- **Why does `Smart Finance Manager` connect `Architecture & Stack` to `Core Financial Domain`, `Audit & History`?**
  _High betweenness centrality (0.343) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `User` (e.g. with `PostgreSQL` and `Smart Finance Manager`) actually correct?**
  _`User` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Console Scope V1` (e.g. with `FinancialRecord` and `Goal`) actually correct?**
  _`Console Scope V1` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Python`, `Docker`, `Pytest` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._