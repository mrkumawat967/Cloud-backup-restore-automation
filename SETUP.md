# 📘 SETUP.md – Cloud Backup & Restore Automation

## 📌 Step-by-Step Implementation

This document explains the complete process followed to build the Cloud Backup & Restore Automation project using Microsoft Azure.

---

## 🔹 Step 1: Create Storage Account
- Logged into Azure Portal
- Created a Storage Account
- Selected region and resource group

---

## 🔹 Step 2: Create Blob Container
- Opened Storage Account
- Created a container named 'backup-data'
- Set access level to private

---

## 🔹 Step 3: Enable Data Protection
- Enabled Blob Versioning
- Enabled Soft Delete
- Enabled Encryption (default Azure encryption)

---

## 🔹 Step 4: Upload Initial Data
- Uploaded sample files to Blob Storage
- Verified files are stored successfully

---

## 🔹 Step 5: Create Backup Script
- Created a PowerShell script to:
  - Copy files from local system to Blob Storage
  - Maintain backup versions

---

## 🔹 Step 6: Automate Backup
- Used Task Scheduler (Windows) or Cron (Linux)
- Scheduled script to run daily

---

## 🔹 Step 7: Verify Backup Process
- Checked new files in Blob Storage
- Verified version history

---

## 🔹 Step 8: Restore Workflow
- Selected previous file version
- Restored data from Blob Storage to local system

---

## 🔹 Step 9: Test Recovery
- Deleted original files
- Restored from backup
- Verified data integrity

---

## 🔹 Step 10: Security Implementation
- Ensured encryption at rest
- Used secure access keys for storage

---

## 🔹 Step 11: Upload to GitHub
- Uploaded scripts, screenshots, and documentation

---

## ✅ Final Output
- Automated backup system  
- Secure storage with versioning  
- Successful restore and recovery workflow  