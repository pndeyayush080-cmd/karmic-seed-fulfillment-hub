# 5-Minute Walkthrough Script

## 0:00–0:35 — Problem

"I approached this as an operations visibility problem. XYZ is processing a few hundred orders a day, but the process is spread across spreadsheets and shared folders. That makes it difficult to see order status, identify delays, protect priority orders, and know when inventory or courier issues need attention."

## 0:35–1:00 — What I built

"I built a lightweight Fulfillment Hub. Instead of trying to replace every part of the warehouse process, I focused on giving the team one simple operational view of orders, inventory, shipping and exceptions."

## 1:00–2:00 — Dashboard

Show Dashboard.

"The dashboard gives the team a quick status check: today's orders, orders in progress, delayed orders, priority orders, shipped orders and low-stock SKUs. The order pipeline shows where work is accumulating. Below that, I show priority orders and an attention list, because these are the orders most likely to need action."

## 2:00–2:45 — Orders

Open Orders.

"The Orders page allows the user to search and filter by status and priority. Selecting an order gives the key information needed to follow it through the process, including its courier, promised ship time and any issue recorded against it."

## 2:45–3:25 — Inventory

Open Inventory.

"Inventory is separated from orders because the case specifically mentions that stock in the spreadsheet can be missing or inaccurate. I flag SKUs that are at or below their reorder level, and I also flag situations where reserved stock is higher than main-warehouse stock, which may require a transfer from the secondary warehouse."

## 3:25–4:00 — Shipping

Open Shipping.

"The Shipping page tracks the packed box, its location, courier and pickup status. This directly addresses the problem of packed boxes being misplaced and courier pickups being missed."

## 4:00–4:35 — Exceptions

Open Exceptions.

"The Exceptions page is the main operational improvement. Instead of leaving problems in messages or informal conversations, delayed orders, priority orders at risk, low stock and missed pickups become visible work items."

## 4:35–5:00 — Closing

"For this prototype I deliberately kept the application simple because the warehouse team is not very comfortable with technology. In a production version, I would connect it to the order and inventory systems, courier APIs and barcode scanning, and add user roles and an audit trail. The goal of this prototype is to demonstrate the operational workflow and the decisions behind the solution."
