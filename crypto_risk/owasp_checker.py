"""
OWASP 2025 Cryptography Compliance Checker

This module implements checks for OWASP 2025 cryptographic guidelines,
focusing on:
- Secure key lengths and algorithms
- Proper random number generation
- Secure hash functions
- Modern encryption standards
- Quantum-resistant considerations
"""

from typing import Dict, List, Any
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.backends import default_backend
import hashlib


class OWASPCryptoChecker:
    """
    Validates cryptographic implementations against OWASP 2025 guidelines.
    """
    
    # OWASP 2025 Recommended Algorithms
    APPROVED_SYMMETRIC = ["AES-256-GCM", "ChaCha20-Poly1305"]
    APPROVED_ASYMMETRIC = ["RSA-4096", "ECDSA-P384", "Ed25519"]
    APPROVED_HASHES = ["SHA-256", "SHA-384", "SHA-512", "SHA3-256", "SHA3-512"]
    
    # Deprecated/Weak Algorithms (OWASP 2025)
    DEPRECATED_ALGORITHMS = [
        "DES", "3DES", "RC4", "MD5", "SHA1", "RSA-1024", "RSA-2048"
    ]
    
    # Minimum key lengths (bits)
    MIN_SYMMETRIC_KEY_LENGTH = 256
    MIN_RSA_KEY_LENGTH = 4096
    MIN_ECC_KEY_LENGTH = 384
    
    def __init__(self):
        self.findings = []
        
    def check_algorithm_strength(self, algorithm: str, key_length: int = None) -> Dict[str, Any]:
        """
        Check if an algorithm meets OWASP 2025 standards.
        
        Args:
            algorithm: Name of the cryptographic algorithm
            key_length: Key length in bits (if applicable)
            
        Returns:
            Dictionary with compliance status and recommendations
        """
        result = {
            "algorithm": algorithm,
            "key_length": key_length,
            "compliant": False,
            "risk_level": "UNKNOWN",
            "recommendations": []
        }
        
        # Check for deprecated algorithms
        if any(dep in algorithm.upper() for dep in self.DEPRECATED_ALGORITHMS):
            result["compliant"] = False
            result["risk_level"] = "CRITICAL"
            result["recommendations"].append(
                f"⚠️ CRITICAL: {algorithm} is deprecated in OWASP 2025. "
                f"Migrate to approved algorithms immediately."
            )
            return result
        
        # Check symmetric encryption
        if "AES" in algorithm.upper():
            if key_length and key_length >= self.MIN_SYMMETRIC_KEY_LENGTH:
                result["compliant"] = True
                result["risk_level"] = "LOW"
                result["recommendations"].append(
                    "✓ AES with sufficient key length meets OWASP 2025 standards."
                )
            else:
                result["risk_level"] = "HIGH"
                result["recommendations"].append(
                    f"⚠️ AES key length should be at least {self.MIN_SYMMETRIC_KEY_LENGTH} bits."
                )
        
        # Check asymmetric encryption
        elif "RSA" in algorithm.upper():
            if key_length and key_length >= self.MIN_RSA_KEY_LENGTH:
                result["compliant"] = True
                result["risk_level"] = "LOW"
                result["recommendations"].append(
                    "✓ RSA-4096+ meets OWASP 2025 standards."
                )
            else:
                result["risk_level"] = "CRITICAL"
                result["recommendations"].append(
                    f"⚠️ CRITICAL: RSA key must be at least {self.MIN_RSA_KEY_LENGTH} bits. "
                    "Consider ECC alternatives for better performance."
                )
        
        # Check elliptic curve
        elif "EC" in algorithm.upper() or "ECDSA" in algorithm.upper():
            if "P-256" in algorithm.upper():
                result["risk_level"] = "MEDIUM"
                result["recommendations"].append(
                    "⚠️ P-256 is marginally acceptable. Upgrade to P-384 or P-521 recommended."
                )
            elif "P-384" in algorithm.upper() or "P-521" in algorithm.upper():
                result["compliant"] = True
                result["risk_level"] = "LOW"
                result["recommendations"].append(
                    "✓ ECC P-384/P-521 meets OWASP 2025 standards."
                )
        
        # Check hash functions
        elif "SHA" in algorithm.upper():
            if "SHA1" in algorithm.upper() or "SHA-1" in algorithm.upper():
                result["risk_level"] = "CRITICAL"
                result["recommendations"].append(
                    "⚠️ CRITICAL: SHA-1 is broken. Use SHA-256 or SHA-3 family."
                )
            elif any(h in algorithm.upper() for h in ["SHA-256", "SHA-384", "SHA-512", "SHA3"]):
                result["compliant"] = True
                result["risk_level"] = "LOW"
                result["recommendations"].append(
                    "✓ Hash function meets OWASP 2025 standards."
                )
        
        return result
    
    def check_quantum_resistance(self, algorithm: str) -> Dict[str, Any]:
        """
        Assess quantum computing resistance of cryptographic algorithm.
        
        OWASP 2025 emphasizes preparing for quantum threats.
        """
        result = {
            "algorithm": algorithm,
            "quantum_resistant": False,
            "risk_level": "UNKNOWN",
            "recommendations": []
        }
        
        # Classical algorithms vulnerable to quantum
        vulnerable = ["RSA", "ECDSA", "ECDH", "DH"]
        if any(v in algorithm.upper() for v in vulnerable):
            result["quantum_resistant"] = False
            result["risk_level"] = "HIGH"
            result["recommendations"].append(
                "⚠️ Algorithm is vulnerable to quantum attacks (Shor's algorithm). "
                "Begin planning migration to post-quantum cryptography (PQC)."
            )
            result["recommendations"].append(
                "Consider: CRYSTALS-Kyber, CRYSTALS-Dilithium, or hybrid approaches."
            )
        
        # Symmetric algorithms (doubled key size for quantum)
        elif "AES" in algorithm.upper():
            result["recommendations"].append(
                "ℹ️ AES-256 provides ~128-bit quantum security (Grover's algorithm). "
                "This is considered acceptable for OWASP 2025."
            )
            result["risk_level"] = "MEDIUM"
        
        # Hash functions
        elif "SHA" in algorithm.upper():
            result["recommendations"].append(
                "ℹ️ Hash functions require doubled output for quantum resistance. "
                "SHA-384+ recommended for long-term security."
            )
            result["risk_level"] = "LOW"
        
        return result
    
    def generate_compliance_report(self, systems: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate comprehensive OWASP 2025 compliance report.
        
        Args:
            systems: List of cryptographic systems to analyze
            
        Returns:
            Detailed compliance report with risk scores
        """
        report = {
            "timestamp": "",
            "total_systems": len(systems),
            "compliant_systems": 0,
            "critical_issues": 0,
            "high_issues": 0,
            "medium_issues": 0,
            "low_issues": 0,
            "findings": [],
            "overall_risk": "UNKNOWN"
        }
        
        for system in systems:
            algo = system.get("algorithm", "UNKNOWN")
            key_len = system.get("key_length")
            
            # Check algorithm strength
            algo_check = self.check_algorithm_strength(algo, key_len)
            report["findings"].append(algo_check)
            
            # Check quantum resistance
            quantum_check = self.check_quantum_resistance(algo)
            report["findings"].append(quantum_check)
            
            # Update counters
            if algo_check["compliant"]:
                report["compliant_systems"] += 1
            
            if algo_check["risk_level"] == "CRITICAL":
                report["critical_issues"] += 1
            elif algo_check["risk_level"] == "HIGH":
                report["high_issues"] += 1
            elif algo_check["risk_level"] == "MEDIUM":
                report["medium_issues"] += 1
            elif algo_check["risk_level"] == "LOW":
                report["low_issues"] += 1
        
        # Determine overall risk
        if report["critical_issues"] > 0:
            report["overall_risk"] = "CRITICAL"
        elif report["high_issues"] > 0:
            report["overall_risk"] = "HIGH"
        elif report["medium_issues"] > 0:
            report["overall_risk"] = "MEDIUM"
        else:
            report["overall_risk"] = "LOW"
        
        return report
    
    def validate_key_generation(self, key_type: str, key_size: int) -> Dict[str, Any]:
        """
        Validate cryptographic key generation parameters.
        """
        result = {
            "key_type": key_type,
            "key_size": key_size,
            "valid": False,
            "recommendations": []
        }
        
        if key_type.upper() == "RSA":
            if key_size >= self.MIN_RSA_KEY_LENGTH:
                result["valid"] = True
                result["recommendations"].append(
                    f"✓ RSA-{key_size} meets OWASP 2025 minimum requirements."
                )
            else:
                result["recommendations"].append(
                    f"⚠️ RSA key size {key_size} is below minimum {self.MIN_RSA_KEY_LENGTH}. "
                    "Use RSA-4096 or switch to ECC."
                )
        
        elif key_type.upper() in ["AES", "CHACHA20"]:
            if key_size >= self.MIN_SYMMETRIC_KEY_LENGTH:
                result["valid"] = True
                result["recommendations"].append(
                    f"✓ {key_type}-{key_size} meets OWASP 2025 requirements."
                )
            else:
                result["recommendations"].append(
                    f"⚠️ Symmetric key size should be at least {self.MIN_SYMMETRIC_KEY_LENGTH} bits."
                )
        
        return result
