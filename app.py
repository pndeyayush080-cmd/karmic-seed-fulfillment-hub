import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Fulfillment Hub", page_icon="📦", layout="wide")

DATA_DIR = Path(__file__).parent / "data"

@st.cache_data
def load_data():
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    inventory = pd.read_csv(DATA_DIR / "inventory.csv")
    shipping = pd.read_csv(DATA_DIR / "shipping.csv")
    return orders, inventory, shipping

orders, inventory, shipping = load_data()

# ---------- helpers ----------
def status_badge(status):
    colors = {
        "Received": "#64748b", "Processed": "#2563eb", "Picking": "#7c3aed",
        "Packed": "#0891b2", "Staged": "#d97706", "Shipped": "#16a34a",
        "Delayed": "#dc2626"
    }
    c = colors.get(status, "#64748b")
    return f'<span style="background:{c};color:white;padding:4px 9px;border-radius:999px;font-size:12px;font-weight:600">{status}</span>'

# ---------- sidebar ----------
st.sidebar.title("📦 Fulfillment Hub")
st.sidebar.caption("XYZ Operations Console")
page = st.sidebar.radio("Navigate", ["Dashboard", "Orders", "Inventory", "Shipping", "Exceptions"], index=0)
st.sidebar.divider()
st.sidebar.caption("Demo data • Oct 2026")

# ---------- Dashboard ----------
if page == "Dashboard":
    st.title("Fulfillment Hub")
    st.write("A simple operational view for keeping orders, inventory and courier pickups on track.")

    total = len(orders)
    pending = int(orders["Status"].isin(["Received", "Processed", "Picking", "Packed", "Staged"]).sum())
    delayed = int((orders["Status"] == "Delayed").sum())
    priority = int((orders["Priority"] == "High").sum())
    shipped = int((orders["Status"] == "Shipped").sum())
    low_stock = int((inventory["Available_Units"] <= inventory["Reorder_Level"]).sum())

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Orders today", total)
    c2.metric("In progress", pending)
    c3.metric("Delayed", delayed, delta="Needs attention" if delayed else None, delta_color="inverse")
    c4.metric("Priority", priority)
    c5.metric("Shipped", shipped)
    c6.metric("Low stock", low_stock, delta="Check inventory" if low_stock else None, delta_color="inverse")

    st.divider()
    left, right = st.columns([1.15, 1])
    with left:
        st.subheader("Order pipeline")
        pipeline = orders["Status"].value_counts().reindex(
            ["Received", "Processed", "Picking", "Packed", "Staged", "Shipped", "Delayed"], fill_value=0
        )
        st.bar_chart(pipeline)

    with right:
        st.subheader("Priority orders")
        p = orders[orders["Priority"] == "High"].copy()
        p["Status"] = p["Status"].apply(status_badge)
        st.write(p[["Order_ID", "Customer", "Status", "Promised_Ship_Time"]].to_html(escape=False, index=False), unsafe_allow_html=True)

    st.subheader("Today's attention list")
    attention = orders[(orders["Status"] == "Delayed") | ((orders["Priority"] == "High") & (orders["Status"] != "Shipped"))].copy()
    if attention.empty:
        st.success("No urgent issues right now.")
    else:
        attention["Status"] = attention["Status"].apply(status_badge)
        st.write(attention[["Order_ID", "Priority", "Status", "Product", "Promised_Ship_Time", "Issue"]].to_html(escape=False, index=False), unsafe_allow_html=True)

# ---------- Orders ----------
elif page == "Orders":
    st.title("Orders")
    st.write("Search orders and quickly identify priority or delayed work.")

    a, b, c = st.columns(3)
    search = a.text_input("Search order / customer / product")
    status_filter = b.multiselect("Status", sorted(orders["Status"].unique()), default=[], placeholder="All statuses")
    priority_filter = c.multiselect("Priority", sorted(orders["Priority"].unique()), default=[], placeholder="All priorities")

    filtered = orders.copy()
    if status_filter:
        filtered = filtered[filtered["Status"].isin(status_filter)]
    if priority_filter:
        filtered = filtered[filtered["Priority"].isin(priority_filter)]
    if search:
        q = search.lower()
        mask = filtered.astype(str).apply(lambda col: col.str.lower().str.contains(q, na=False)).any(axis=1)
        filtered = filtered[mask]

    st.caption(f"Showing {len(filtered)} of {len(orders)} orders")
    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.subheader("Order detail")
    if not filtered.empty:
        selected = st.selectbox("Select an order", filtered["Order_ID"].tolist())
        row = filtered[filtered["Order_ID"] == selected].iloc[0]
        d1, d2, d3, d4 = st.columns(4)
        d1.metric("Status", row["Status"])
        d2.metric("Priority", row["Priority"])
        d3.metric("Courier", row["Courier"])
        d4.metric("Promised ship", row["Promised_Ship_Time"])
        st.info(f"**Issue / note:** {row['Issue']}")

