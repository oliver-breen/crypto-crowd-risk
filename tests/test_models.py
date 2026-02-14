"""
Unit tests for data models
"""
import pytest
from datetime import date
from crypto_crowd_risk import CryptoRiskEntry, RiskLevel, CrowdSentiment


class TestCryptoRiskEntry:
    """Test cases for CryptoRiskEntry model"""

    def test_create_basic_entry(self):
        """Test creating a basic crypto risk entry"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="Test User",
            report_date=date(2024, 1, 1),
        )
        assert entry.cryptocurrency == "Bitcoin"
        assert entry.risk_level == RiskLevel.MEDIUM
        assert entry.reporter == "Test User"
        assert entry.report_date == date(2024, 1, 1)

    def test_entry_to_dict(self):
        """Test converting entry to dictionary"""
        entry = CryptoRiskEntry(
            cryptocurrency="Ethereum",
            risk_level=RiskLevel.HIGH,
            reporter="John Doe",
            report_date=date(2024, 1, 15),
            description="Test description",
            market_cap=100000.50,
            volatility_index=25.5,
            crowd_sentiment=CrowdSentiment.BEARISH,
            risk_score=75.0,
            entry_id=1,
        )
        data = entry.to_dict()
        
        assert data["entry_id"] == 1
        assert data["cryptocurrency"] == "Ethereum"
        assert data["risk_level"] == "high"
        assert data["reporter"] == "John Doe"
        assert data["report_date"] == "2024-01-15"
        assert data["description"] == "Test description"
        assert data["market_cap"] == 100000.50
        assert data["volatility_index"] == 25.5
        assert data["crowd_sentiment"] == "bearish"
        assert data["risk_score"] == 75.0

    def test_entry_from_dict(self):
        """Test creating entry from dictionary"""
        data = {
            "entry_id": 1,
            "cryptocurrency": "Litecoin",
            "risk_level": "low",
            "reporter": "Jane Smith",
            "report_date": "2024-02-01",
            "description": "Low risk assessment",
            "market_cap": 50000.0,
            "volatility_index": 10.0,
            "crowd_sentiment": "bullish",
            "risk_score": 15.0,
        }
        entry = CryptoRiskEntry.from_dict(data)
        
        assert entry.entry_id == 1
        assert entry.cryptocurrency == "Litecoin"
        assert entry.risk_level == RiskLevel.LOW
        assert entry.reporter == "Jane Smith"
        assert entry.report_date == date(2024, 2, 1)
        assert entry.description == "Low risk assessment"
        assert entry.market_cap == 50000.0
        assert entry.volatility_index == 10.0
        assert entry.crowd_sentiment == CrowdSentiment.BULLISH
        assert entry.risk_score == 15.0

    def test_entry_with_none_sentiment(self):
        """Test entry with no sentiment"""
        entry = CryptoRiskEntry(
            cryptocurrency="Dogecoin",
            risk_level=RiskLevel.CRITICAL,
            reporter="Anonymous",
            report_date=date.today(),
            crowd_sentiment=None,
        )
        data = entry.to_dict()
        assert data["crowd_sentiment"] is None


class TestEnums:
    """Test cases for enumerations"""

    def test_risk_levels(self):
        """Test all risk level values"""
        assert RiskLevel.LOW.value == "low"
        assert RiskLevel.MEDIUM.value == "medium"
        assert RiskLevel.HIGH.value == "high"
        assert RiskLevel.CRITICAL.value == "critical"

    def test_crowd_sentiments(self):
        """Test all crowd sentiment values"""
        assert CrowdSentiment.BULLISH.value == "bullish"
        assert CrowdSentiment.NEUTRAL.value == "neutral"
        assert CrowdSentiment.BEARISH.value == "bearish"
