"""
Risk calculation logic for cryptocurrency risk assessment
"""
from typing import List
from .models import CryptoRiskEntry, RiskLevel, CrowdSentiment


class RiskCalculator:
    """
    Calculates risk scores for cryptocurrency entries
    """

    # Base scores for different risk levels
    RISK_LEVEL_SCORES = {
        RiskLevel.LOW: 20.0,
        RiskLevel.MEDIUM: 45.0,
        RiskLevel.HIGH: 70.0,
        RiskLevel.CRITICAL: 90.0,
    }

    # Sentiment impact on risk score
    SENTIMENT_FACTORS = {
        CrowdSentiment.BULLISH: -10.0,  # Bullish reduces risk
        CrowdSentiment.NEUTRAL: 0.0,
        CrowdSentiment.BEARISH: 10.0,   # Bearish increases risk
    }

    @staticmethod
    def calculate_risk_score(entry: CryptoRiskEntry) -> float:
        """
        Calculate risk score for a crypto risk entry
        
        Args:
            entry: CryptoRiskEntry to calculate score for
            
        Returns:
            Risk score between 0-100
        """
        # Base score from risk level
        base_score = RiskCalculator.RISK_LEVEL_SCORES[entry.risk_level]

        # Volatility factor (0-30 points)
        volatility_factor = min(entry.volatility_index, 30.0)

        # Sentiment factor (-10 to +10 points)
        sentiment_factor = 0.0
        if entry.crowd_sentiment:
            sentiment_factor = RiskCalculator.SENTIMENT_FACTORS[entry.crowd_sentiment]

        # Calculate total risk score
        risk_score = base_score + volatility_factor + sentiment_factor

        # Ensure score is within 0-100 range
        risk_score = max(0.0, min(100.0, risk_score))

        return round(risk_score, 2)

    @staticmethod
    def calculate_average_risk(entries: List[CryptoRiskEntry]) -> float:
        """
        Calculate average risk score from multiple entries
        
        Args:
            entries: List of CryptoRiskEntry objects
            
        Returns:
            Average risk score
        """
        if not entries:
            return 0.0

        total_score = sum(entry.risk_score for entry in entries)
        return round(total_score / len(entries), 2)

    @staticmethod
    def get_risk_by_cryptocurrency(entries: List[CryptoRiskEntry], 
                                   cryptocurrency: str) -> List[CryptoRiskEntry]:
        """
        Filter entries by cryptocurrency name
        
        Args:
            entries: List of all entries
            cryptocurrency: Name of cryptocurrency to filter
            
        Returns:
            Filtered list of entries
        """
        return [entry for entry in entries 
                if entry.cryptocurrency.lower() == cryptocurrency.lower()]
