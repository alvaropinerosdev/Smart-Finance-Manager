# Git Workflow & Branching Strategy Guidelines

## 1. Branch Strategy Overview

Smart Finance Manager follows a structured **Release & Feature Branching Workflow** designed to ensure environment isolation and stability:

```text
main (Production / Stable)
  ▲
  │ (Only merged when v1 is completely validated and ready for release)
  │
v1 (Active Development / Version 1 Integration)
  ▲                     ▲
  │ (PR: base = v1)      │ (PR: base = v1)
chore/*               feature/*
```

- **`main`**: Represents production-ready, stable releases. It remains locked and unchanged throughout daily development sprints.
- **`v1`**: Central development integration branch for Version 1. All sprint tasks and features integrate here.
- **`feature/*` / `chore/*`**: Short-lived branches created off `v1` and merged back into `v1` via Pull Requests.

---

## 2. Engineering Incident & Lessons Learned (Interview Case Study)

### The Scenario
During the Day 0 setup of Sprint 2, a Pull Request (`chore/setup-test-environment`) was merged. Because GitHub's repository settings defaulted the target base branch to `main`, the PR merged directly into `main` rather than `v1`. Subsequently, another PR was opened from `v1` into `main`, synchronizing both branches prematurely.

### Technical Analysis & Root Cause
1. **GitHub UI Default Target**: When creating a PR on a repository where `main` is the default branch, GitHub automatically selects `base: main` unless explicitly overridden to `base: v1`.
2. **Loss of Branch Isolation**: Merging development and setup iterations directly into `main` breaks the separation between stable releases and in-progress development, effectively treating `main` as a working branch.

### Corrective Action Taken
1. Re-aligned `v1` with the changes to preserve development continuity.
2. Formally locked `main` from receiving any daily sprint commits.
3. Established a strict rule: all future feature and chore PRs must explicitly designate `base: v1`.
4. `main` will only be updated via a single, audited Release PR once Version 1 domain logic, persistence, and end-to-end tests are 100% complete.

---

## 3. Key Takeaways for Technical Interviews

When discussing this experience in technical interviews:

- **Branch Protection & Release Maturity**: Demonstrates understanding that `main` must always represent production stability. Incomplete sprint tasks or ongoing feature work should never contaminate the production line.
- **Root Cause Analysis (RCA)**: Shows the ability to identify why an operational divergence happened (GitHub default PR target behavior) and how to implement a systematic protocol to prevent regression.
- **Real-World CI/CD Awareness**: Reflects practical knowledge of modern software engineering practices, Git Flow, branch permissions, and code review lifecycles.

---

## 4. Strict Sub-Branch Integration Protocol (Preventing Involuntary Merges to `main`)

### Mandatory Rule: `v1` Exclusivity
When completing and deleting any sub-branch (`feature/*` or `chore/*`), **all changes must integrate exclusively into `v1`**. 
Changes must **NEVER** land in `main` and `v1` simultaneously during daily development sprints.

### Why this Error Recurs:
1. **GitHub Default Branch Trap**: In GitHub repository settings, `main` is designated as the default branch. Consequently, whenever a new Pull Request is opened, GitHub's UI automatically pre-selects `base: main`.
2. If the author clicks "Create pull request" and merges without manually overriding the base selector, the code merges directly into production (`main`), polluting the release baseline.

### Operational Checklist to Prevent Recurrence:
1. **Manual Inspection**: Before confirming PR creation, verify the branch target badge reads:
   $$\text{base: } \mathbf{v1} \longleftarrow \text{compare: } \mathbf{feature/*}$$
2. **Permanent Preventive Solution (GitHub Setting)**:
   In GitHub Repository Settings $\rightarrow$ **Branches** $\rightarrow$ **Default branch**, switch the default branch to `v1` for the duration of Version 1 development. This forces all GitHub PR forms and comparison banners to target `v1` automatically.
3. **Local Audit Rule**:
   After deleting a sub-branch, run:
   ```bash
   git fetch origin
   git log origin/v1 -n 3 --oneline
   git log origin/main -n 3 --oneline
   ```
   Ensure that only `origin/v1` advanced, while `origin/main` remained unchanged.
