#!/usr/bin/env python3
"""
Command-line interface for Crypto Crowd Risk application
"""
import argparse
from datetime import date
from crypto_crowd_risk import (
    CryptoRiskEntry, RiskLevel, CrowdSentiment,
    RiskCalculator, Database
)


def add_entry(args):
    """Add a new risk entry"""
    db = Database(args.database)
    
    # Parse risk level
    risk_level = RiskLevel(args.risk_level.lower())
    
    # Parse sentiment if provided
    sentiment = None
    if args.sentiment:
        sentiment = CrowdSentiment(args.sentiment.lower())
    
    # Create entry
    entry = CryptoRiskEntry(
        cryptocurrency=args.cryptocurrency,
        risk_level=risk_level,
        reporter=args.reporter,
        report_date=date.today(),
        description=args.description or "",
        market_cap=args.market_cap or 0.0,
        volatility_index=args.volatility or 0.0,
        crowd_sentiment=sentiment,
    )
    
    entry_id = db.add_entry(entry)
    print(f"✓ Entry added successfully with ID: {entry_id}")
    print(f"  Risk Score: {entry.risk_score}/100")


def list_entries(args):
    """List all or filtered entries"""
    db = Database(args.database)
    
    if args.cryptocurrency:
        entries = db.get_entries_by_crypto(args.cryptocurrency)
        print(f"\n{'='*70}")
        print(f"Risk Entries for {args.cryptocurrency}")
        print(f"{'='*70}")
    else:
        entries = db.get_all_entries()
        print(f"\n{'='*70}")
        print("All Risk Entries")
        print(f"{'='*70}")
    
    if not entries:
        print("No entries found.")
        return
    
    for entry in entries:
        print(f"\nID: {entry.entry_id}")
        print(f"  Cryptocurrency: {entry.cryptocurrency}")
        print(f"  Risk Level: {entry.risk_level.value.upper()}")
        print(f"  Risk Score: {entry.risk_score}/100")
        print(f"  Reporter: {entry.reporter}")
        print(f"  Date: {entry.report_date}")
        if entry.crowd_sentiment:
            print(f"  Sentiment: {entry.crowd_sentiment.value.upper()}")
        if entry.description:
            print(f"  Description: {entry.description}")


def show_stats(args):
    """Show statistics for a cryptocurrency"""
    db = Database(args.database)
    entries = db.get_entries_by_crypto(args.cryptocurrency)
    
    if not entries:
        print(f"No entries found for {args.cryptocurrency}")
        return
    
    avg_risk = RiskCalculator.calculate_average_risk(entries)
    
    print(f"\n{'='*70}")
    print(f"Statistics for {args.cryptocurrency}")
    print(f"{'='*70}")
    print(f"Total Entries: {len(entries)}")
    print(f"Average Risk Score: {avg_risk}/100")
    
    # Count by risk level
    risk_counts = {}
    for entry in entries:
        level = entry.risk_level.value
        risk_counts[level] = risk_counts.get(level, 0) + 1
    
    print("\nRisk Level Distribution:")
    for level, count in sorted(risk_counts.items()):
        print(f"  {level.upper()}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description="Crypto Crowd Risk - Cryptocurrency risk assessment tool"
    )
    parser.add_argument(
        "--database",
        default="data/crypto_risk.db",
        help="Path to database file (default: data/crypto_risk.db)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add entry command
    add_parser = subparsers.add_parser("add", help="Add a new risk entry")
    add_parser.add_argument("cryptocurrency", help="Cryptocurrency name (e.g., Bitcoin)")
    add_parser.add_argument("risk_level", choices=["low", "medium", "high", "critical"],
                           help="Risk level")
    add_parser.add_argument("reporter", help="Reporter name")
    add_parser.add_argument("--description", help="Risk description")
    add_parser.add_argument("--market-cap", type=float, help="Market capitalization")
    add_parser.add_argument("--volatility", type=float, help="Volatility index")
    add_parser.add_argument("--sentiment", choices=["bullish", "neutral", "bearish"],
                           help="Crowd sentiment")
    add_parser.set_defaults(func=add_entry)
    
    # List entries command
    list_parser = subparsers.add_parser("list", help="List risk entries")
    list_parser.add_argument("--cryptocurrency", help="Filter by cryptocurrency")
    list_parser.set_defaults(func=list_entries)
    
    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show statistics")
    stats_parser.add_argument("cryptocurrency", help="Cryptocurrency name")
    stats_parser.set_defaults(func=show_stats)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    args.func(args)


if __name__ == "__main__":
    main()
