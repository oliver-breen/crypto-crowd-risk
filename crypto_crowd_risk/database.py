"""
Database management for crypto risk entries
"""
import json
import sqlite3
from datetime import date
from pathlib import Path
from typing import List, Optional
from .models import CryptoRiskEntry, RiskLevel, CrowdSentiment
from .calculator import RiskCalculator


class Database:
    """
    Manages storage and retrieval of crypto risk entries
    """

    def __init__(self, db_path: str = "data/crypto_risk.db"):
        """
        Initialize database connection
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._create_table()

    def _create_table(self):
        """Create the crypto_risk_entries table if it doesn't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS crypto_risk_entries (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cryptocurrency TEXT NOT NULL,
                    risk_level TEXT NOT NULL,
                    reporter TEXT NOT NULL,
                    report_date TEXT NOT NULL,
                    description TEXT,
                    market_cap REAL,
                    volatility_index REAL,
                    crowd_sentiment TEXT,
                    risk_score REAL
                )
            """)
            conn.commit()

    def add_entry(self, entry: CryptoRiskEntry) -> int:
        """
        Add a new risk entry to the database
        
        Args:
            entry: CryptoRiskEntry to add
            
        Returns:
            ID of the newly created entry
        """
        # Calculate risk score before saving
        entry.risk_score = RiskCalculator.calculate_risk_score(entry)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO crypto_risk_entries 
                (cryptocurrency, risk_level, reporter, report_date, description,
                 market_cap, volatility_index, crowd_sentiment, risk_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entry.cryptocurrency,
                entry.risk_level.value,
                entry.reporter,
                entry.report_date.isoformat(),
                entry.description,
                entry.market_cap,
                entry.volatility_index,
                entry.crowd_sentiment.value if entry.crowd_sentiment else None,
                entry.risk_score,
            ))
            conn.commit()
            return cursor.lastrowid

    def get_entry(self, entry_id: int) -> Optional[CryptoRiskEntry]:
        """
        Retrieve a specific entry by ID
        
        Args:
            entry_id: ID of the entry to retrieve
            
        Returns:
            CryptoRiskEntry or None if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM crypto_risk_entries WHERE entry_id = ?",
                (entry_id,)
            )
            row = cursor.fetchone()
            if row:
                return self._row_to_entry(row)
        return None

    def get_all_entries(self) -> List[CryptoRiskEntry]:
        """
        Retrieve all entries from the database
        
        Returns:
            List of all CryptoRiskEntry objects
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM crypto_risk_entries ORDER BY report_date DESC")
            rows = cursor.fetchall()
            return [self._row_to_entry(row) for row in rows]

    def get_entries_by_crypto(self, cryptocurrency: str) -> List[CryptoRiskEntry]:
        """
        Retrieve all entries for a specific cryptocurrency
        
        Args:
            cryptocurrency: Name of the cryptocurrency
            
        Returns:
            List of CryptoRiskEntry objects
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM crypto_risk_entries WHERE cryptocurrency = ? ORDER BY report_date DESC",
                (cryptocurrency,)
            )
            rows = cursor.fetchall()
            return [self._row_to_entry(row) for row in rows]

    def _row_to_entry(self, row: tuple) -> CryptoRiskEntry:
        """Convert database row to CryptoRiskEntry object"""
        return CryptoRiskEntry(
            entry_id=row[0],
            cryptocurrency=row[1],
            risk_level=RiskLevel(row[2]),
            reporter=row[3],
            report_date=date.fromisoformat(row[4]),
            description=row[5] or "",
            market_cap=row[6] or 0.0,
            volatility_index=row[7] or 0.0,
            crowd_sentiment=CrowdSentiment(row[8]) if row[8] else None,
            risk_score=row[9] or 0.0,
        )

    def export_to_json(self, filepath: str):
        """
        Export all entries to a JSON file
        
        Args:
            filepath: Path to output JSON file
        """
        entries = self.get_all_entries()
        data = [entry.to_dict() for entry in entries]
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
