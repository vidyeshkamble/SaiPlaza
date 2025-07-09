# SaiPlaza

SaiPlaza is a web application designed to calculate and manage monthly maintenance payments for housing societies. It includes digital billing, record tracking, and UPI-based payment gateway integration.


## 📌 Purpose

- Automatically calculate and display monthly maintenance per flat
- Let users log in securely using their flat number and password
- Enable UPI-based payments (like PhonePe or Google Pay)
- Admin panel to track paid/unpaid bills
- Email/SMS reminders and downloadable receipts


## 🔧 Features

- 📅 Monthly maintenance calculation per flat
- 💳 Integrated UPI payment gateway (e.g., PhonePe, Google Pay)
- 📊 Admin dashboard for viewing paid/pending bills
- 🧾 Downloadable receipts and invoices
- 📬 Email/SMS reminders for dues
- 🔐 Secure login for admin and users


## 🖼️ Login UI

Here's a screenshot of the resident login screen:

![Login Screen](myvidyesh.pythonanywhere.com_(iPhone%2012%20Pro).png)

## 🚀 Getting Started

### Requirements
- Python 3.x
- Flask
- MySQL
- pdfkit
- Flask-Mail
- OpenCV (for barcode scanning, if used)
- UPI gateway (PhonePe integration)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/vidyeshkamble/SaiPlaza.git
cd SaiPlaza
pip install -r requirements.txt
python app.py
