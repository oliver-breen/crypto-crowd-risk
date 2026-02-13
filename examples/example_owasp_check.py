"""
Example: Basic OWASP 2025 Compliance Check

This example demonstrates how to use the OWASPCryptoChecker to validate
cryptographic implementations against OWASP 2025 guidelines.
"""

from crypto_risk import OWASPCryptoChecker


def main():
    print("=" * 80)
    print("EXAMPLE: OWASP 2025 Cryptography Compliance Check")
    print("=" * 80)
    print()
    
    # Initialize the checker
    checker = OWASPCryptoChecker()
    
    # Example 1: Check modern AES encryption
    print("1. Checking AES-256-GCM (Modern Standard)")
    print("-" * 80)
    result = checker.check_algorithm_strength("AES-256-GCM", key_length=256)
    print(f"Compliant: {result['compliant']}")
    print(f"Risk Level: {result['risk_level']}")
    for rec in result['recommendations']:
        print(f"  • {rec}")
    print()
    
    # Example 2: Check legacy RSA
    print("2. Checking RSA-2048 (Legacy - Below OWASP 2025 Standard)")
    print("-" * 80)
    result = checker.check_algorithm_strength("RSA-2048", key_length=2048)
    print(f"Compliant: {result['compliant']}")
    print(f"Risk Level: {result['risk_level']}")
    for rec in result['recommendations']:
        print(f"  • {rec}")
    print()
    
    # Example 3: Check modern RSA
    print("3. Checking RSA-4096 (Modern Standard)")
    print("-" * 80)
    result = checker.check_algorithm_strength("RSA-4096", key_length=4096)
    print(f"Compliant: {result['compliant']}")
    print(f"Risk Level: {result['risk_level']}")
    for rec in result['recommendations']:
        print(f"  • {rec}")
    print()
    
    # Example 4: Check deprecated algorithm
    print("4. Checking MD5 (Deprecated)")
    print("-" * 80)
    result = checker.check_algorithm_strength("MD5")
    print(f"Compliant: {result['compliant']}")
    print(f"Risk Level: {result['risk_level']}")
    for rec in result['recommendations']:
        print(f"  • {rec}")
    print()
    
    # Example 5: Quantum resistance check
    print("5. Quantum Resistance Assessment")
    print("-" * 80)
    algorithms = ["RSA-4096", "AES-256", "SHA-384"]
    for algo in algorithms:
        result = checker.check_quantum_resistance(algo)
        print(f"\n{algo}:")
        print(f"  Quantum Resistant: {result['quantum_resistant']}")
        print(f"  Risk Level: {result['risk_level']}")
        for rec in result['recommendations']:
            print(f"    • {rec}")
    print()
    
    # Example 6: Generate compliance report
    print("\n6. Comprehensive Compliance Report")
    print("-" * 80)
    systems = [
        {"algorithm": "AES-256-GCM", "key_length": 256},
        {"algorithm": "RSA-2048", "key_length": 2048},
        {"algorithm": "RSA-4096", "key_length": 4096},
        {"algorithm": "SHA-256", "key_length": None},
        {"algorithm": "MD5", "key_length": None},
    ]
    
    report = checker.generate_compliance_report(systems)
    print(f"Total Systems: {report['total_systems']}")
    print(f"Compliant: {report['compliant_systems']}")
    print(f"Overall Risk: {report['overall_risk']}")
    print(f"\nIssue Count:")
    print(f"  CRITICAL: {report['critical_issues']}")
    print(f"  HIGH: {report['high_issues']}")
    print(f"  MEDIUM: {report['medium_issues']}")
    print(f"  LOW: {report['low_issues']}")
    print()


if __name__ == "__main__":
    main()
