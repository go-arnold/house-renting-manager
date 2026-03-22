# House Renting Manager

## Project Description

House Renting Manager is a simple **Python CLI application** to manage houses for rent.
It allows users to **add houses, view houses, rent and release houses**, search by location or price, and view only available houses.
All actions are **logged** for tracking, and the project uses **unit tests** and **CI/CD** for quality.

---

## Features

- Add a house (name, location, price)
- View all houses with status (Available / Rented)
- Rent a house
- Release a house
- Search houses by location or maximum price
- Show only available houses
- Logging for all actions (`house_manager.log`)
- Unit tests for all features
- CI/CD pipeline with GitHub Actions
- Code quality ensured with `pre-commit` hooks

---

## Requirements

- Python 3.11+
- pip
- Virtual environment (`venv`)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd house-renting-manager
```

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install pre-commit hooks:

```bash
pre-commit install
```

---

## Usage

Run the CLI application:

```bash
python app/main.py
```

Menu options:

- Add house
- View houses
- Rent house
- Release house
- Search houses
- Show available houses
- Exit

---

## Testing

Run unit tests with pytest:

```bash
pytest
```

All tests should pass.

---

## CI/CD

CI/CD pipeline is configured with GitHub Actions (`.github/workflows/main.yml`).
On every push or pull request:

- Dependencies are installed
- Pre-commit hooks are run
- Unit tests are executed

---

## Logging

All actions are logged in `house_manager.log`:

- Adding a house
- Renting a house
- Releasing a house
- Searching houses

Example log:

```
2026-03-22 15:30:00 - INFO - Added house: Villa, Kigali, 500
2026-03-22 15:32:12 - INFO - Rented house: Villa
2026-03-22 15:35:10 - INFO - Released house: Villa
```

---

## Project Structure

```
house-renting-manager/
├── app/
│   ├── main.py
│   ├── house.py
│   └── logger.py
├── tests/
│   └── test_house.py
├── .github/workflows/main.yml
├── .pre-commit-config.yaml
├── requirements.txt
├── README.md
└── venv/
```

---

## Agile & DevOps Practices Used

**Agile:** Product Vision, Product Backlog, Sprint Planning, Sprint Reviews, Retrospectives
**DevOps:** Git commits, pre-commit hooks, CI/CD pipeline, unit testing, logging

---

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push and create a pull request
5. CI/CD will validate your code automatically

---

## Author

Arnold Mataba

This README.md includes:

- Project description
- Features
- Installation and usage instructions
- Testing & CI/CD
- Logging
- Project structure
- Agile & DevOps practices
- Contribution guide

---

If you want, next I can **explain the entire project step by step**, summarizing **all sprints, features, DevOps, and Agile process** in one clear explanation.

Do you want me to do that?
