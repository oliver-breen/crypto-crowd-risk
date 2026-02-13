# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/oliver-breen/crypto-crowd-risk.git
cd crypto-crowd-risk

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Basic Usage

### 1. Run All Analyses

```bash
crypto-risk all
```

This will run all three analysis modules:
- OWASP 2025 compliance check
- Cryptocurrency risk analysis
- Market condition security analysis

### 2. Run Individual Analyses

```bash
# OWASP 2025 compliance check only
crypto-risk owasp

# Cryptocurrency risk analysis only
crypto-risk crypto

# Market conditions analysis only
crypto-risk market
```

### 3. Get Help

```bash
crypto-risk help
```

## Python API Usage

### Example 1: Check Algorithm Compliance

```python
from crypto_risk import OWASPCryptoChecker

checker = OWASPCryptoChecker()

# Check if algorithm meets OWASP 2025 standards
result = checker.check_algorithm_strength("AES-256-GCM", key_length=256)
print(f"Compliant: {result['compliant']}")
print(f"Risk Level: {result['risk_level']}")

# Check quantum resistance
quantum = checker.check_quantum_resistance("RSA-4096")
print(f"Quantum Resistant: {quantum['quantum_resistant']}")
```

### Example 2: Analyze Wallet Security

```python
from crypto_risk import CryptoRiskAnalyzer

analyzer = CryptoRiskAnalyzer()

wallet_config = {
    "type": "hot_wallet",
    "key_storage": "encrypted",
    "mnemonic_protected": True,
    "multisig_enabled": False,
    "hardware_wallet": False,
    "value": 50000
}

result = analyzer.analyze_wallet_security(wallet_config)
print(f"Risk Score: {result['risk_score']}/10")
print(f"Overall Risk: {result['overall_risk']}")

for rec in result['recommendations']:
    print(f"• {rec}")
```

### Example 3: Calculate Crowd Risk Score

```python
from crypto_risk import CryptoRiskAnalyzer

analyzer = CryptoRiskAnalyzer()

market_data = {
    "asset": "Example Coin",
    "market_cap": 5_000_000,
    "volume": 500_000,
    "active_addresses": 500,
    "github_commits": 50
}

result = analyzer.calculate_crowd_risk_score(market_data)
print(f"Crowd Risk Score: {result['crowd_risk_score']}/10")

for factor in result['risk_factors']:
    print(f"• {factor}")
```

### Example 4: Analyze Network Economics

```python
from crypto_risk import MarketConditionAnalyzer

analyzer = MarketConditionAnalyzer()

network_data = {
    "name": "Example Network",
    "hashrate": 100_000_000,
    "hash_cost": 0.05,
    "total_value_secured": 50_000_000_000
}

result = analyzer.analyze_network_security_economics(network_data)

if "51_percent_attack_hourly" in result['attack_cost_analysis']:
    cost = result['attack_cost_analysis']['51_percent_attack_hourly']
    print(f"51% Attack Cost (hourly): ${cost:,.2f}")

for rec in result['security_recommendations']:
    print(f"• {rec}")
```

## Running Examples

The repository includes comprehensive example scripts:

```bash
# OWASP compliance examples
python examples/example_owasp_check.py

# Cryptocurrency risk analysis examples
python examples/example_crypto_analysis.py

# Market condition analysis examples
python examples/example_market_analysis.py
```

## Running Tests

```bash
# Run all tests
python -m unittest discover -s tests -p "test_*.py" -v

# Run specific test module
python -m unittest tests.test_owasp_checker -v
```

## Understanding the Output

### Risk Levels

- **CRITICAL**: Immediate action required, severe security risk
- **HIGH**: Significant risk, should be addressed soon
- **MEDIUM**: Moderate risk, plan remediation
- **LOW**: Minimal risk, follow best practices

### Compliance Status

- ✓ **PASS**: Meets OWASP 2025 standards
- ✗ **FAIL**: Does not meet OWASP 2025 standards

### Crowd Risk Score

Scale of 0-10 where:
- **0-2**: Low risk, well-established project
- **3-4**: Medium risk, exercise caution
- **5+**: High risk, requires thorough due diligence

## Common Use Cases

### 1. Auditing Existing Cryptographic Implementation

```bash
crypto-risk owasp
```

Review the output to identify:
- Deprecated algorithms in use
- Insufficient key lengths
- Quantum vulnerability exposure

### 2. Evaluating Cryptocurrency Investment

```python
from crypto_risk import CryptoRiskAnalyzer

analyzer = CryptoRiskAnalyzer()

# Analyze the protocol
protocol_analysis = analyzer.analyze_blockchain_protocol("Bitcoin")

# Calculate crowd risk
market_data = {...}  # Your market data
crowd_risk = analyzer.calculate_crowd_risk_score(market_data)
```

### 3. Assessing Network Security Posture

```bash
crypto-risk market
```

This analyzes:
- Economic cost of attacks
- Fee market health
- Mempool security
- Cryptographic agility

### 4. Wallet Security Assessment

```python
from crypto_risk import CryptoRiskAnalyzer

analyzer = CryptoRiskAnalyzer()

# Define your wallet configuration
wallet_config = {
    "type": "cold_wallet",
    "key_storage": "hardware",
    "mnemonic_protected": True,
    "multisig_enabled": True,
    "hardware_wallet": True,
    "value": 1000000
}

# Analyze security
result = analyzer.analyze_wallet_security(wallet_config)
```

## Troubleshooting

### Import Errors

If you get import errors, ensure the package is installed:

```bash
pip install -e .
```

### Missing Dependencies

Install all required dependencies:

```bash
pip install -r requirements.txt
```

### Python Version

Ensure you're using Python 3.8 or higher:

```bash
python --version
```

## Next Steps

1. Read the full [README.md](../README.md) for detailed information
2. Review [OWASP 2025 Guidelines](OWASP_2025_GUIDELINES.md) documentation
3. Explore the example scripts in the `examples/` directory
4. Run the test suite to understand the validation logic
5. Integrate the API into your own security workflows

## Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/oliver-breen/crypto-crowd-risk/issues
- Repository: https://github.com/oliver-breen/crypto-crowd-risk

---

**Remember**: This tool provides risk assessment and recommendations. Always consult with security professionals for production systems.
