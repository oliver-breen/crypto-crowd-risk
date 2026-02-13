"""
Unit tests for Market Condition Analyzer
"""

import unittest
from crypto_risk.market_analyzer import MarketConditionAnalyzer


class TestMarketConditionAnalyzer(unittest.TestCase):
    """Test cases for MarketConditionAnalyzer"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = MarketConditionAnalyzer()
    
    def test_network_security_economics_high_security(self):
        """Test network with high economic security"""
        data = {
            "name": "Secure Network",
            "hashrate": 500_000_000,
            "hash_cost": 0.05,
            "total_value_secured": 1_000_000_000_000
        }
        result = self.analyzer.analyze_network_security_economics(data)
        
        self.assertIn("attack_cost_analysis", result)
        self.assertIn("security_recommendations", result)
        self.assertTrue(len(result['security_recommendations']) > 0)
    
    def test_network_security_economics_vulnerable(self):
        """Test network with low economic security"""
        data = {
            "name": "Vulnerable Network",
            "hashrate": 100_000,
            "hash_cost": 0.05,
            "total_value_secured": 100_000_000_000  # High value, low hashrate
        }
        result = self.analyzer.analyze_network_security_economics(data)
        
        if "security_ratio" in result['attack_cost_analysis']:
            security_ratio = result['attack_cost_analysis']['security_ratio']
            # Low security ratio means vulnerable
            self.assertTrue(any('CRITICAL' in rec or 'MEDIUM' in rec 
                              for rec in result['security_recommendations']))
    
    def test_fee_market_low_fees(self):
        """Test fee market analysis with very low fees"""
        data = {
            "network": "Test Network",
            "avg_fee_usd": 0.005
        }
        result = self.analyzer.analyze_fee_market_security(data)
        
        self.assertEqual(result['congestion_level'], 'LOW')
        self.assertTrue(any('dust' in impl.lower() or 'spam' in impl.lower() 
                          for impl in result['security_implications']))
    
    def test_fee_market_high_fees(self):
        """Test fee market analysis with high fees"""
        data = {
            "network": "Test Network",
            "avg_fee_usd": 15.0
        }
        result = self.analyzer.analyze_fee_market_security(data)
        
        self.assertIn(result['congestion_level'], ['HIGH', 'CRITICAL'])
        self.assertTrue(len(result['security_implications']) > 0)
    
    def test_mempool_security_normal(self):
        """Test mempool analysis under normal conditions"""
        data = {
            "network": "Test Network",
            "size_mb": 20,
            "tx_count": 5000,
            "mev_opportunities": 2,
            "rbf_enabled": True
        }
        result = self.analyzer.analyze_mempool_security(data)
        
        # Should have minimal risks under normal conditions
        self.assertLessEqual(len(result['risks']), 1)
    
    def test_mempool_security_under_attack(self):
        """Test mempool analysis under potential attack"""
        data = {
            "network": "Test Network",
            "size_mb": 150,
            "tx_count": 100000,
            "mev_opportunities": 25,
            "rbf_enabled": False
        }
        result = self.analyzer.analyze_mempool_security(data)
        
        self.assertTrue(len(result['risks']) > 0)
        self.assertTrue(len(result['recommendations']) > 0)
    
    def test_cryptographic_agility_high(self):
        """Test high cryptographic agility"""
        config = {
            "name": "Modern System",
            "algorithm_versioning": True,
            "hybrid_crypto_support": True,
            "upgrade_mechanism": True,
            "governance_process": True
        }
        result = self.analyzer.analyze_cryptographic_agility(config)
        
        self.assertGreaterEqual(result['agility_score'], 8)
        self.assertEqual(result['agility_level'], 'HIGH')
    
    def test_cryptographic_agility_low(self):
        """Test low cryptographic agility"""
        config = {
            "name": "Legacy System",
            "algorithm_versioning": False,
            "hybrid_crypto_support": False,
            "upgrade_mechanism": False,
            "governance_process": False
        }
        result = self.analyzer.analyze_cryptographic_agility(config)
        
        self.assertEqual(result['agility_score'], 0)
        self.assertEqual(result['agility_level'], 'LOW')
    
    def test_market_report_generation(self):
        """Test comprehensive market report generation"""
        network_data = {
            "name": "Test Network",
            "hashrate": 100_000_000,
            "hash_cost": 0.05,
            "total_value_secured": 10_000_000_000
        }
        fee_data = {
            "network": "Test Network",
            "avg_fee_usd": 2.50
        }
        mempool_data = {
            "network": "Test Network",
            "size_mb": 30,
            "tx_count": 8000,
            "mev_opportunities": 5,
            "rbf_enabled": True
        }
        
        report = self.analyzer.generate_market_report(
            network_data, fee_data, mempool_data
        )
        
        self.assertIsInstance(report, str)
        self.assertTrue(len(report) > 0)
        self.assertIn("MARKET SECURITY CONDITIONS", report)


if __name__ == '__main__':
    unittest.main()
