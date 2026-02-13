"""
Command-line interface for Crypto Crowd Risk assessment tool.
"""

import sys
import json
from typing import Optional
from .owasp_checker import OWASPCryptoChecker
from .risk_analyzer import CryptoRiskAnalyzer
from .market_analyzer import MarketConditionAnalyzer


def print_banner():
    """Print application banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                   CRYPTO CROWD RISK ANALYZER                          ║
    ║              OWASP 2025 Cryptography Compliance Tool                  ║
    ║                      Version 1.0.0                                    ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_owasp_compliance():
    """Run OWASP 2025 cryptography compliance check."""
    print("\n🔍 OWASP 2025 Cryptography Compliance Check\n")
    print("=" * 80)
    
    checker = OWASPCryptoChecker()
    
    # Example systems to check
    systems = [
        {"algorithm": "RSA", "key_length": 2048, "name": "Legacy RSA System"},
        {"algorithm": "RSA", "key_length": 4096, "name": "Modern RSA System"},
        {"algorithm": "AES-256-GCM", "key_length": 256, "name": "AES Encryption"},
        {"algorithm": "SHA-256", "key_length": None, "name": "Hash Function"},
        {"algorithm": "ECDSA-P384", "key_length": 384, "name": "Elliptic Curve"},
        {"algorithm": "MD5", "key_length": None, "name": "Legacy Hash (DEPRECATED)"},
    ]
    
    print("\nAnalyzing cryptographic systems...\n")
    
    for system in systems:
        print(f"System: {system['name']}")
        print(f"  Algorithm: {system['algorithm']}")
        if system['key_length']:
            print(f"  Key Length: {system['key_length']} bits")
        
        result = checker.check_algorithm_strength(
            system['algorithm'], 
            system['key_length']
        )
        
        print(f"  Compliance: {'✓ PASS' if result['compliant'] else '✗ FAIL'}")
        print(f"  Risk Level: {result['risk_level']}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations']:
                print(f"    {rec}")
        
        # Check quantum resistance
        quantum = checker.check_quantum_resistance(system['algorithm'])
        if quantum['recommendations']:
            print("  Quantum Considerations:")
            for rec in quantum['recommendations']:
                print(f"    {rec}")
        
        print()
    
    # Generate compliance report
    report = checker.generate_compliance_report(systems)
    print("\n" + "=" * 80)
    print("COMPLIANCE SUMMARY")
    print("=" * 80)
    print(f"Total Systems Analyzed: {report['total_systems']}")
    print(f"Compliant Systems: {report['compliant_systems']}")
    print(f"Overall Risk Level: {report['overall_risk']}")
    print(f"\nIssue Breakdown:")
    print(f"  CRITICAL: {report['critical_issues']}")
    print(f"  HIGH:     {report['high_issues']}")
    print(f"  MEDIUM:   {report['medium_issues']}")
    print(f"  LOW:      {report['low_issues']}")
    print()


def analyze_crypto_risks():
    """Run cryptocurrency risk analysis."""
    print("\n💰 Cryptocurrency Security Risk Analysis\n")
    print("=" * 80)
    
    analyzer = CryptoRiskAnalyzer()
    
    # Example wallet analysis
    print("\n1. WALLET SECURITY ANALYSIS")
    print("-" * 80)
    
    wallet_configs = [
        {
            "name": "Hot Wallet",
            "type": "hot_wallet",
            "key_storage": "encrypted",
            "mnemonic_protected": True,
            "multisig_enabled": False,
            "hardware_wallet": False,
            "value": 50000
        },
        {
            "name": "Cold Storage",
            "type": "cold_wallet",
            "key_storage": "hardware",
            "mnemonic_protected": True,
            "multisig_enabled": True,
            "hardware_wallet": True,
            "value": 5000000
        }
    ]
    
    for config in wallet_configs:
        result = analyzer.analyze_wallet_security(config)
        print(f"\nWallet: {config['name']}")
        print(f"  Type: {result['wallet_type']}")
        print(f"  Risk Score: {result['risk_score']}/10")
        print(f"  Overall Risk: {result['overall_risk']}")
        
        if result['risks']:
            print("  Identified Risks:")
            for risk in result['risks']:
                print(f"    • {risk}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations']:
                print(f"    • {rec}")
    
    # Example blockchain protocol analysis
    print("\n\n2. BLOCKCHAIN PROTOCOL ANALYSIS")
    print("-" * 80)
    
    protocols = ["Bitcoin", "Ethereum"]
    for protocol in protocols:
        result = analyzer.analyze_blockchain_protocol(protocol)
        print(f"\nProtocol: {result['protocol']}")
        print("  Algorithms Used:")
        for key, value in result['algorithms'].items():
            print(f"    {key}: {value}")
        
        if result['vulnerabilities']:
            print("  Known Vulnerabilities:")
            for vuln in result['vulnerabilities']:
                print(f"    • {vuln}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations']:
                print(f"    • {rec}")
    
    # Example transaction signing analysis
    print("\n\n3. TRANSACTION SIGNING ANALYSIS")
    print("-" * 80)
    
    signing_configs = [
        {
            "name": "Insecure Signing",
            "algorithm": "ECDSA-secp256k1",
            "nonce_handling": "static",
            "malleability_protection": False,
            "side_channel_protection": False
        },
        {
            "name": "Secure Signing",
            "algorithm": "ECDSA-secp256k1",
            "nonce_handling": "rfc6979",
            "malleability_protection": True,
            "side_channel_protection": True
        }
    ]
    
    for config in signing_configs:
        result = analyzer.analyze_transaction_signing(config)
        print(f"\nConfiguration: {config['name']}")
        print(f"  Algorithm: {result['signing_algorithm']}")
        
        if result['risks']:
            print("  Risks:")
            for risk in result['risks']:
                print(f"    • {risk}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations']:
                print(f"    • {rec}")
    
    # Crowd risk scoring
    print("\n\n4. CROWD RISK SCORING (Novel Approach)")
    print("-" * 80)
    print("\nAnalyzing market-based security indicators...\n")
    
    market_examples = [
        {
            "asset": "Established Coin",
            "market_cap": 50_000_000_000,
            "volume": 2_000_000_000,
            "active_addresses": 100_000,
            "github_commits": 5000
        },
        {
            "asset": "New Project",
            "market_cap": 5_000_000,
            "volume": 500_000,
            "active_addresses": 500,
            "github_commits": 50
        }
    ]
    
    for market_data in market_examples:
        result = analyzer.calculate_crowd_risk_score(market_data)
        print(f"Asset: {result['asset']}")
        print(f"  Market Cap: ${result['market_cap_usd']:,.0f}")
        print(f"  Daily Volume: ${result['daily_volume_usd']:,.0f}")
        print(f"  Crowd Risk Score: {result['crowd_risk_score']}/10")
        
        if result['risk_factors']:
            print("  Risk Factors:")
            for factor in result['risk_factors']:
                print(f"    • {factor}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations']:
                print(f"    • {rec}")
        print()


def analyze_market_conditions():
    """Run market conditions security analysis."""
    print("\n📊 Market Condition Security Analysis\n")
    print("=" * 80)
    
    analyzer = MarketConditionAnalyzer()
    
    # Example network data
    network_data = {
        "name": "Example PoW Network",
        "hashrate": 100_000_000,  # TH/s
        "hash_cost": 0.05,  # USD per TH/s per hour
        "total_value_secured": 10_000_000_000  # USD
    }
    
    fee_data = {
        "network": "Example Network",
        "avg_fee_usd": 5.50
    }
    
    mempool_data = {
        "network": "Example Network",
        "size_mb": 50,
        "tx_count": 10000,
        "mev_opportunities": 5,
        "rbf_enabled": True
    }
    
    # Generate comprehensive report
    report = analyzer.generate_market_report(network_data, fee_data, mempool_data)
    print(report)
    
    # Cryptographic agility analysis
    print("\n\n5. CRYPTOGRAPHIC AGILITY ASSESSMENT")
    print("-" * 80)
    
    system_configs = [
        {
            "name": "Modern System",
            "algorithm_versioning": True,
            "hybrid_crypto_support": True,
            "upgrade_mechanism": True,
            "governance_process": True
        },
        {
            "name": "Legacy System",
            "algorithm_versioning": False,
            "hybrid_crypto_support": False,
            "upgrade_mechanism": False,
            "governance_process": False
        }
    ]
    
    for config in system_configs:
        result = analyzer.analyze_cryptographic_agility(config)
        print(f"\nSystem: {result['system']}")
        print(f"  Agility Score: {result['agility_score']}/{result['max_score']}")
        print(f"  Agility Level: {result['agility_level']}")
        print("  Assessment:")
        for finding in result['findings']:
            print(f"    • {finding}")


def show_help():
    """Display help information."""
    help_text = """
