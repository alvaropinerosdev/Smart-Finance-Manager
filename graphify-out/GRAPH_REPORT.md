# Graph Report - Smart_Finance_Manager  (2026-09-29)

## Corpus Check
- 5 files · ~24,013 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 36 nodes · 38 edges · 7 communities (5 shown, 2 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ec282ee6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FinancialRecord
- Goal
- Smart Finance Manager
- Architecture.md
- 3. Components
- rules/graphify.md
- workflows/graphify.md

## God Nodes (most connected - your core abstractions)
1. `FinancialRecord` - 8 edges
2. `User` - 7 edges
3. `Smart Finance Manager` - 6 edges
4. `Smart Finance Manager — System Architecture` - 4 edges
5. `3. Components` - 4 edges
6. `4. Intermediaries` - 4 edges
7. `Goal` - 4 edges
8. `ModificationHistory` - 3 edges
9. `Console Scope V1` - 3 edges
10. `Category` - 2 edges

## Surprising Connections (you probably didn't know these)
- `User` --implements--> `PostgreSQL`  [INFERRED]
  Docs/DataBase.md → README.md
- `Console Scope V1` --conceptually_related_to--> `FinancialRecord`  [INFERRED]
  README.md → Docs/DataBase.md
- `Smart Finance Manager` --references--> `User`  [INFERRED]
  README.md → Docs/DataBase.md
- `Database UML` --references--> `FinancialRecord`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md
- `Database UML` --references--> `User`  [EXTRACTED]
  Docs/Images/database_uml.png → Docs/DataBase.md

## Hyperedges (group relationships)
- **Core Domain Entities** — docs_db_user, docs_db_financialrecord, docs_db_category, docs_db_goal [EXTRACTED 1.00]
- **Audit & History System** — docs_db_modificationhistory, docs_db_polymorphic_history, docs_db_soft_delete [INFERRED 0.95]

## Communities (7 total, 2 thin omitted)

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
Cohesion: 0.29
Nodes (6): 4.1 Validators, 4.2 Mappers, 4.3 Router, 4. Intermediaries, 5. Services, 6. General Flow

### Community 4 - "3. Components"
Cohesion: 0.29
Nodes (7): 1. Architecture Objective, 2. Main Structure, 3.1 Logic, 3. Components, `entities/`, `rules/`, Smart Finance Manager — System Architecture

## Knowledge Gaps
- **19 isolated node(s):** `graphify`, `Workflow: graphify`, `1. Architecture Objective`, `2. Main Structure`, `3.1 Logic` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 23 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FinancialRecord` connect `FinancialRecord` to `Goal`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `User` connect `FinancialRecord` to `Goal`, `Smart Finance Manager`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Why does `Smart Finance Manager — System Architecture` connect `3. Components` to `Architecture.md`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `User` (e.g. with `PostgreSQL` and `Smart Finance Manager`) actually correct?**
  _`User` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. Architecture Objective` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._