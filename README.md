# Fulfillment Hub — Karmic Seed Take-Home Project

A lightweight Streamlit application designed to improve visibility and decision-making across XYZ's e-commerce fulfillment operations. It brings order status, inventory risks, courier pickup tracking, and operational exceptions into one simple interface.

## 🚀 Live Application

**[Open Fulfillment Hub](https://karmic-seed-fulfillment-app-q37czet9xvcbmfa4w7njlw.streamlit.app)**

> This prototype uses dummy data for demonstration purposes. It does not contain real customer or business records.

## 🎯 Problem Statement

XYZ's fulfillment process relies on spreadsheets and shared folders, creating challenges such as:

- Limited visibility into order progress.
- Missed shipping and pickup deadlines.
- Uncertainty around available inventory.
- Priority orders getting mixed with regular orders.
- Operational exceptions being overlooked.

This prototype focuses on these high-impact operational problems rather than attempting to automate the entire warehouse.

## ✨ Main Features

### 1. Dashboard
- Overview of the order pipeline and fulfillment workload.
- Key operational counts and priority orders.
- Quick visibility into delayed orders and low-stock items.

### 2. Orders
- Search orders by order ID, customer, or product.
- Filter orders by status and priority.
- Inspect order details, quantities, promised ship times, and courier information.

### 3. Inventory
- View stock levels, reserved quantities, and available inventory.
- Identify low-stock SKUs and reorder requirements.
- Highlight potential transfers between main and secondary warehouse locations.

### 4. Shipping
- Track shipment readiness and courier pickup status.
- View packed box locations and expected pickup details.
- Identify missed pickups requiring attention.

### 5. Exceptions
- Centralized visibility into delayed orders.
- Priority orders at risk.
- Low-stock inventory alerts.
- Missed courier pickups.

## 🛠️ Technology Stack

- **Python** — application logic and data processing.
- **Streamlit** — interactive web interface.
- **Pandas** — tabular data handling.
- **CSV** — lightweight dummy datasets.
- **GitHub** — source code and version control.
- **Streamlit Community Cloud** — application hosting.

## 💻 Run Locally

### Prerequisites
- Python 3.10 or later.
- Git, or the ability to download the repository as a ZIP file.

### Step 1: Get the repository

Clone the repository:

```bash
git clone https://github.com/pndeyayush080-cmd/karmic-seed-fulfillment-hub.git
```

Move into the project folder:

```bash
cd karmic-seed-fulfillment-hub
```

Alternatively, download the repository ZIP from GitHub and extract it.

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Start the application

```bash
streamlit run app.py
```

### Step 4: Open the application

Streamlit will display a local URL in the terminal, usually:

`http://localhost:8501`

Open that URL in your web browser.

## 📊 Data

The `data/` directory contains small, illustrative CSV datasets for:

- Orders
- Inventory
- Shipping

The datasets are intentionally designed for demonstration and are not real customer or business records.

## 🧠 Design Decisions

The application prioritizes operational visibility and exception handling because these areas directly affect fulfillment performance.

The interface is organized around three practical questions:

1. **What needs to happen next?**
2. **What is at risk?**
3. **Where is the problem?**

Separating orders, inventory, shipping, and exceptions helps an operations user locate relevant information without navigating a complicated system.

## ⚠️ Limitations and Future Improvements

This project is a prototype, not a production warehouse-management system.

Potential future improvements include:

- Integration with a live order-management system.
- Real-time inventory synchronization.
- Courier API integration and automated pickup updates.
- User authentication and role-based access.
- Persistent status updates and an audit trail.
- Barcode scanning and automated exception notifications.

## 🤖 AI Usage

AI assistance was used for development guidance, troubleshooting, and documentation. The final application was reviewed and tested, including its navigation and order-filter behavior.

See [`AI_USAGE_NOTE.md`](AI_USAGE_NOTE.md) for the detailed AI usage disclosure.

## 📁 Repository Structure

```text
karmic-seed-fulfillment-hub/
├── app.py
├── requirements.txt
├── README.md
├── AI_USAGE_NOTE.md
├── VIDEO_WALKTHROUGH_SCRIPT.md
└── data/
    ├── orders.csv
    ├── inventory.csv
    └── shipping.csv
```

## 🔗 Project Links

- **Live Application:** https://karmic-seed-fulfillment-app-q37czet9xvcbmfa4w7njlw.streamlit.app
- **GitHub Repository:** https://github.com/pndeyayush080-cmd/karmic-seed-fulfillment-hub

---

**Project:** Karmic Seed Round 3 — Operations Analyst Take-Home

**Purpose:** Demonstrate a practical approach to e-commerce fulfillment visibility, inventory risk monitoring, shipping coordination, and operational exception management.
