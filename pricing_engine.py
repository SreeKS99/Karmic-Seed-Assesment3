
"""
Pricing Engine
Author: Sreekumar K S

This module implements a rule-based pricing engine designed to
support scalable, explainable pricing decisions.
"""

def recommend_price(
    current_price: float,
    margin_pct: float,
    sales_30d: float,
    inventory_status: str = None,
    high_acos: bool = False
) -> float:
    """
    Returns a recommended price based on business rules.

    Rules:
    - Margin < 20%       -> +7% price increase
    - Low sales velocity -> -7% price reduction
    - Overstocked SKU   -> -10% price reduction
    - Stockout risk     -> +5% price increase
    - High ACOS         -> Hold price, optimize ads first
    """

    price = current_price

    # Margin protection
    if margin_pct < 20:
        return round(price * 1.07, 2)

    # Inventory-led pricing
    if inventory_status == "OVERSTOCK":
        return round(price * 0.90, 2)

    if inventory_status == "STOCKOUT_RISK":
        return round(price * 1.05, 2)

    # Demand-led pricing
    if sales_30d < 10:
        return round(price * 0.93, 2)

    # Default: maintain price
    return round(price, 2)
