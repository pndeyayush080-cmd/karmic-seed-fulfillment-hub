# Fulfillment Hub — Karmic Seed Take-Home Project

A small Streamlit application for XYZ's e-commerce fulfillment process. It brings order status, inventory risk, shipping pickup status and operational exceptions into one simple view.

## What problem does it solve?

XYZ currently relies on spreadsheets and shared folders. The biggest operational problems are poor visibility, missed deadlines, inventory uncertainty, priority orders getting mixed with regular work, and forgotten exceptions.

This prototype focuses on those high-impact problems rather than trying to automate the entire warehouse.

## Main features

- **Dashboard:** order pipeline, key counts and priority orders needing attention.
- **Orders:** search/filter orders and inspect individual order details.
- **Inventory:** identify low stock and possible main/secondary warehouse transfers.
- **Shipping:** track packed boxes, courier pickup status and missed pickups.
- **Exceptions:** one place for delayed orders, priority orders at risk, low stock and missed pickups.

## Run locally

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

4. Open the local URL shown by Streamlit.

## Data

The `data/` folder contains intentionally small dummy datasets for demonstration. They are not real customer or business records.

## Design choices

The application prioritizes visibility and exception handling because those are the problems most directly connected to the scenario. A warehouse user should not have to understand a complicated system to answer three questions: **What needs to happen next? What is at risk? Where is the problem?**

## Limitations / next steps

This is a prototype, not a production warehouse-management system. A production version would connect to the order platform, inventory database and courier APIs; add user roles; maintain an audit trail; persist status changes; and add barcode scanning.
