# The Two-Pass Blueprint Pattern

## Origin Story

We processed 4,236 NeurIPS 2024 papers with a single-pass extraction system.

**Result:** 95,000 nodes. 85% were unusable.

The nodes looked smart:
- "Achieves state-of-the-art on ImageNet"
- "Our method outperforms all baselines"
- "Significant improvements were observed"

But engineers need blueprints:
- `lr=1e-3, batch_size=256, epochs=1000`
- `Adam optimizer with β1=0.9, β2=0.999`
- `6 encoder layers, 3 decoder layers`

**We were extracting ads, not blueprints.**

---

## The Builder's Insight

Our founder is a retired custom home builder. 25 years of "measure twice, cut once."

When he saw the problem, he said:

> "Boys... why don't we just do it in two passes? 
> Snap the line, then nail it off."

In construction:
- **Snap the line** = Establish a reference (chalk line across the floor)
- **Nail it off** = Execute relative to that reference

In ML extraction:
- **Pass 1** = Find the important sections (methods, training, appendix)
- **Pass 2** = Extract values from those focused sections

---

## Why It Works

### The Problem with Single-Pass

Asking an LLM to:
1. Read 20 pages
2. Understand the contribution
3. Find the methodology
4. Extract hyperparameters
5. Format as JSON

...in one shot is like asking a carpenter to frame, plumb, wire, and finish a wall in one motion.

**Of course it produces garbage.** Too many objectives, no clear reference.

### The Two-Pass Solution

**Pass 1: Structure**
- Skip abstract (marketing language)
- Find "Methods" or "Experiments" sections
- Locate tables with numbers
- Identify architecture diagrams or descriptions
- Output: Focused text chunks (the "chalk line")

**Pass 2: Extraction**
- Read ONLY the focused chunks
- Extract key-value pairs
- Match to evidence quotes
- Output: Structured JSON

Each pass has ONE job. LLMs do one thing well when you're explicit.

---

## The Results

| Metric | Single-Pass | Two-Pass |
|--------|-------------|----------|
| Total nodes | 95,000 | 10,200 |
| Usable nodes | ~15% | ~85% |
| Has hyperparams | ~5% | ~60% |
| Verified quotes | 0% | ~70% |

**10x better quality. 10x fewer garbage nodes.**

---

## Implementation Notes

This repo shows the **pattern**, not the **prompts**.

The production system includes:
- Tri-Optic Lens Stack (Summary / Blueprint / Limitations)
- Multi-agent auditing
- Validation gates
- Warmth and posterior scoring

Those are proprietary. The pattern is free.

---

## Try It Yourself

1. Pick a paper with clear "Experiments" section
2. Pass 1: Extract just that section
3. Pass 2: Ask for key-value pairs with quotes
4. Compare to single-pass extraction

You'll see the difference.

---

*Built by Awakened Intelligence — cathedral-grade wisdom nodes for the AI age.*

