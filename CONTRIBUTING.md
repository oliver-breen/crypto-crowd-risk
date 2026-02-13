# Contributing to Crypto Crowd Risk

Thank you for your interest in contributing to the Crypto Crowd Risk project! This document provides guidelines for contributing to this OWASP 2025 cryptography assessment tool.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/crypto-crowd-risk.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Install dependencies: `pip install -r requirements.txt`
5. Install in development mode: `pip install -e .`

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Setting Up Your Environment

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

## Project Structure

```
crypto-crowd-risk/
├── crypto_risk/           # Main package
│   ├── __init__.py        # Package initialization
│   ├── owasp_checker.py   # OWASP compliance checker
│   ├── risk_analyzer.py   # Crypto risk analyzer
│   ├── market_analyzer.py # Market condition analyzer
│   └── cli.py             # CLI interface
├── tests/                 # Unit tests
├── examples/              # Example scripts
├── docs/                  # Documentation
└── setup.py              # Package configuration
```

## Code Style

This project follows PEP 8 style guidelines:

- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names
- Include docstrings for classes and functions
- Add type hints where appropriate

### Example Code Style

```python
def analyze_security(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze security configuration.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Analysis results
    """
    result = {
        "compliant": False,
        "risks": []
    }
    return result
```

## Testing

All contributions should include tests.

### Running Tests

```bash
# Run all tests
python -m unittest discover -s tests -p "test_*.py" -v

# Run specific test file
python -m unittest tests.test_owasp_checker -v

# Run with coverage (if pytest-cov installed)
pytest --cov=crypto_risk tests/
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test methods as `test_*`
- Use descriptive test names
- Include both positive and negative test cases

Example:

```python
def test_algorithm_compliance_pass(self):
    """Test that AES-256 passes compliance check"""
    checker = OWASPCryptoChecker()
    result = checker.check_algorithm_strength("AES-256-GCM", 256)
    self.assertTrue(result['compliant'])
```

## Areas for Contribution

### High Priority

1. **Additional Blockchain Protocols**
   - Add analyzers for more blockchain protocols (Cardano, Polkadot, etc.)
   - Implement protocol-specific risk assessments

2. **Post-Quantum Cryptography**
   - Add checks for NIST PQC standards
   - Implement hybrid crypto analysis
   - Support for CRYSTALS-Kyber/Dilithium

3. **Real-Time Market Data**
   - Integration with cryptocurrency APIs
   - Live market condition monitoring
   - Automated risk alerting

4. **Enhanced Reporting**
   - PDF report generation
   - JSON export functionality
   - Dashboard visualizations

### Medium Priority

1. **Additional OWASP Guidelines**
   - Implement more OWASP 2025 checks
   - Add secure coding pattern validation
   - Certificate analysis

2. **Integration Features**
   - CI/CD pipeline integration
   - GitHub Actions support
   - Docker containerization

3. **Educational Content**
   - Interactive tutorials
   - Video walkthroughs
   - Case studies

### Good First Issues

- Add more example scripts
- Improve documentation
- Add unit tests for edge cases
- Fix typos and improve error messages
- Add logging functionality

## Contribution Process

1. **Find or Create an Issue**
   - Check existing issues first
   - Create a new issue describing your contribution
   - Wait for maintainer feedback

2. **Develop Your Feature**
   - Create a feature branch
   - Write code following style guidelines
   - Add tests for new functionality
   - Update documentation

3. **Test Thoroughly**
   - Run all existing tests
   - Add new tests for your code
   - Ensure no regressions

4. **Submit a Pull Request**
   - Push to your fork
   - Create a PR with clear description
   - Reference related issues
   - Wait for code review

### Pull Request Guidelines

- **Title**: Clear, descriptive title
- **Description**: Explain what and why
- **Tests**: Include test coverage
- **Documentation**: Update relevant docs
- **No Breaking Changes**: Unless discussed first

Example PR description:

```
## Description
Add support for Cardano blockchain protocol analysis

## Changes
- Implemented CardanoAnalyzer class
- Added unit tests for Cardano-specific checks
- Updated documentation with Cardano examples

## Related Issues
Closes #42

## Testing
- All existing tests pass
- Added 15 new tests for Cardano analysis
- Manual testing with real Cardano data
```

## Security Considerations

This is a security tool. Pay special attention to:

1. **Cryptographic Operations**
   - Use well-vetted libraries
   - Never implement custom crypto
   - Follow OWASP guidelines

2. **Input Validation**
   - Validate all user inputs
   - Sanitize data before processing
   - Handle edge cases

3. **Dependency Management**
   - Keep dependencies updated
   - Check for vulnerabilities
   - Use minimal dependencies

4. **Disclosure**
   - Report security issues privately
   - Do not publish vulnerabilities publicly
   - Contact maintainers first

## Documentation

Update documentation for:

- New features
- API changes
- Configuration options
- Examples

Documentation locations:
- `README.md` - Main overview
- `docs/OWASP_2025_GUIDELINES.md` - OWASP standards
- `docs/QUICK_START.md` - Usage guide
- Docstrings in code

## Code Review Process

All contributions go through code review:

1. Automated checks (tests, style)
2. Maintainer review
3. Feedback and iteration
4. Approval and merge

Be prepared to:
- Answer questions
- Make changes
- Discuss design decisions

## Communication

- **GitHub Issues**: Bug reports, feature requests
- **Pull Requests**: Code contributions
- **Discussions**: General questions, ideas

## Recognition

Contributors are:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Mentioned in commit messages

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions:
1. Check existing documentation
2. Search closed issues
3. Open a new issue
4. Tag it as "question"

## Thank You!

Your contributions make this project better for everyone working to improve cryptocurrency security. Whether you're fixing a typo or adding a major feature, every contribution matters.

---

**Remember**: Security is everyone's responsibility. Let's build safer cryptocurrency systems together!
