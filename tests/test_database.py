"""
Unit tests for database operations
"""
import pytest
import json
import tempfile
import os
from datetime import date
from pathlib import Path
from crypto_crowd_risk import (
    CryptoRiskEntry, RiskLevel, CrowdSentiment, Database
)


class TestDatabase:
    """Test cases for Database class"""

    @pytest.fixture
    def temp_db(self):
        """Create a temporary database for testing"""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = os.path.join(tmpdir, "test.db")
            yield Database(db_path)

    def test_add_and_retrieve_entry(self, temp_db):
        """Test adding and retrieving an entry"""
        entry = CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="Test User",
            report_date=date.today(),
            volatility_index=10.0,
        )
        
        entry_id = temp_db.add_entry(entry)
        assert entry_id > 0
        
        retrieved = temp_db.get_entry(entry_id)
        assert retrieved is not None
        assert retrieved.cryptocurrency == "Bitcoin"
        assert retrieved.risk_level == RiskLevel.MEDIUM
        assert retrieved.risk_score > 0  # Should be calculated

    def test_get_all_entries(self, temp_db):
        """Test retrieving all entries"""
        entries = [
            CryptoRiskEntry(
                cryptocurrency="Bitcoin",
                risk_level=RiskLevel.HIGH,
                reporter="User1",
                report_date=date.today(),
            ),
            CryptoRiskEntry(
                cryptocurrency="Ethereum",
                risk_level=RiskLevel.LOW,
                reporter="User2",
                report_date=date.today(),
            ),
        ]
        
        for entry in entries:
            temp_db.add_entry(entry)
        
        all_entries = temp_db.get_all_entries()
        assert len(all_entries) == 2

    def test_get_entries_by_crypto(self, temp_db):
        """Test filtering entries by cryptocurrency"""
        temp_db.add_entry(CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.HIGH,
            reporter="User1",
            report_date=date.today(),
        ))
        temp_db.add_entry(CryptoRiskEntry(
            cryptocurrency="Ethereum",
            risk_level=RiskLevel.LOW,
            reporter="User2",
            report_date=date.today(),
        ))
        temp_db.add_entry(CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.MEDIUM,
            reporter="User3",
            report_date=date.today(),
        ))
        
        bitcoin_entries = temp_db.get_entries_by_crypto("Bitcoin")
        assert len(bitcoin_entries) == 2
        assert all(e.cryptocurrency == "Bitcoin" for e in bitcoin_entries)

    def test_export_to_json(self, temp_db):
        """Test JSON export functionality"""
        # Add some entries
        temp_db.add_entry(CryptoRiskEntry(
            cryptocurrency="Bitcoin",
            risk_level=RiskLevel.HIGH,
            reporter="User1",
            report_date=date(2024, 1, 1),
            description="Test entry",
            volatility_index=20.0,
            crowd_sentiment=CrowdSentiment.BEARISH,
        ))
        temp_db.add_entry(CryptoRiskEntry(
            cryptocurrency="Ethereum",
            risk_level=RiskLevel.LOW,
            reporter="User2",
            report_date=date(2024, 1, 2),
        ))
        
        # Export to JSON
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json_path = f.name
        
        try:
            temp_db.export_to_json(json_path)
            
            # Verify file exists and has correct content
            assert os.path.exists(json_path)
            
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            assert len(data) == 2
            assert data[0]['cryptocurrency'] == "Ethereum"  # Ordered by date DESC
            assert data[1]['cryptocurrency'] == "Bitcoin"
            assert data[0]['reporter'] == "User2"
            assert data[1]['description'] == "Test entry"
            
        finally:
            if os.path.exists(json_path):
                os.unlink(json_path)
