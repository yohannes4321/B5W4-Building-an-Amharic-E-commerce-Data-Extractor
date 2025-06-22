# B5W4: Building an Amharic E-commerce Data Extractor

## 🚀 Overview

This project is part of EthioMart's initiative to centralize data from multiple Telegram-based e-commerce channels in Ethiopia. Our system ingests real-time data from independent vendors and processes it to extract key business entities such as product names, prices, and locations using Amharic Named Entity Recognition (NER). The ultimate goal is to help EthioMart identify the best vendors for financial services and loans.

---

## 📊 Business Need

Telegram is increasingly used for e-commerce in Ethiopia. However, decentralization makes it hard for customers to discover products and compare vendors. EthioMart aims to solve this by creating a centralized hub.

This project addresses the core of that vision:

* Ingesting and preprocessing Telegram data
* Creating a structured, annotated Amharic dataset
* Training and evaluating Amharic NER models
* Providing insights for vendor assessment and business integration

---

## 📂 Data

* **Sources**: Public Ethiopian Telegram e-commerce channels (e.g., ShagerOnlineStore)
* **Types**:

  * Amharic text messages
  * Product images
  * Optional contact and delivery metadata

---

## 🤸️ Knowledge & Skills Used

* Telegram scraping via `telethon`
* Amharic text normalization and tokenization
* CoNLL format annotation for NER
* Fine-tuning transformer models with Hugging Face
* Model evaluation (F1, Precision, Recall)
* Model interpretability: SHAP, LIME

---

## 🎓 Learning Outcomes

By the end of this project, contributors will be able to:

* Extract and structure Amharic data from Telegram
* Apply NER techniques and annotation formats
* Fine-tune multilingual models like XLM-R/mBERT on Amharic text
* Interpret model predictions and evaluate performance
* Link NLP outputs to business use cases like loan scoring

 
 
---

## ✍️ Instructions

### Task 1: Data Ingestion & Preprocessing

* Select at least **5 Telegram channels**
* Build a `telegram_scrapper.py` to collect messages, images, timestamps
* Normalize Amharic text and tokenize messages
* Store data in structured format: separate metadata (timestamp, sender) and content (message)

### Task 2: Label Data in CoNLL Format

* Label 30–50 messages manually with these entity types:

  * `B-Product`, `I-Product`
  * `B-LOC`, `I-LOC`
  * `B-PRICE`, `I-PRICE`
  * `O` for non-entities
* Follow CoNLL format (one token per line + label, blank line separates sentences)
* Save to plain `.txt` file

---

## 📄 Deliverables

| File                       | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| `telegram_scrapper.py`     | Script to ingest and structure Telegram data                 |
| `telegram_data.csv.dvc`    | Data versioning reference (if using DVC)                     |
| `conll_labels.txt`         | 30-50 labeled messages in CoNLL format                       |
| `README.md`                | Project description and summary (this file)                  |
| `.github/workflows/ci.yml` | GitHub Actions workflow for simple CI                        |
| `requirement.txt`          | All required packages (telethon, pandas, transformers, etc.) |

---
