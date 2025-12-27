# Value Predictor (Statistics)

A simple Flask web app that uses **linear regression formulas from statistics**
to:

- Predict **X from Y**
- Predict **Y from X**
- Compute **correlation coefficient (r)**

## Math Used

- Regression coefficients:
  - bxy = (NΣXY − ΣX.ΣY) / (NΣY² − (ΣY)²)
  - byx = (NΣXY − ΣX.ΣY) / (NΣX² − (ΣX)²)

- Regression lines:
  - x − x̄ = bxy(y − ȳ)
  - y − ȳ = byx(x − x̄)

- Correlation:
  - r = ±√(bxy · byx)

## How to Run

```bash
pip install flask
python app.py