# ---------- Inventory ----------
elif page == "Inventory":
    st.title("Inventory")
    st.write("See what is available in the main warehouse and where stock needs attention.")

    inv = inventory.copy()
    inv["Stock_Status"] = inv.apply(lambda r: "Reorder" if r["Available_Units"] <= r["Reorder_Level"] else "OK", axis=1)
    inv["Transfer_Needed"] = inv.apply(lambda r: "Yes" if r["Main_Units"] < r["Reserved_Units"] else "No", axis=1)

    c1, c2, c3 = st.columns(3)
    c1.metric("SKUs", len(inv))
    c2.metric("Low-stock SKUs", int((inv["Stock_Status"] == "Reorder").sum()))
    c3.metric("Transfer flags", int((inv["Transfer_Needed"] == "Yes").sum()))

    show_low = st.checkbox("Show only items needing attention")
    view = inv[(inv["Stock_Status"] == "Reorder") | (inv["Transfer_Needed"] == "Yes")] if show_low else inv
    st.dataframe(view, use_container_width=True, hide_index=True)

    st.subheader("Inventory rule")
    st.caption("A SKU is flagged when available units are at or below its reorder level, or when reserved stock is higher than main-warehouse stock and a transfer may be needed.")

# ---------- Shipping ----------
elif page == "Shipping":
    st.title("Shipping & Pickup")
    st.write("Track packed orders through courier handoff and spot missed pickups.")

    s = shipping.copy()
    pickup_issue = int((s["Pickup_Status"] == "Missed").sum())
    ready = int((s["Pickup_Status"] == "Ready").sum())
    collected = int((s["Pickup_Status"] == "Collected").sum())

    c1, c2, c3 = st.columns(3)
    c1.metric("Ready for pickup", ready)
    c2.metric("Collected", collected)
    c3.metric("Missed pickups", pickup_issue, delta="Follow up" if pickup_issue else None, delta_color="inverse")

    st.dataframe(s, use_container_width=True, hide_index=True)

    st.subheader("Courier view")
    courier_summary = s.groupby("Courier").agg(
        Shipments=("Order_ID", "count"),
        Missed_Pickups=("Pickup_Status", lambda x: (x == "Missed").sum())
    ).reset_index()
    st.dataframe(courier_summary, use_container_width=True, hide_index=True)

# ---------- Exceptions ----------
elif page == "Exceptions":
    st.title("Exceptions")
    st.write("A single place for issues that need an operations decision or follow-up.")

    delayed = orders[orders["Status"] == "Delayed"].copy()
    priority_risk = orders[(orders["Priority"] == "High") & (orders["Status"].isin(["Received", "Processed", "Picking", "Packed", "Staged"]))].copy()
    low = inventory[inventory["Available_Units"] <= inventory["Reorder_Level"]].copy()
    missed = shipping[shipping["Pickup_Status"] == "Missed"].copy()

    tabs = st.tabs([f"Delayed ({len(delayed)})", f"Priority at risk ({len(priority_risk)})", f"Low stock ({len(low)})", f"Missed pickup ({len(missed)})"])
    with tabs[0]:
        st.dataframe(delayed, use_container_width=True, hide_index=True)
    with tabs[1]:
        st.dataframe(priority_risk, use_container_width=True, hide_index=True)
    with tabs[2]:
        st.dataframe(low, use_container_width=True, hide_index=True)
    with tabs[3]:
        st.dataframe(missed, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("Why this page exists")
    st.write("The original process handles problems informally, so issues can be forgotten. This view turns exceptions into visible work items that the office or warehouse team can follow up on.")

st.sidebar.divider()
st.sidebar.caption("Built as a take-home project for Karmic Seed — Operations Analyst")
