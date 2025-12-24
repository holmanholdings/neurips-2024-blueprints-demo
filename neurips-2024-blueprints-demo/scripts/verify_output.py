#!/usr/bin/env python3
"""
Blueprint Verification Demo
============================

Shows how we validate extracted values against source text.
Production validation includes multi-agent review ("Black Lion Gaze").

This demo shows the CONCEPT, not the implementation.
"""

import json
from pathlib import Path


def load_blueprint():
    """Load the sample blueprint."""
    path = Path(__file__).parent.parent / "outputs" / "sample_blueprint.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def verify_blueprint(blueprint: dict) -> dict:
    """
    Demonstrate verification logic.
    
    In production, we:
    1. Match each extracted value to a quote in the source
    2. Check quote actually exists in paper text
    3. Flag hallucinated values for review
    4. Calculate reproducibility score
    
    This demo shows the structure, not the implementation.
    """
    results = {
        "paper_id": blueprint["paper_id"],
        "checks_passed": [],
        "checks_failed": [],
        "warnings": []
    }
    
    # Check: Has hyperparameters
    hp = blueprint.get("hyperparameters", {})
    if len(hp) >= 3:
        results["checks_passed"].append("✅ Has 3+ hyperparameters")
    else:
        results["checks_failed"].append("❌ Insufficient hyperparameters")
    
    # Check: Learning rate is reasonable
    lr = hp.get("learning_rate", "0")
    try:
        lr_val = float(lr)
        if 1e-6 <= lr_val <= 1.0:
            results["checks_passed"].append("✅ Learning rate in valid range")
        else:
            results["warnings"].append("⚠️ Learning rate outside typical range")
    except ValueError:
        results["checks_failed"].append("❌ Learning rate not a valid number")
    
    # Check: Has validation data
    val = blueprint.get("validation", {})
    if val.get("verified_quotes", 0) > 0:
        results["checks_passed"].append("✅ Has verified quotes")
    else:
        results["warnings"].append("⚠️ No verified quotes found")
    
    # Check: Paper type makes sense
    if blueprint.get("paper_type") == "empirical" and len(hp) > 0:
        results["checks_passed"].append("✅ Empirical paper has hyperparams")
    elif blueprint.get("paper_type") == "theoretical" and len(hp) == 0:
        results["checks_passed"].append("✅ Theoretical paper (no hyperparams expected)")
    
    return results


def main():
    print("\n🔍 Blueprint Verification Demo\n")
    print("=" * 50)
    
    blueprint = load_blueprint()
    results = verify_blueprint(blueprint)
    
    print(f"\nPaper: {blueprint['paper_title']}")
    print(f"ID: {results['paper_id']}\n")
    
    if results["checks_passed"]:
        print("Passed:")
        for check in results["checks_passed"]:
            print(f"  {check}")
    
    if results["warnings"]:
        print("\nWarnings:")
        for warn in results["warnings"]:
            print(f"  {warn}")
    
    if results["checks_failed"]:
        print("\nFailed:")
        for fail in results["checks_failed"]:
            print(f"  {fail}")
    
    total = len(results["checks_passed"]) + len(results["checks_failed"])
    passed = len(results["checks_passed"])
    print(f"\n📊 Score: {passed}/{total} checks passed")
    
    print("\n" + "=" * 50)
    print("💡 Production verification includes:")
    print("   • Multi-agent review (Black Lion Gaze)")
    print("   • Quote matching against source text")
    print("   • Hallucination detection")
    print("   • Cross-paper consistency checks")
    print()


if __name__ == "__main__":
    main()

