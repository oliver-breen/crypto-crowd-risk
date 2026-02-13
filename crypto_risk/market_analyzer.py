"""
Market Condition Analyzer for Cryptocurrency Security

Analyzes current market conditions and their impact on cryptographic security,
including network congestion, fee markets, and attack economics.
"""

from typing import Dict, List, Any
from datetime import datetime, timezone


class MarketConditionAnalyzer:
    """
    Analyzes market conditions affecting cryptocurrency security posture.
    """
    
    def __init__(self):
        self.analysis_cache = {}
        
    def analyze_network_security_economics(self, network_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze economic security of blockchain network.
        
        This novel approach assesses the cost of attacking the network
        versus the value secured, following OWASP 2025 risk-based analysis.
        """
        analysis = {
            "network": network_data.get("name", "UNKNOWN"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "attack_cost_analysis": {},
            "security_recommendations": []
        }
        
        # Calculate 51% attack cost (for PoW)
        hashrate = network_data.get("hashrate", 0)
        hash_cost_per_unit = network_data.get("hash_cost", 0)
        
        if hashrate > 0 and hash_cost_per_unit > 0:
            attack_cost_hourly = (hashrate * 0.51) * hash_cost_per_unit
            analysis["attack_cost_analysis"]["51_percent_attack_hourly"] = attack_cost_hourly
            
            # Calculate security margin
            network_value = network_data.get("total_value_secured", 0)
            if network_value > 0:
                security_ratio = attack_cost_hourly / (network_value / 24 / 365)  # hourly value
                analysis["attack_cost_analysis"]["security_ratio"] = security_ratio
                
                if security_ratio < 1:
                    analysis["security_recommendations"].append(
                        "⚠️ CRITICAL: Attack cost is less than value-at-risk. "
                        "Network is economically vulnerable to 51% attacks."
                    )
                elif security_ratio < 10:
                    analysis["security_recommendations"].append(
                        "⚠️ MEDIUM: Security margin is thin. Monitor for hashrate changes."
                    )
                else:
                    analysis["security_recommendations"].append(
                        "✓ Network has strong economic security against PoW attacks."
                    )
        
        # Analyze staking economics (for PoS)
        total_staked = network_data.get("total_staked", 0)
        total_supply = network_data.get("total_supply", 0)
        
        if total_staked > 0 and total_supply > 0:
            staking_ratio = total_staked / total_supply
            analysis["attack_cost_analysis"]["staking_ratio"] = staking_ratio
            
            if staking_ratio < 0.33:
                analysis["security_recommendations"].append(
                    "⚠️ HIGH: Low staking ratio (<33%) increases centralization risk."
                )
            elif staking_ratio > 0.67:
                analysis["security_recommendations"].append(
                    "✓ High staking ratio (>67%) provides strong economic security."
                )
            else:
                analysis["security_recommendations"].append(
                    "ℹ️ Moderate staking ratio. Security depends on validator distribution."
                )
        
        return analysis
    
    def analyze_fee_market_security(self, fee_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze transaction fee market and its security implications.
        
        High fees can make dust attacks expensive, but also price out legitimate users.
        """
        analysis = {
            "network": fee_data.get("network", "UNKNOWN"),
            "current_fee_usd": fee_data.get("avg_fee_usd", 0),
            "congestion_level": "UNKNOWN",
            "security_implications": []
        }
        
        avg_fee = fee_data.get("avg_fee_usd", 0)
        
        # Analyze fee levels
        if avg_fee < 0.01:
            analysis["congestion_level"] = "LOW"
            analysis["security_implications"].append(
                "⚠️ Very low fees enable dust attacks and spam transactions"
            )
            analysis["security_implications"].append(
                "Consider implementing rate limiting or minimum relay fees"
            )
        elif avg_fee < 1.0:
            analysis["congestion_level"] = "MODERATE"
            analysis["security_implications"].append(
                "✓ Moderate fees provide reasonable spam protection"
            )
        elif avg_fee < 10.0:
            analysis["congestion_level"] = "HIGH"
            analysis["security_implications"].append(
                "⚠️ High fees may price out legitimate users"
            )
            analysis["security_implications"].append(
                "Monitor for layer-2 scaling solutions"
            )
        else:
            analysis["congestion_level"] = "CRITICAL"
            analysis["security_implications"].append(
                "⚠️ CRITICAL: Extremely high fees indicate network congestion"
            )
            analysis["security_implications"].append(
                "Network may be under spam attack or needs scaling urgently"
            )
        
        return analysis
    
    def analyze_mempool_security(self, mempool_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze mempool state for security implications.
        
        Mempool analysis can reveal MEV attacks, spam, and censorship.
        """
        analysis = {
            "network": mempool_data.get("network", "UNKNOWN"),
            "mempool_size": mempool_data.get("size_mb", 0),
            "pending_tx_count": mempool_data.get("tx_count", 0),
            "risks": [],
            "recommendations": []
        }
        
        size_mb = mempool_data.get("size_mb", 0)
        tx_count = mempool_data.get("tx_count", 0)
        
        # Check for mempool bloat
        if size_mb > 100:
            analysis["risks"].append(
                "⚠️ Large mempool (>100MB) may indicate spam or DoS attack"
            )
            analysis["recommendations"].append(
                "Implement dynamic fee estimation to prioritize transactions"
            )
        
        # Check for sandwich attack patterns
        if mempool_data.get("mev_opportunities", 0) > 10:
            analysis["risks"].append(
                "⚠️ High MEV (Miner Extractable Value) activity detected"
            )
            analysis["recommendations"].append(
                "Consider using private mempools or MEV-protection services"
            )
        
        # Check transaction replacement
        rbf_enabled = mempool_data.get("rbf_enabled", False)
        if not rbf_enabled:
            analysis["recommendations"].append(
                "💡 Enable RBF (Replace-By-Fee) for better fee management"
            )
        
        return analysis
    
    def analyze_cryptographic_agility(self, system_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess cryptographic agility - ability to upgrade algorithms.
        
        OWASP 2025 emphasizes crypto-agility for responding to emerging threats.
        """
        analysis = {
            "system": system_config.get("name", "UNKNOWN"),
            "agility_score": 0,
            "max_score": 10,
            "findings": []
        }
        
        # Check for algorithm versioning
        if system_config.get("algorithm_versioning", False):
            analysis["agility_score"] += 3
            analysis["findings"].append(
                "✓ Algorithm versioning enables smooth transitions"
            )
        else:
            analysis["findings"].append(
                "⚠️ No algorithm versioning - upgrades will be disruptive"
            )
        
        # Check for hybrid crypto support
        if system_config.get("hybrid_crypto_support", False):
            analysis["agility_score"] += 2
            analysis["findings"].append(
                "✓ Hybrid cryptography enables gradual migration"
            )
        else:
            analysis["findings"].append(
                "💡 Consider hybrid approach (classical + post-quantum)"
            )
        
        # Check for protocol upgrade mechanism
        if system_config.get("upgrade_mechanism", False):
            analysis["agility_score"] += 3
            analysis["findings"].append(
                "✓ Protocol upgrade mechanism exists"
            )
        else:
            analysis["findings"].append(
                "⚠️ No clear upgrade path - may be locked into current algorithms"
            )
        
        # Check for governance process
        if system_config.get("governance_process", False):
            analysis["agility_score"] += 2
            analysis["findings"].append(
                "✓ Governance process can approve security updates"
            )
        else:
            analysis["findings"].append(
                "⚠️ No governance process may delay critical security updates"
            )
        
        # Determine agility level
        if analysis["agility_score"] >= 8:
            analysis["agility_level"] = "HIGH"
        elif analysis["agility_score"] >= 5:
            analysis["agility_level"] = "MEDIUM"
        else:
            analysis["agility_level"] = "LOW"
        
        return analysis
    
    def generate_market_report(self, 
                              network_data: Dict[str, Any],
                              fee_data: Dict[str, Any],
                              mempool_data: Dict[str, Any]) -> str:
        """
        Generate comprehensive market condition security report.
        """
        report_lines = [
            "=" * 80,
            "CRYPTOCURRENCY MARKET SECURITY CONDITIONS REPORT",
            f"Generated: {datetime.now(timezone.utc).isoformat()}",
            "=" * 80,
            ""
        ]
        
        # Network Economics
        net_analysis = self.analyze_network_security_economics(network_data)
        report_lines.append("NETWORK SECURITY ECONOMICS")
        report_lines.append("-" * 80)
        for rec in net_analysis.get("security_recommendations", []):
            report_lines.append(f"  • {rec}")
        report_lines.append("")
        
        # Fee Market
        fee_analysis = self.analyze_fee_market_security(fee_data)
        report_lines.append("FEE MARKET ANALYSIS")
        report_lines.append("-" * 80)
        report_lines.append(f"  Congestion Level: {fee_analysis['congestion_level']}")
        report_lines.append(f"  Average Fee: ${fee_analysis['current_fee_usd']:.2f}")
        for impl in fee_analysis.get("security_implications", []):
            report_lines.append(f"  • {impl}")
        report_lines.append("")
        
        # Mempool
        mempool_analysis = self.analyze_mempool_security(mempool_data)
        report_lines.append("MEMPOOL SECURITY")
        report_lines.append("-" * 80)
        for risk in mempool_analysis.get("risks", []):
            report_lines.append(f"  • {risk}")
        for rec in mempool_analysis.get("recommendations", []):
            report_lines.append(f"  • {rec}")
        report_lines.append("")
        
        report_lines.append("=" * 80)
        report_lines.append("END OF REPORT")
        report_lines.append("=" * 80)
        
        return "\n".join(report_lines)
