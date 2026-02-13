"""
Cryptocurrency Risk Analyzer

Analyzes cryptographic risks specific to cryptocurrency and blockchain systems,
including wallet security, transaction signing, and blockchain protocol vulnerabilities.
"""

from typing import Dict, List, Any
import hashlib


class CryptoRiskAnalyzer:
    """
    Analyzes cryptographic risks in cryptocurrency systems.
    """
    
    # Common cryptocurrency algorithms
    BITCOIN_ALGOS = {
        "signature": "ECDSA-secp256k1",
        "hash": "SHA-256",
        "address": "RIPEMD-160"
    }
    
    ETHEREUM_ALGOS = {
        "signature": "ECDSA-secp256k1",
        "hash": "Keccak-256"
    }
    
    def __init__(self):
        self.risk_scores = {}
        
    def analyze_wallet_security(self, wallet_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze cryptocurrency wallet security configuration.
        
        Args:
            wallet_config: Dictionary containing wallet security parameters
            
        Returns:
            Security analysis with risk assessment
        """
        analysis = {
            "wallet_type": wallet_config.get("type", "UNKNOWN"),
            "risks": [],
            "risk_score": 0,
            "recommendations": []
        }
        
        # Check private key storage
        key_storage = wallet_config.get("key_storage", "").lower()
        if "plaintext" in key_storage or "unencrypted" in key_storage:
            analysis["risks"].append("CRITICAL: Private keys stored in plaintext")
            analysis["risk_score"] += 10
            analysis["recommendations"].append(
                "⚠️ CRITICAL: Encrypt private keys using AES-256-GCM or ChaCha20-Poly1305"
            )
        
        # Check mnemonic seed security
        mnemonic = wallet_config.get("mnemonic_protected", False)
        if not mnemonic:
            analysis["risks"].append("HIGH: Mnemonic seed not properly protected")
            analysis["risk_score"] += 7
            analysis["recommendations"].append(
                "⚠️ Implement BIP-39 compliant mnemonic with passphrase protection"
            )
        
        # Check multi-signature support
        multisig = wallet_config.get("multisig_enabled", False)
        if not multisig and wallet_config.get("value", 0) > 1000000:
            analysis["risks"].append("MEDIUM: High-value wallet without multi-sig")
            analysis["risk_score"] += 5
            analysis["recommendations"].append(
                "💡 Consider multi-signature (2-of-3 or 3-of-5) for high-value wallets"
            )
        
        # Check hardware wallet integration
        hardware = wallet_config.get("hardware_wallet", False)
        if not hardware:
            analysis["risks"].append("LOW: No hardware wallet integration")
            analysis["risk_score"] += 2
            analysis["recommendations"].append(
                "💡 Hardware wallets provide additional security layer"
            )
        
        # Determine overall risk level
        if analysis["risk_score"] >= 10:
            analysis["overall_risk"] = "CRITICAL"
        elif analysis["risk_score"] >= 7:
            analysis["overall_risk"] = "HIGH"
        elif analysis["risk_score"] >= 4:
            analysis["overall_risk"] = "MEDIUM"
        else:
            analysis["overall_risk"] = "LOW"
        
        return analysis
    
    def analyze_blockchain_protocol(self, protocol: str) -> Dict[str, Any]:
        """
        Analyze cryptographic security of blockchain protocols.
        """
        analysis = {
            "protocol": protocol,
            "algorithms": {},
            "vulnerabilities": [],
            "recommendations": []
        }
        
        protocol_upper = protocol.upper()
        
        if "BITCOIN" in protocol_upper or "BTC" in protocol_upper:
            analysis["algorithms"] = self.BITCOIN_ALGOS
            analysis["vulnerabilities"].append(
                "ℹ️ secp256k1 curve has ~128-bit security, quantum-vulnerable"
            )
            analysis["recommendations"].append(
                "Monitor quantum computing advances; plan migration to post-quantum signatures"
            )
            analysis["recommendations"].append(
                "✓ SHA-256 double hashing provides good security"
            )
            
        elif "ETHEREUM" in protocol_upper or "ETH" in protocol_upper:
            analysis["algorithms"] = self.ETHEREUM_ALGOS
            analysis["vulnerabilities"].append(
                "ℹ️ secp256k1 curve has ~128-bit security, quantum-vulnerable"
            )
            analysis["vulnerabilities"].append(
                "⚠️ Smart contract vulnerabilities can bypass cryptographic security"
            )
            analysis["recommendations"].append(
                "Implement formal verification for critical smart contracts"
            )
            analysis["recommendations"].append(
                "Use OpenZeppelin audited libraries for cryptographic operations"
            )
        
        return analysis
    
    def analyze_transaction_signing(self, signing_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze transaction signing security.
        """
        analysis = {
            "signing_algorithm": signing_config.get("algorithm", "UNKNOWN"),
            "risks": [],
            "recommendations": []
        }
        
        # Check for nonce reuse vulnerability
        nonce_handling = signing_config.get("nonce_handling", "").lower()
        if "static" in nonce_handling or "reused" in nonce_handling:
            analysis["risks"].append(
                "CRITICAL: Nonce reuse can leak private keys in ECDSA"
            )
            analysis["recommendations"].append(
                "⚠️ CRITICAL: Use deterministic nonce generation (RFC 6979) or fresh random nonces"
            )
        
        # Check signature malleability
        malleability_check = signing_config.get("malleability_protection", False)
        if not malleability_check:
            analysis["risks"].append(
                "MEDIUM: No signature malleability protection"
            )
            analysis["recommendations"].append(
                "Implement low-S signature normalization to prevent malleability"
            )
        
        # Check for side-channel protection
        side_channel = signing_config.get("side_channel_protection", False)
        if not side_channel:
            analysis["risks"].append(
                "HIGH: No side-channel attack protection"
            )
            analysis["recommendations"].append(
                "Use constant-time signing implementations to prevent timing attacks"
            )
        
        return analysis
    
    def calculate_crowd_risk_score(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate crowd-based risk score for cryptocurrency security.
        
        This novel approach considers market sentiment and adoption patterns
        as indicators of security scrutiny and vulnerability discovery likelihood.
        """
        score_data = {
            "asset": market_data.get("asset", "UNKNOWN"),
            "market_cap_usd": market_data.get("market_cap", 0),
            "daily_volume_usd": market_data.get("volume", 0),
            "active_addresses": market_data.get("active_addresses", 0),
            "github_commits": market_data.get("github_commits", 0),
            "crowd_risk_score": 0,
            "risk_factors": [],
            "recommendations": []
        }
        
        # Low market cap = less scrutiny = higher risk
        if score_data["market_cap_usd"] < 10_000_000:
            score_data["crowd_risk_score"] += 3
            score_data["risk_factors"].append(
                "Low market cap (<$10M) suggests limited security auditing"
            )
        
        # Low development activity = maintenance risk
        if score_data["github_commits"] < 100:
            score_data["crowd_risk_score"] += 2
            score_data["risk_factors"].append(
                "Low development activity may indicate unpatched vulnerabilities"
            )
        
        # High volume with low addresses = potential wash trading
        if score_data["daily_volume_usd"] > 0 and score_data["active_addresses"] > 0:
            volume_per_address = score_data["daily_volume_usd"] / score_data["active_addresses"]
            if volume_per_address > 100_000:
                score_data["crowd_risk_score"] += 2
                score_data["risk_factors"].append(
                    "High volume per active address may indicate market manipulation"
                )
        
        # Generate recommendations
        if score_data["crowd_risk_score"] >= 5:
            score_data["recommendations"].append(
                "⚠️ HIGH RISK: Exercise extreme caution with this asset"
            )
            score_data["recommendations"].append(
                "Verify cryptographic implementation through independent audit"
            )
        elif score_data["crowd_risk_score"] >= 3:
            score_data["recommendations"].append(
                "⚠️ MEDIUM RISK: Additional due diligence recommended"
            )
        else:
            score_data["recommendations"].append(
                "✓ Risk metrics within acceptable ranges"
            )
        
        return score_data
    
    def generate_risk_report(self, analysis_results: List[Dict[str, Any]]) -> str:
        """
        Generate formatted risk report from analysis results.
        """
        report_lines = [
            "=" * 80,
            "CRYPTOCURRENCY CRYPTOGRAPHIC RISK REPORT",
            "=" * 80,
            ""
        ]
        
        for result in analysis_results:
            report_lines.append(f"Analysis Type: {result.get('type', 'UNKNOWN')}")
            report_lines.append("-" * 80)
            
            if "risks" in result:
                report_lines.append("Identified Risks:")
                for risk in result["risks"]:
                    report_lines.append(f"  • {risk}")
                report_lines.append("")
            
            if "recommendations" in result:
                report_lines.append("Recommendations:")
                for rec in result["recommendations"]:
                    report_lines.append(f"  • {rec}")
                report_lines.append("")
            
            report_lines.append("")
        
        return "\n".join(report_lines)
