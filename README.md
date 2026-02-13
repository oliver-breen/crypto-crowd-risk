# Crypto Crowd Risk - OWASP 2025 Cryptography Assessment Tool

A comprehensive Python application for assessing cryptographic security in cryptocurrency and blockchain systems according to OWASP 2025 guidelines.

## 🎯 Overview

**Crypto Crowd Risk** takes a novel approach to cryptocurrency security by combining:
- **OWASP 2025 Cryptography Compliance**: Validates cryptographic implementations against the latest OWASP standards
- **Cryptocurrency-Specific Risk Analysis**: Evaluates wallet security, blockchain protocols, and transaction signing
- **Market-Based Security Assessment**: Introduces "crowd risk scoring" that considers market conditions, development activity, and economic security
- **Current Market Conditions**: Analyzes fee markets, mempool security, and network economics

## 🚀 Key Features

### 1. OWASP 2025 Compliance Checker
- ✅ Validates encryption algorithms (AES-256-GCM, ChaCha20-Poly1305)
- ✅ Checks key lengths (RSA-4096+, ECC P-384+)
- ✅ Identifies deprecated algorithms (MD5, SHA-1, 3DES, RSA-2048)
- ✅ Assesses quantum resistance
- ✅ Evaluates cryptographic agility

### 2. Cryptocurrency Risk Analyzer
- 💰 Wallet security assessment
- 🔗 Blockchain protocol analysis (Bitcoin, Ethereum, etc.)
- ✍️ Transaction signing security evaluation
- 📊 Novel "crowd risk scoring" based on market indicators
- 🔐 Multi-signature and hardware wallet recommendations

### 3. Market Condition Analyzer
- 📈 Network security economics (51% attack cost analysis)
- 💸 Fee market security implications
- 🔄 Mempool security and MEV analysis
- ⚡ Cryptographic agility assessment
- 🛡️ Economic security ratio calculations

## 📦 Installation

### Requirements
- Python 3.8 or higher
- pip package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/oliver-breen/crypto-crowd-risk.git
cd crypto-crowd-risk

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## 🔧 Usage

### Command Line Interface

Run all analyses:
```bash
crypto-risk all
```

Run specific analyses:
```bash
# OWASP compliance check only
crypto-risk owasp

# Cryptocurrency risk analysis only
crypto-risk crypto

# Market conditions analysis only
crypto-risk market

# Show help
crypto-risk help
```

### Python API

```python
from crypto_risk import OWASPCryptoChecker, CryptoRiskAnalyzer, MarketConditionAnalyzer

# Check OWASP compliance
checker = OWASPCryptoChecker()
result = checker.check_algorithm_strength("AES-256-GCM", key_length=256)
print(result['recommendations'])

# Analyze wallet security
analyzer = CryptoRiskAnalyzer()
wallet_config = {
    "type": "hot_wallet",
    "key_storage": "encrypted",
    "mnemonic_protected": True,
    "multisig_enabled": False,
    "hardware_wallet": False,
    "value": 50000
}
wallet_analysis = analyzer.analyze_wallet_security(wallet_config)
print(f"Risk Score: {wallet_analysis['risk_score']}/10")

# Analyze market conditions
market_analyzer = MarketConditionAnalyzer()
network_data = {
    "name": "Bitcoin",
    "hashrate": 500_000_000,  # TH/s
    "hash_cost": 0.05,
    "total_value_secured": 1_000_000_000_000
}
security_economics = market_analyzer.analyze_network_security_economics(network_data)
```

## 🔬 Novel Approach: Crowd Risk Scoring

One of the unique features of this tool is **Crowd Risk Scoring** - a novel methodology that assesses cryptocurrency security based on market dynamics:

- **Market Capitalization**: Lower market cap = less security scrutiny
- **Development Activity**: GitHub commits indicate active maintenance
- **Trading Volume vs. Active Addresses**: Detects potential manipulation
- **Economic Security**: Calculates cost of attacking vs. value secured

This approach recognizes that security in cryptocurrency is not just about cryptographic strength, but also about ecosystem health and economic incentives.

## 📋 OWASP 2025 Cryptography Guidelines Addressed

This tool implements checks for OWASP 2025's key cryptographic recommendations:

1. **Modern Encryption Standards**
   - AES-256-GCM (authenticated encryption)
   - ChaCha20-Poly1305
   - Minimum 256-bit symmetric keys

2. **Strong Asymmetric Cryptography**
   - RSA-4096 or higher
   - ECDSA with P-384 or P-521 curves
   - Ed25519 for signatures

3. **Secure Hash Functions**
   - SHA-256, SHA-384, SHA-512
   - SHA-3 family
   - Deprecation of SHA-1 and MD5

4. **Quantum Considerations**
   - Assessment of quantum vulnerability
   - Planning for post-quantum migration
   - Hybrid cryptographic approaches

5. **Cryptographic Agility**
   - Algorithm versioning support
   - Upgrade mechanisms
   - Governance processes for security updates

## 🏗️ Project Structure

```
crypto-crowd-risk/
├── crypto_risk/
│   ├── __init__.py              # Package initialization
│   ├── owasp_checker.py         # OWASP 2025 compliance checker
│   ├── risk_analyzer.py         # Cryptocurrency risk analysis
│   ├── market_analyzer.py       # Market condition security analysis
│   └── cli.py                   # Command-line interface
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup configuration
├── README.md                    # This file
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore rules
```

## 🔒 Security Considerations

This tool is designed for **assessment and education** purposes. When using it:

- Always validate findings with security professionals
- Keep cryptographic libraries up to date
- Consider the context of your specific use case
- Plan for quantum-resistant algorithms now
- Implement defense in depth, not just cryptographic security

## 🤝 Contributing

Contributions are welcome! This project addresses cutting-edge security challenges in cryptocurrency. Areas for contribution:

- Additional blockchain protocol analyzers
- Post-quantum cryptography modules
- Real-time market data integration
- Additional OWASP guideline implementations
- Test coverage improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)

## 👤 Author

**Oliver Breen**

---

**⚠️ Disclaimer**: This tool provides security assessments based on OWASP 2025 guidelines and industry best practices. It should be used as part of a comprehensive security strategy, not as the sole security measure. Always consult with qualified security professionals for production systems.
