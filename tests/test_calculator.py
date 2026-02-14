"""
Unit tests for crypto risk calculator
"""
import pytest
from datetime import date
from crypto_crowd_risk import (
    CryptoRiskEntry, RiskLevel, CrowdSentiment, RiskCalculator
)


class TestRiskCalculator:
    """Test cases for RiskCalculator"""

    def test_calculate_risk_score_low_risk(self):
        """Test risk score calculation for low risk level"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.LOW,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=0.0,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 20.0

    def test_calculate_risk_score_high_risk(self):
        """Test risk score calculation for high risk level"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.HIGH,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=0.0,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 70.0

    def test_calculate_risk_score_with_volatility(self):
        """Test risk score with volatility factor"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=15.0,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 60.0  # 45 base + 15 volatility

    def test_calculate_risk_score_with_bullish_sentiment(self):
        """Test risk score with bullish sentiment"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=0.0,
            crowd_sentiment=CrowdSentiment.BULLISH,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 35.0  # 45 base - 10 bullish

    def test_calculate_risk_score_with_bearish_sentiment(self):
        """Test risk score with bearish sentiment"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=0.0,
            crowd_sentiment=CrowdSentiment.BEARISH,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 55.0  # 45 base + 10 bearish

    def test_calculate_risk_score_max_cap(self):
        """Test risk score caps at 100"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.CRITICAL,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=50.0,  # High volatility
            crowd_sentiment=CrowdSentiment.BEARISH,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 100.0  # Capped at 100

    def test_calculate_risk_score_min_cap(self):
        """Test risk score doesn't go below 0"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.LOW,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=0.0,
            crowd_sentiment=CrowdSentiment.BULLISH,
        )
        score = RiskCalculator.calculate_risk_score(entry)
        assert score == 10.0  # 20 base - 10 bullish

    def test_calculate_average_risk(self):
        """Test average risk calculation"""
        entries = [
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.LOW,
                reporter="User1",
                report_date=date.today(),
                risk_score=20.0,
            ),
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.HIGH,
                reporter="User2",
                report_date=date.today(),
                risk_score=70.0,
            ),
        ]
        avg = RiskCalculator.calculate_average_risk(entries)
        assert avg == 45.0

    def test_get_risk_by_cryptocurrency(self):
        """Test filtering by cryptocurrency"""
        entries = [
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.LOW,
                reporter="User1",
                report_date=date.today(),
            ),
            CryptoRiskEntry(
                cryptocurrency="Ethereum",
                risk_level=RiskLevel.HIGH,
                reporter="User2",
                report_date=date.today(),
            ),
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.MEDIUM,
                reporter="User3",
                report_date=date.today(),
            ),
        ]
        bitcoin_entries = RiskCalculator.get_risk_by_cryptocurrency(entries, "Bitcoin")
        assert len(bitcoin_entries) == 2
        assert all(e.cryptocurrency == "Bitcoin" for e in bitcoin_entries)

    def test_risk_score_rounding(self):
        """Test that risk scores are rounded to 2 decimal places"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=15.777,  # Will produce decimals
        )
        score = RiskCalculator.calculate_risk_score(entry)
        # Check it's rounded to 2 decimal places
        assert score == round(score, 2)
        assert len(str(score).split('.')[-1]) <= 2

    def test_average_risk_rounding(self):
        """Test that average risk is rounded to 2 decimal places"""
        entries = [
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.LOW,
                reporter="User1",
                report_date=date.today(),
                risk_score=20.0,
            ),
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.HIGH,
                reporter="User2",
                report_date=date.today(),
                risk_score=71.0,
            ),
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.MEDIUM,
                reporter="User3",
                report_date=date.today(),
                risk_score=48.0,
            ),
        ]
        # Average of 20, 71, 48 = 46.333... (repeating decimal)
        avg = RiskCalculator.calculate_average_risk(entries)
        assert avg == 46.33
        assert len(str(avg).split('.')[-1]) <= 2
