# SMART_FINANCE_MANAGER

## Overview

SMART_FINANCE_MANAGER is a personal finance management application designed to help users track their income and expenses, understand their financial behavior, set financial goals, and make informed decisions based on their financial data.

The project focuses on making personal financial management more accessible, interactive, and consistent by reducing the effort required to record and understand financial activity.

## Problem Statement

Nowadays, many people struggle to properly manage their personal finances due to a lack of time, organization, and consistency when tracking their income and expenses.

Managing finances through traditional methods, such as spreadsheets or manual records, requires users to dedicate time to an activity that does not always provide an immediate sense of value or progress. As a result, financial tracking is often postponed or abandoned.

This situation becomes even more complex for people who do not have a fixed or continuous income, as their earnings can vary significantly from day to day or month to month. This variability makes it difficult to accurately determine how much money is available, identify where financial resources are being spent, and evaluate whether current financial decisions are contributing to the achievement of personal goals.

As a consequence, the lack of consistent financial tracking can lead to a limited understanding of spending habits, difficulties in planning the use of available money, and a greater likelihood of making financial decisions without sufficient information.

Furthermore, when financial tracking is perceived as a repetitive and unappealing task, people may become less motivated to maintain financial management habits over time.

Therefore, there is a problem related to the difficulty of maintaining consistent personal financial management, particularly for people with variable income, due to the time and effort required to record, understand, and analyze their financial behavior.

## Solution

SMART_FINANCE_MANAGER aims to provide a simple and interactive way to manage personal finances by reducing the effort required to record, understand, and analyze financial activity.

The application will allow users to record their income and expenses, visualize their financial activity, monitor their progress toward financial goals, and use the resulting data to support better financial decision-making.

The project also aims to make financial management more engaging by providing clear visualizations and an interactive experience, encouraging users to maintain consistent financial tracking habits over time.

## Core Features

- Income and expense tracking
- Financial activity visualization
- Spending and income statistics
- Financial goal management
- Financial data analysis
- AI-assisted financial recommendations
- Easy personal finance management
- Financial data export to Excel
- Cloud-based access to financial information

## Technologies

### Core Technologies

- **Python** — Main programming language used to develop the application.
- **PostgreSQL** — Relational database used to store and manage financial data.
- **Git** — Version control system used to track changes throughout the development process.
- **GitHub** — Platform used to host the repository and manage the project's source code.

### Testing

- **pytest** — Testing framework used to verify application behavior and ensure code reliability.

### Development & Deployment

- **Docker** — Used to create consistent and reproducible development environments.

### AI-Assisted Development

AI tools are used throughout the development process to assist with code generation and implementation. Generated code is reviewed, tested, and corrected manually to ensure that it meets the project's requirements and quality standards.

## Learning Objectives

This project is designed to strengthen practical software development skills through the design, implementation, testing, and deployment of a complete application.

By developing SMART_FINANCE_MANAGER, I aim to gain experience in:

- **Python development** — Strengthen programming skills and apply software design principles in a real project.
- **Object-Oriented Programming** — Design and organize application components using classes, objects, and appropriate abstractions.
- **Database management** — Learn how to design, connect, query, and manage a PostgreSQL database from Python.
- **Software architecture** — Understand how to structure a maintainable application and separate its responsibilities into appropriate components.
- **Scalability and maintainability** — Learn how to design the project structure and components so the application can grow and incorporate new features without requiring major structural changes.
- **Documentation** — Learn how to create clear and organized technical documentation that makes the project easier to understand, maintain, contribute to, and scale in the future.
- **Git and GitHub workflows** — Practice version control, meaningful commits, branching, repository management, and project history.
- **Testing** — Learn how to write and maintain automated tests using pytest.
- **Docker** — Learn how to containerize the application and create reproducible development environments.
- **Data analysis and visualization** — Learn how to transform financial data into useful statistics and visualizations.
- **API development** — Gain practical experience in building and consuming application interfaces as the project evolves.
- **AI-assisted development** — Learn how to effectively use AI tools for code generation while reviewing, testing, debugging, and improving the generated code.
- **Software development practices** — Improve problem-solving, debugging, documentation, code organization, and iterative development skills.

## Requirements

The following requirements define the conditions that SMART_FINANCE_MANAGER must satisfy during its development.

### Functional Requirements

The system must:

- Allow users to create, modify, and delete their financial records.
- Maintain a consistent relationship between financial records and their corresponding categories.
- Calculate financial balances and summaries from the stored data.
- Preserve historical financial information for subsequent analysis.
- Allow users to define financial goals and maintain their progress over time.
- Generate financial information in a format suitable for external analysis or storage.
- Use stored financial data as the basis for automated analysis and recommendations.

### Non-Functional Requirements

The system must:

- Maintain data consistency and integrity during normal application operations.
- Protect stored financial information against unauthorized access.
- Provide predictable and reliable behavior when processing user data.
- Be structured so that individual components can be modified or extended without unnecessary changes to unrelated components.
- Include automated tests for critical application behavior.
- Provide reproducible development and execution environments.
- Handle application errors without compromising stored financial data.
- Maintain sufficient documentation to support installation, development, and future maintenance.

## Project Scope

The project scope defines the boundaries of version 1.0 of SMART_FINANCE_MANAGER. This version is intended as a foundational development stage focused on implementing and validating the core functionality of the application.

### Version 1.0 Scope

Version 1.0 will be a console-based application focused on the fundamental management and processing of personal financial information.

The initial version will include:

- Creation, modification, and deletion of financial records.

- Storage and retrieval of financial information using PostgreSQL.

- Categorization of income and expenses.

- Balance and basic financial calculations.

- Historical financial data management.

- Basic financial statistics and analysis.

- Creation and tracking of financial goals.

- Export of financial data to Excel.

- Automated testing of core application functionality.

- Docker-based development environment.

- Modification History.

- Modular project architecture designed to support future development.

- Makes goals.

- Financial Reports.

Version 1.0 will be developed as a console-based application and will not include a graphical user interface or web interface. The application will be designed to run in a controlled environment and may be deployed on other computers for development, testing, or personal use.

This version is intended for development, learning, testing, and validation of the application's core architecture and functionality. It is not intended to be released as a commercial product or deployed for public use.

### Outside the Scope of Version 1.0

The following are intentionally excluded from the initial version:

- Graphical user interfaces.

- Web interfaces.

- Mobile applications.

- AI-assisted financial analysis or recommendations.

- Direct integration with bank accounts or financial institutions.

- Automatic retrieval of transactions from external financial services.

- Execution of payments, transfers, investments, or other financial transactions.

- Professional financial advisory services.

- Tax filing or automatic tax submission.

- Credit approval or lending services.

- Real-time financial market operations.

- Multi-user or shared financial management.

- Public or commercial deployment.

### Future Scope

Future versions may expand the application with:

- Graphical or web-based interfaces.

- AI-assisted financial analysis and recommendations.

- Bank and financial institution integrations.

- Automatic transaction synchronization.

- Advanced budgeting and financial forecasting.

- Automated notifications and reminders.

- Mobile applications.

- Multi-user financial management.

- Additional financial services and integrations.

The scope may evolve as the project progresses based on technical feasibility, development experience, and the requirements identified during subsequent versions.