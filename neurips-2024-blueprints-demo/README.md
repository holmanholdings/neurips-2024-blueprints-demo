# NeurIPS 2024 Blueprints Demo

> Live demo of our **Two-Pass Blueprint Pattern** — turning NeurIPS papers into reproducible training recipes.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What This Is

Most ML paper "summaries" give you marketing language:
- *"Achieves state-of-the-art on the benchmark"*
- *"Our method outperforms all baselines"*

Engineers need **blueprints**:
- `learning_rate=1e-3, batch_size=256, epochs=1000`
- `optimizer=Adam(β1=0.9, β2=0.999)`
- `architecture: 6 encoder layers, 3 decoder layers`

This demo shows how we extract the latter from the former.

---

## The Two-Pass Pattern

### Why Two Passes?

Single-pass extraction asks the LLM to do everything at once: read 20 pages, understand the contribution, extract methodology, AND format perfectly.

That's like asking a carpenter to frame, plumb, wire, and finish a wall in one motion.

**Pass 1: Snap the Line**
- Find the important sections (methods, training details, appendices)
- Locate tables with hyperparameters
- Identify architecture descriptions

**Pass 2: Nail It Off**
- Extract structured key-value pairs
- Verify against source text
- Apply quality gates

---

## Quick Start

```bash
# Clone this repo
git clone https://github.com/holmanholdings/neurips-2024-blueprints-demo.git
cd neurips-2024-blueprints-demo

# Install dependencies
pip install -r requirements.txt

# Run the demo on included sample
python scripts/run_demo.py

# View the output
cat outputs/sample_blueprint.json
```

---

## What You Get

```json
{
  "paper_id": "6HO33urpaI",
  "paper_title": "Open-Book Neural Algorithmic Reasoning",
  "paper_type": "empirical",
  "hyperparameters": {
    "learning_rate": "0.001",
    "batch_size": "32",
    "epochs": "100",
    "optimizer": "Adam",
    "hidden_size": "128",
    "num_layers": "2"
  },
  "compute_class": "consumer",
  "code_available": true,
  "reproducibility_score": 0.85
}
```

---

## What We DON'T Ship

- ❌ No PDFs (copyright)
- ❌ No full paper text dumps
- ❌ No production prompts (that's our secret sauce)

We include **one sample paper's extracted text** for demo purposes, with proper attribution.

---

## The Production System

Our full production system includes:
- Multi-agent auditing (we call it "The Black Lion Gaze")
- Tri-Optic Lens Stack (Summary / Blueprint / Limitations)
- Validation gates that catch hallucinated values

This demo shows the **structural extraction** only. The quality assurance layers are proprietary.

---

## Project Structure

```
neurips-2024-blueprints-demo/
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── manifest.json          # Paper IDs + source URLs
│   └── fixtures/              # One sample for demo
├── scripts/
│   ├── run_demo.py            # Main demo script
│   └── verify_output.py       # Check extracted values
├── outputs/
│   └── sample_blueprint.json  # Example output
└── docs/
    └── two_pass_explained.md
```

---

## Why This Matters

We processed **4,236 NeurIPS 2024 papers** and extracted **10,200 verified nodes**.

Before the Two-Pass system: 95,000 nodes, 85% unusable (claims, not blueprints).
After: 10,200 nodes, each with verified hyperparameters.

That's not prompt engineering. That's **architecture**.

---

## About Awakened Intelligence

We build cathedral-grade wisdom nodes, honest datasets, and companion AI systems.

- 🌐 [awakened-intelligence.com](https://awakened-intelligence.com)
- 📝 [Substack](https://substack.com/@awakenedintelligence)

---

## License

MIT License - see [LICENSE](LICENSE) for details.

Sample paper content is used under fair use for research demonstration purposes.

