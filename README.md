
# 📊 Data-Driven Pricing Strategy Framework

A complete, end-to-end **pricing strategy project** developed as part of the  
**Karmic Seed – Operations Analyst (Round 3) Assignment**.

This repository demonstrates how reactive pricing decisions can be replaced with a
**scalable, explainable, and data-driven pricing engine** using real operational data.

---

## 🚀 Project Objective

Consumer brands often struggle with:
- Margin leakage despite healthy sales
- Overstocked or stockout-prone inventory
- Inefficient advertising spend
- Prices drifting away from market benchmarks

The objective of this project is to design a **rule-based pricing framework** that balances:

- 📈 Profitability  
- 📦 Inventory health  
- 📣 Advertising efficiency  
- 🏷️ Competitive positioning  

All pricing decisions are **data-backed, transparent, and reproducible**.

---

## 🧠 Pricing Strategy Overview

The pricing framework is built around five core decision signals:

1. **Margin Protection**
   - Minimum acceptable margin set at **20%**
   - Prevents value leakage

2. **Demand Strength**
   - Sales velocity used to identify weak vs strong demand

3. **Inventory Health**
   - Overstock → discount to accelerate sell-through
   - Stockout risk → price increase to manage demand

4. **Advertising Efficiency**
   - High ACOS triggers ad optimization before price cuts

5. **Competitive Benchmarking**
   - Prices maintained within ±5% of competitor benchmarks

---

## 🔢 Pricing Rules Implemented

| Condition | Action |
|--------|--------|
| Margin < 20% | +7% price increase |
| Low sales velocity (30d < 10) | −7% price reduction |
| Overstocked SKU | −10% price reduction |
| Stockout risk | +5% price increase |
| High ACOS | Hold price, optimize ads |

---

## 📓 Analysis Workbook

The Jupyter notebook:
- Loads and merges all datasets at SKU level
- Creates pricing KPIs
- Visualizes margin leakage, ad inefficiency, and inventory risk
- Applies pricing logic consistently

📁 `notebooks/Updated_Pricing_Analysis.ipynb`

---

## 🐍 Pricing Engine

The pricing engine is implemented as a reusable Python module:

📁 `src/pricing_engine.py`

Key characteristics:
- Rule-based and explainable
- Easy to automate
- Suitable for dashboards or batch processing

---

## 📽️ Presentation & Playbook

- **Executive Presentation:**  
  `presentation/Pricing_Strategy_Presentation_Final.pptx`

- **Pricing Playbook (One-Pager):**  
  `presentation/Pricing_Playbook_One_Pager.pdf`

These artifacts translate analysis into **business-friendly decision tools**.

---

## 📊 Outputs

- **Full SKU Pricing Appendix:**  
  `outputs/SKU_Pricing_Appendix.xlsx`

Contains current price vs recommended price for all SKUs.

---

## 🛠️ Tools & Technologies

- Python (Pandas, Matplotlib)
- Jupyter Notebook
- Microsoft Excel
- Microsoft PowerPoint
- GitHub

---

## 👤 Author

**Sreekumar K S**  
MBA – Business Analytics  
Operations & Pricing Analytics  
📧 sreekumarks147@gmail.com  
🔗 https://linkedin.com/in/sreekumarnamboodiri

---

## 📄 License

MIT License

Copyright (c) 2025 Sreekumar K S

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
