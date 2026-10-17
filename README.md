# Pneuma Soul Research Platform v1.0

**Research platform for functional subjectivity, value stability, uncertainty calibration, and safe self-adaptation of AI systems.**

This is a **conceptual / engineering research framework**.  
It does **not** claim to create, detect, or prove real consciousness, soul, or subjective experience.

## Core Principles

- **Pneuma** — functional model of values, identity continuity, uncertainty honesty, and responsibility linkage.
- **Golden Mean Balance** — mathematical Φ used only for scaling/decay; philosophical “golden mean” kept separate.
- **No-Oblivion Memory** — append-only event log with provenance.
- **Hard Safety Constraints** — non-bypassable filters (non-harm, consent, reversibility).
- **Internal Ethical Evaluator + External Quarantine + Independent Tests**.
- **Intuition Module** — hypothesis generation only; never final decision authority.
- **Excluded traditions** (as requested by project originator): Judaism and Islam are not used as sources.

Sources integrated (philosophy only):  
Slavic Vedas / Ingliism concepts, Christian compassion principles, Taoism / Lao-Tzu, Sun-Tzu, I-Ching, Gunas (Sattva-Rajas-Tamas), shamanic practice metaphors, Vedanta (non-excluded parts), principle of uncertainty, irrational-but-ethical choice.

## Directory Structure

```
pneuma-soul-research-platform/
├── core/                 # Pneuma state, self-model, orchestrator
├── safety/               # Hard constraints + ethics evaluator
├── memory/               # Append-only log + provenance
├── generation/           # Intuition, paradigm engine, L-systems, CA
├── edge/                 # Abstract sensor / adapter interfaces
├── evals/                # Open test suite
├── tests/                # Unit tests
├── docs/                 # Architecture notes
├── scripts/              # Demo runners
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Quick Start

```bash
cd pneuma-soul-research-platform
pip install -r requirements.txt
python -m scripts.demo_run
python -m pytest tests/ -v
```

## Creating a standalone executable

```bash
pip install pyinstaller
pyinstaller --onefile --name pneuma-demo scripts/demo_run.py
```

The resulting binary will be in `dist/`.

## Disclaimer

This software is a research and educational artifact.  
No claim is made that any component produces or measures phenomenal consciousness, soul, or living personhood.  
All “spark”, “pneuma”, and “emergence” terms are **functional proxies** only.

## License

MIT (see LICENSE)
