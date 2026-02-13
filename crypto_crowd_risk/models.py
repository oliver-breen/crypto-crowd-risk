"""
Data models for crypto risk entries
"""
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class RiskLevel(Enum):
    """Risk level enumeration"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class CrowdSentiment(Enum):
    """Crowd sentiment enumeration"""
    BULLISH = "bullish"
    NEUTRAL = "neutral"
    BEARISH = "bearish"


@dataclass
class CryptoRiskEntry:
    """
    Represents a cryptocurrency risk assessment entry
    """
    cryptocurrency: str
    risk_level: RiskLevel
    reporter: str
    report_date: date
    description: str = ""
    market_cap: float = 0.0
    volatility_index: float = 0.0
    crowd_sentiment: Optional[CrowdSentiment] = None
    risk_score: float = 0.0
    entry_id: Optional[int] = None

    def to_dict(self) -> dict:
        """Convert entry to dictionary"""
        return {
            "entry_id": self.entry_id,
            "cryptocurrency": self.cryptocurrency,
            "risk_level": self.risk_level.value,
            "reporter": self.reporter,
            "report_date": self.report_date.isoformat(),
            "description": self.description,
            "market_cap": self.market_cap,
            "volatility_index": self.volatility_index,
            "crowd_sentiment": self.crowd_sentiment.value if self.crowd_sentiment else None,
            "risk_score": self.risk_score,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CryptoRiskEntry":
        """Create entry from dictionary"""
        return cls(
            entry_id=data.get("entry_id"),
            cryptocurrency=data["cryptocurrency"],
            risk_level=RiskLevel(data["risk_level"]),
            reporter=data["reporter"],
            report_date=date.fromisoformat(data["report_date"]),
            description=data.get("description", ""),
            market_cap=data.get("market_cap", 0.0),
            volatility_index=data.get("volatility_index", 0.0),
            crowd_sentiment=CrowdSentiment(data["crowd_sentiment"]) if data.get("crowd_sentiment") else None,
            risk_score=data.get("risk_score", 0.0),
        )
