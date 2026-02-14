"""
Example: Cryptocurrency Risk Analysis

This example demonstrates cryptocurrency-specific risk analysis including
wallet security, blockchain protocols, and the novel crowd risk scoring.
"""

from crypto_risk import CryptoRiskAnalyzer


def main():
    print("=" * 80)
    print("EXAMPLE: Cryptocurrency Security Risk Analysis")
    print("=" * 80)
    print()
    
    analyzer = CryptoRiskAnalyzer()
    
    # Example 1: Analyze different wallet configurations
    print("1. Wallet Security Analysis")
    print("-" * 80)
    
    wallets = [
        {
            "name": "Mobile Hot Wallet",
            "type": "hot_wallet",
            "key_storage": "encrypted",
            "mnemonic_protected": True,
            "multisig_enabled": False,
            "hardware_wallet": False,
            "value": 5000
        },
        {
            "name": "Exchange Hot Wallet",
            "type": "hot_wallet",
            "key_storage": "plaintext",  # Bad practice!
            "mnemonic_protected": False,
            "multisig_enabled": False,
            "hardware_wallet": False,
            "value": 1000000
        },
        {
            "name": "Institutional Cold Storage",
            "type": "cold_wallet",
            "key_storage": "hardware",
            "mnemonic_protected": True,
            "multisig_enabled": True,
            "hardware_wallet": True,
            "value": 50000000
        }
    ]
    
    for wallet in wallets:
        print(f"\n{wallet['name']}:")
        result = analyzer.analyze_wallet_security(wallet)
        print(f"  Type: {result['wallet_type']}")
        print(f"  Risk Score: {result['risk_score']}/10")
        print(f"  Overall Risk: {result['overall_risk']}")
        
        if result['risks']:
            print("  Risks:")
            for risk in result['risks']:
                print(f"    • {risk}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations'][:2]:  # Show first 2
                print(f"    • {rec}")
    
    # Example 2: Analyze blockchain protocols
    print("\n\n2. Blockchain Protocol Analysis")
    print("-" * 80)
    
    protocols = ["Bitcoin", "Ethereum"]
    for protocol in protocols:
        print(f"\n{protocol}:")
        result = analyzer.analyze_blockchain_protocol(protocol)
        print("  Cryptographic Algorithms:")
        for key, value in result['algorithms'].items():
            print(f"    {key.title()}: {value}")
        
        print("  Security Considerations:")
        for item in result['vulnerabilities'][:2]:
            print(f"    • {item}")
    
    # Example 3: Crowd Risk Scoring (Novel Approach)
    print("\n\n3. Crowd Risk Scoring - Novel Market-Based Assessment")
    print("-" * 80)
    print("\nThis innovative approach considers market dynamics as security indicators:")
    
    assets = [
        {
            "name": "Established Cryptocurrency",
            "asset": "Example Coin A",
            "market_cap": 100_000_000_000,
            "volume": 5_000_000_000,
            "active_addresses": 500_000,
            "github_commits": 10000
        },
        {
            "name": "Mid-Cap Project",
            "asset": "Example Coin B",
            "market_cap": 500_000_000,
            "volume": 50_000_000,
            "active_addresses": 10_000,
            "github_commits": 1000
        },
        {
            "name": "New/Small Project",
            "asset": "Example Coin C",
            "market_cap": 2_000_000,
            "volume": 100_000,
            "active_addresses": 200,
            "github_commits": 30
        }
    ]
    
    for asset in assets:
        print(f"\n{asset['name']} ({asset['asset']}):")
        result = analyzer.calculate_crowd_risk_score(asset)
        print(f"  Market Cap: ${result['market_cap_usd']:,.0f}")
        print(f"  Daily Volume: ${result['daily_volume_usd']:,.0f}")
        print(f"  Active Addresses: {result['active_addresses']:,}")
        print(f"  GitHub Commits: {result['github_commits']:,}")
        print(f"  Crowd Risk Score: {result['crowd_risk_score']}/10")
        
        if result['risk_factors']:
            print("  Risk Factors:")
            for factor in result['risk_factors']:
                print(f"    • {factor}")
        
        if result['recommendations']:
            print("  Recommendation:")
            print(f"    • {result['recommendations'][0]}")
    
    print("\n\n" + "=" * 80)
    print("Key Insight: Crowd Risk Scoring combines traditional cryptographic")
    print("analysis with market dynamics to provide a holistic security assessment.")
    print("=" * 80)


if __name__ == "__main__":
    main()
