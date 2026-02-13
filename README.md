# Crypto Crowd Risk

A Python-based cryptocurrency crowd-sourced risk assessment application. This tool allows users to track, analyze, and assess cryptocurrency risks through crowd-sourced data.

## Features

- **Risk Entry Management**: Add and track cryptocurrency risk assessments
- **Risk Calculation**: Automated risk scoring based on multiple factors:
  - Base risk level (Low, Medium, High, Critical)
  - Volatility index
  - Crowd sentiment (Bullish, Neutral, Bearish)
- **Data Storage**: SQLite database for persistent storage
- **CLI Interface**: Easy-to-use command-line interface
- **Statistics**: View aggregate risk statistics by cryptocurrency

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/oliver-breen/crypto-crowd-risk.git
cd crypto-crowd-risk
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install in development mode:
```bash
pip install -e .
```

## Usage

### Command-Line Interface

#### Add a Risk Entry

```bash
python -m crypto_crowd_risk.cli add Bitcoin high "John Doe" \
  --description "High market volatility observed" \
  --volatility 25.5 \
  --sentiment bearish
```

#### List All Entries

```bash
python -m crypto_crowd_risk.cli list
```

#### List Entries for Specific Cryptocurrency

```bash
python -m crypto_crowd_risk.cli list --cryptocurrency Bitcoin
```

#### View Statistics

```bash
python -m crypto_crowd_risk.cli stats Bitcoin
```

### Python API

```python
from datetime import date
from crypto_crowd_risk import (
    CryptoRiskEntry, RiskLevel, CrowdSentiment,
    RiskCalculator, Database
)

# Create database
db = Database("data/crypto_risk.db")

# Create a risk entry
entry = CryptoRiskEntry(
    cryptocurrency="Bitcoin",
    risk_level=RiskLevel.HIGH,
    reporter="Jane Smith",
    report_date=date.today(),
    volatility_index=20.0,
    crowd_sentiment=CrowdSentiment.BEARISH,
)

# Add entry to database (automatically calculates risk score)
entry_id = db.add_entry(entry)

# Retrieve entries
all_entries = db.get_all_entries()
bitcoin_entries = db.get_entries_by_crypto("Bitcoin")

# Calculate average risk
avg_risk = RiskCalculator.calculate_average_risk(bitcoin_entries)
```

## Risk Scoring Algorithm

The risk score (0-100) is calculated using:

1. **Base Score**: Determined by risk level
   - Low: 20 points
   - Medium: 45 points
   - High: 70 points
   - Critical: 90 points

2. **Volatility Factor**: 0-30 points based on volatility index

3. **Sentiment Factor**: -10 to +10 points
   - Bullish: -10 (reduces risk)
   - Neutral: 0
   - Bearish: +10 (increases risk)

Final score is capped between 0 and 100.

## Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=crypto_crowd_risk
```

## Project Structure

```
crypto-crowd-risk/
├── crypto_crowd_risk/      # Main package
│   ├── __init__.py
│   ├── models.py           # Data models
│   ├── calculator.py       # Risk calculation logic
│   ├── database.py         # Database management
│   └── cli.py              # Command-line interface
├── tests/                  # Test suite
│   ├── test_models.py
│   └── test_calculator.py
├── data/                   # Data directory (created at runtime)
├── requirements.txt        # Dependencies
├── setup.py               # Package setup
└── README.md              # This file
```

## License

See LICENSE file for details.
