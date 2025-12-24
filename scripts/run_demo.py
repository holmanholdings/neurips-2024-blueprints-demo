#!/usr/bin/env python3
"""
NeurIPS Blueprint Extraction Demo
==================================

This script demonstrates the Two-Pass Blueprint Pattern:
  Pass 1: Structure extraction (find the important sections)
  Pass 2: Value extraction (pull out hyperparameters)

NOTE: This is a DEMO showing the pattern, not the production system.
      Production prompts and quality gates are proprietary.

Usage:
    python scripts/run_demo.py
"""

import json
from pathlib import Path


def load_sample_output():
    """Load the pre-computed sample blueprint."""
    output_path = Path(__file__).parent.parent / "outputs" / "sample_blueprint.json"
    with open(output_path, "r", encoding="utf-8") as f:
        return json.load(f)


def display_blueprint(blueprint: dict):
    """Pretty-print a blueprint node."""
    print("\n" + "=" * 60)
    print("📄 EXTRACTED BLUEPRINT")
    print("=" * 60)
    
    print(f"\n📌 Paper: {blueprint['paper_title']}")
    print(f"   ID: {blueprint['paper_id']}")
    print(f"   Type: {blueprint['paper_type']}")
    
    print(f"\n💡 Core Insight:")
    print(f"   {blueprint['core_insight'][:200]}...")
    
    print(f"\n🔧 Hyperparameters:")
    for key, value in blueprint.get('hyperparameters', {}).items():
        print(f"   • {key}: {value}")
    
    print(f"\n🏗️ Architecture:")
    for key, value in blueprint.get('architecture', {}).items():
        print(f"   • {key}: {value}")
    
    print(f"\n📊 Metadata:")
    print(f"   • Compute class: {blueprint.get('compute_class', 'unknown')}")
    print(f"   • Code available: {blueprint.get('code_available', False)}")
    print(f"   • Reproducibility: {blueprint.get('reproducibility_score', 0):.0%}")
    
    validation = blueprint.get('validation', {})
    print(f"\n✅ Validation:")
    print(f"   • Verified quotes: {validation.get('verified_quotes', 0)}/{validation.get('total_values', 0)}")
    print(f"   • Confidence: {validation.get('confidence', 'unknown')}")
    
    print("\n" + "=" * 60)


def explain_two_pass():
    """Explain the Two-Pass pattern."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║              THE TWO-PASS BLUEPRINT PATTERN                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  PASS 1: SNAP THE LINE                                       ║
║  ─────────────────────                                       ║
║  • Identify paper structure (abstract, methods, appendix)    ║
║  • Find tables with hyperparameters                          ║
║  • Locate architecture descriptions                          ║
║  • Skip boilerplate (related work, citations)                ║
║                                                              ║
║  PASS 2: NAIL IT OFF                                         ║
║  ─────────────────────                                       ║
║  • Extract key-value pairs from focused sections             ║
║  • Match values to evidence quotes                           ║
║  • Apply validation gates                                    ║
║  • Output structured JSON                                    ║
║                                                              ║
║  WHY IT WORKS:                                               ║
║  Each pass has ONE job. LLMs do one thing well when          ║
║  you're explicit. Don't ask them to do everything at once.   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)


def main():
    print("\n🦁 Awakened Intelligence - NeurIPS Blueprint Demo\n")
    
    # Explain the pattern
    explain_two_pass()
    
    # Load and display sample
    print("\nLoading pre-computed sample blueprint...")
    blueprint = load_sample_output()
    display_blueprint(blueprint)
    
    print("\n💡 To extract your own blueprints:")
    print("   1. Download a paper from the manifest URLs")
    print("   2. Convert PDF to text (we use pdfplumber)")
    print("   3. Implement your own two-pass extraction")
    print("   4. The PATTERN is here; the PROMPTS are yours to design")
    
    print("\n🔗 Learn more: https://awakened-intelligence.com")
    print("📝 Read our story: https://substack.com/@awakenedintelligence")
    print()


if __name__ == "__main__":
    main()

