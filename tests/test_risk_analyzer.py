"""
Unit tests for Crypto Risk Analyzer
"""

import unittest
from crypto_risk.risk_analyzer import CryptoRiskAnalyzer


class TestCryptoRiskAnalyzer(unittest.TestCase):
    """Test cases for CryptoRiskAnalyzer"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = CryptoRiskAnalyzer()
    
    def test_wallet_security_plaintext_keys(self):
        """Test that plaintext keys are flagged as critical"""
        config = {
            "type": "hot_wallet",
            "key_storage": "plaintext",
            "mnemonic_protected": False,
            "multisig_enabled": False,
            "hardware_wallet": False,
            "value": 100000
        }
        result = self.analyzer.analyze_wallet_security(config)
        
        self.assertEqual(result['overall_risk'], 'CRITICAL')
        self.assertGreater(result['risk_score'], 8)
        self.assertTrue(any('CRITICAL' in risk for risk in result['risks']))
    
    def test_wallet_security_secure_config(self):
        """Test secure wallet configuration"""
        config = {
            "type": "cold_wallet",
            "key_storage": "hardware",
            "mnemonic_protected": True,
            "multisig_enabled": True,
            "hardware_wallet": True,
            "value": 1000000
        }
        result = self.analyzer.analyze_wallet_security(config)
        
        self.assertIn(result['overall_risk'], ['LOW', 'MEDIUM'])
        self.assertLess(result['risk_score'], 5)
    
    def test_blockchain_protocol_bitcoin(self):
        """Test Bitcoin protocol analysis"""
        result = self.analyzer.analyze_blockchain_protocol("Bitcoin")
        
        self.assertIn("signature", result['algorithms'])
        self.assertEqual(result['algorithms']['signature'], "ECDSA-secp256k1")
        self.assertTrue(len(result['vulnerabilities']) > 0)
        self.assertTrue(len(result['recommendations']) > 0)
    
    def test_blockchain_protocol_ethereum(self):
        """Test Ethereum protocol analysis"""
        result = self.analyzer.analyze_blockchain_protocol("Ethereum")
        
        self.assertIn("signature", result['algorithms'])
        self.assertEqual(result['algorithms']['signature'], "ECDSA-secp256k1")
        self.assertTrue(len(result['vulnerabilities']) > 0)
    
    def test_transaction_signing_nonce_reuse(self):
        """Test detection of nonce reuse vulnerability"""
        config = {
            "algorithm": "ECDSA",
            "nonce_handling": "static",
            "malleability_protection": False,
            "side_channel_protection": False
        }
        result = self.analyzer.analyze_transaction_signing(config)
        
        self.assertTrue(any('CRITICAL' in risk for risk in result['risks']))
        self.assertTrue(any('nonce' in risk.lower() for risk in result['risks']))
    
    def test_transaction_signing_secure(self):
        """Test secure transaction signing configuration"""
        config = {
            "algorithm": "ECDSA",
            "nonce_handling": "rfc6979",
            "malleability_protection": True,
            "side_channel_protection": True
        }
        result = self.analyzer.analyze_transaction_signing(config)
        
        # Should have minimal risks
        self.assertLessEqual(len(result['risks']), 1)
    
    def test_crowd_risk_score_low_market_cap(self):
        """Test crowd risk scoring for low market cap"""
        data = {
            "asset": "Test Coin",
            "market_cap": 1_000_000,  # Low market cap
            "volume": 50_000,
            "active_addresses": 100,
            "github_commits": 20
        }
        result = self.analyzer.calculate_crowd_risk_score(data)
        
        self.assertGreater(result['crowd_risk_score'], 3)
        self.assertTrue(len(result['risk_factors']) > 0)
    
    def test_crowd_risk_score_established_coin(self):
        """Test crowd risk scoring for established coin"""
        data = {
            "asset": "Established Coin",
            "market_cap": 50_000_000_000,
            "volume": 2_000_000_000,
            "active_addresses": 500_000,
            "github_commits": 10000
        }
        result = self.analyzer.calculate_crowd_risk_score(data)
        
        self.assertLess(result['crowd_risk_score'], 3)
    
    def test_risk_report_generation(self):
        """Test risk report generation"""
        results = [
            {
                "type": "wallet_analysis",
                "risks": ["Test risk 1", "Test risk 2"],
                "recommendations": ["Test rec 1"]
            }
        ]
        report = self.analyzer.generate_risk_report(results)
        
        self.assertIsInstance(report, str)
        self.assertTrue(len(report) > 0)
        self.assertIn("RISK REPORT", report)


if __name__ == '__main__':
    unittest.main()