Usage: crypto-risk [command]

Commands:
  owasp       - Run OWASP 2025 cryptography compliance check
  crypto      - Analyze cryptocurrency-specific security risks
  market      - Analyze market condition security factors
  all         - Run all analyses (default)
  help        - Show this help message

Examples:
  crypto-risk owasp    # Check OWASP compliance
  crypto-risk crypto   # Analyze crypto risks
  crypto-risk all      # Run complete analysis

About:
  This tool helps assess cryptographic security in cryptocurrency
  systems according to OWASP 2025 guidelines. It provides a novel
  approach combining traditional security analysis with market-based
  risk indicators (crowd risk scoring).

OWASP 2025 Focus Areas:
  • Modern encryption standards (AES-256-GCM, ChaCha20-Poly1305)
  • Strong key lengths (RSA-4096+, ECC P-384+)
  • Quantum-resistant considerations
  • Cryptographic agility
  • Secure random number generation
  • Post-quantum cryptography planning
    """
    print(help_text)


def main():
    """Main entry point for CLI."""
    print_banner()
    
    # Parse command line arguments
    command = sys.argv[1] if len(sys.argv) > 1 else "all"
    
    if command == "help" or command == "--help" or command == "-h":
        show_help()
    elif command == "owasp":
        check_owasp_compliance()
    elif command == "crypto":
        analyze_crypto_risks()
    elif command == "market":
        analyze_market_conditions()
    elif command == "all":
        check_owasp_compliance()
        analyze_crypto_risks()
        analyze_market_conditions()
    else:
        print(f"Unknown command: {command}")
        print("Run 'crypto-risk help' for usage information.")
        sys.exit(1)
    
    print("\n" + "=" * 80)
    print("Analysis complete! For more information, visit:")
    print("https://github.com/oliver-breen/crypto-crowd-risk")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
