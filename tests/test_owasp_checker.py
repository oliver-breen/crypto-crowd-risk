"""
Unit tests for OWASP Crypto Checker
"""

import unittest
from crypto_risk.owasp_checker import OWASPCryptoChecker


class TestOWASPCryptoChecker(unittest.TestCase):
    """Test cases for OWASPCryptoChecker"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.checker = OWASPCryptoChecker()
    
    def test_approved_aes_256(self):
        """Test that AES-256 is approved"""
        result = self.checker.check_algorithm_strength("AES-256-GCM", key_length=256)
        self.assertTrue(result['compliant'])
        self.assertEqual(result['risk_level'], 'LOW')
    
    def test_deprecated_md5(self):
        """Test that MD5 is flagged as deprecated"""
        result = self.checker.check_algorithm_strength("MD5")
        self.assertFalse(result['compliant'])
        self.assertEqual(result['risk_level'], 'CRITICAL')
    
    def test_deprecated_sha1(self):
        """Test that SHA-1 is flagged as deprecated"""
        result = self.checker.check_algorithm_strength("SHA1")
        self.assertFalse(result['compliant'])
        self.assertEqual(result['risk_level'], 'CRITICAL')
    
    def test_weak_rsa_2048(self):
        """Test that RSA-2048 is below OWASP 2025 standards"""
        result = self.checker.check_algorithm_strength("RSA-2048", key_length=2048)
        self.assertFalse(result['compliant'])
        self.assertEqual(result['risk_level'], 'CRITICAL')
    
    def test_strong_rsa_4096(self):
        """Test that RSA-4096 meets standards"""
        result = self.checker.check_algorithm_strength("RSA-4096", key_length=4096)
        self.assertTrue(result['compliant'])
        self.assertEqual(result['risk_level'], 'LOW')
    
    def test_approved_sha256(self):
        """Test that SHA-256 is approved"""
        result = self.checker.check_algorithm_strength("SHA-256")
        self.assertTrue(result['compliant'])
        self.assertEqual(result['risk_level'], 'LOW')
    
    def test_quantum_resistance_rsa(self):
        """Test quantum resistance assessment for RSA"""
        result = self.checker.check_quantum_resistance("RSA-4096")
        self.assertFalse(result['quantum_resistant'])
        self.assertEqual(result['risk_level'], 'HIGH')
        self.assertTrue(len(result['recommendations']) > 0)
    
    def test_quantum_resistance_aes(self):
        """Test quantum resistance assessment for AES"""
        result = self.checker.check_quantum_resistance("AES-256")
        self.assertEqual(result['risk_level'], 'MEDIUM')
    
    def test_compliance_report_generation(self):
        """Test compliance report generation"""
        systems = [
            {"algorithm": "AES-256-GCM", "key_length": 256},
            {"algorithm": "MD5", "key_length": None},
            {"algorithm": "RSA-4096", "key_length": 4096},
        ]
        report = self.checker.generate_compliance_report(systems)
        
        self.assertEqual(report['total_systems'], 3)
        self.assertGreater(report['critical_issues'], 0)
        self.assertIn(report['overall_risk'], ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'])
    
    def test_key_validation_rsa(self):
        """Test RSA key validation"""
        result = self.checker.validate_key_generation("RSA", 4096)
        self.assertTrue(result['valid'])
        
        result_weak = self.checker.validate_key_generation("RSA", 2048)
        self.assertFalse(result_weak['valid'])
    
    def test_key_validation_aes(self):
        """Test AES key validation"""
        result = self.checker.validate_key_generation("AES", 256)
        self.assertTrue(result['valid'])
        
        result_weak = self.checker.validate_key_generation("AES", 128)
        self.assertFalse(result_weak['valid'])


if __name__ == '__main__':
    unittest.main()
