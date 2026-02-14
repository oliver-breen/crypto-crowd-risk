"""
Example: Market Condition Security Analysis

This example demonstrates how to analyze market conditions for their
security implications, including network economics and fee markets.
"""

from crypto_risk import MarketConditionAnalyzer


def main():
    print("=" * 80)
    print("EXAMPLE: Market Condition Security Analysis")
    print("=" * 80)
    print()
    
    analyzer = MarketConditionAnalyzer()
    
    # Example 1: Network Security Economics
    print("1. Network Security Economics (51% Attack Analysis)")
    print("-" * 80)
    
    networks = [
        {
            "name": "High Security PoW Network",
            "hashrate": 500_000_000,  # 500 EH/s
            "hash_cost": 0.05,  # $0.05 per TH/s per hour
            "total_value_secured": 1_000_000_000_000  # $1 trillion
        },
        {
            "name": "Medium Security PoW Network",
            "hashrate": 10_000_000,  # 10 EH/s
            "hash_cost": 0.05,
            "total_value_secured": 50_000_000_000  # $50 billion
        },
        {
            "name": "Low Security PoW Network",
            "hashrate": 100_000,  # 100 TH/s
            "hash_cost": 0.05,
            "total_value_secured": 100_000_000  # $100 million
        }
    ]
    
    for network in networks:
        print(f"\n{network['name']}:")
        result = analyzer.analyze_network_security_economics(network)
        
        if "51_percent_attack_hourly" in result['attack_cost_analysis']:
            attack_cost = result['attack_cost_analysis']['51_percent_attack_hourly']
            print(f"  51% Attack Cost (hourly): ${attack_cost:,.2f}")
        
        if "security_ratio" in result['attack_cost_analysis']:
            ratio = result['attack_cost_analysis']['security_ratio']
            print(f"  Security Ratio: {ratio:.2f}x")
        
        print("  Assessment:")
        for rec in result['security_recommendations']:
            print(f"    • {rec}")
    
    # Example 2: Fee Market Analysis
    print("\n\n2. Fee Market Security Analysis")
    print("-" * 80)
    
    fee_scenarios = [
        {"network": "Low Fee Network", "avg_fee_usd": 0.005},
        {"network": "Normal Fee Network", "avg_fee_usd": 0.50},
        {"network": "High Fee Network", "avg_fee_usd": 5.00},
        {"network": "Extreme Fee Network", "avg_fee_usd": 50.00},
    ]
    
    for scenario in fee_scenarios:
        print(f"\n{scenario['network']}:")
        result = analyzer.analyze_fee_market_security(scenario)
        print(f"  Average Fee: ${result['current_fee_usd']:.2f}")
        print(f"  Congestion Level: {result['congestion_level']}")
        print("  Security Implications:")
        for impl in result['security_implications']:
            print(f"    • {impl}")
    
    # Example 3: Mempool Security
    print("\n\n3. Mempool Security Analysis")
    print("-" * 80)
    
    mempool_scenarios = [
        {
            "name": "Normal Conditions",
            "network": "Example Network",
            "size_mb": 20,
            "tx_count": 5000,
            "mev_opportunities": 2,
            "rbf_enabled": True
        },
        {
            "name": "Under Attack",
            "network": "Example Network",
            "size_mb": 150,
            "tx_count": 100000,
            "mev_opportunities": 25,
            "rbf_enabled": False
        }
    ]
    
    for scenario in mempool_scenarios:
        print(f"\n{scenario['name']}:")
        result = analyzer.analyze_mempool_security(scenario)
        print(f"  Mempool Size: {result['mempool_size']} MB")
        print(f"  Pending Transactions: {result['pending_tx_count']:,}")
        
        if result['risks']:
            print("  Risks:")
            for risk in result['risks']:
                print(f"    • {risk}")
        
        if result['recommendations']:
            print("  Recommendations:")
            for rec in result['recommendations']:
                print(f"    • {rec}")
    
    # Example 4: Cryptographic Agility
    print("\n\n4. Cryptographic Agility Assessment")
    print("-" * 80)
    print("\nOWASP 2025 emphasizes the ability to upgrade cryptographic algorithms:")
    
    systems = [
        {
            "name": "Modern Agile System",
            "algorithm_versioning": True,
            "hybrid_crypto_support": True,
            "upgrade_mechanism": True,
            "governance_process": True
        },
        {
            "name": "Legacy Rigid System",
            "algorithm_versioning": False,
            "hybrid_crypto_support": False,
            "upgrade_mechanism": False,
            "governance_process": False
        }
    ]
    
    for system in systems:
        print(f"\n{system['name']}:")
        result = analyzer.analyze_cryptographic_agility(system)
        print(f"  Agility Score: {result['agility_score']}/{result['max_score']}")
        print(f"  Agility Level: {result['agility_level']}")
        print("  Key Findings:")
        for finding in result['findings'][:3]:  # Show first 3
            print(f"    • {finding}")
    
    # Example 5: Comprehensive Report
    print("\n\n5. Comprehensive Market Report")
    print("-" * 80)
    
    # Sample data for a complete report
    network_data = {
        "name": "Example Blockchain",
        "hashrate": 100_000_000,
        "hash_cost": 0.05,
        "total_value_secured": 50_000_000_000
    }
    
    fee_data = {
        "network": "Example Blockchain",
        "avg_fee_usd": 2.50
    }
    
    mempool_data = {
        "network": "Example Blockchain",
        "size_mb": 45,
        "tx_count": 15000,
        "mev_opportunities": 8,
        "rbf_enabled": True
    }
    
    report = analyzer.generate_market_report(network_data, fee_data, mempool_data)
    print(report)


if __name__ == "__main__":
    main()
