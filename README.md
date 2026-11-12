# 🛡️ AI-Powered Phishing URL Detector & IoT Security Alert

**Developed by:** Nayyab Faisal  
**Focus Areas:** Artificial Intelligence, Machine Learning, Cybersecurity & Embedded Systems

---

## 📌 Project Overview
Phishing attacks remain one of the most common cybersecurity threats online. This project uses a **Random Forest Machine Learning classifier** built in Python (`scikit-learn`) to inspect website URLs and identify malicious or deceptive links in real time. 

By extracting structural and security indicators—such as URL length, dot/hyphen frequency, `@` symbol obfuscation, HTTPS encryption status, raw IP address usage, and high-risk keywords—the model calculates an instant risk probability score.

---

## ⚙️ Key Features & Architecture
* **Lexical Feature Extraction:** Parses raw URL strings using Regular Expressions (`re`) to detect suspicious patterns.
* **Machine Learning Classification:** Trained a Random Forest model to distinguish legitimate academic/tech domains from fraudulent phishing URLs.
* **Real-Time Risk Scoring:** Outputs clear safety confidence percentages (`SAFE` vs. `PHISHING`) for instant verification.

---

## 📊 Verified Test Results

| Target URL | Prediction | Confidence Score |
| :--- | :--- | :--- |
| `https://kaist.ac.kr` | ✅ **SAFE** | **92.0%** Safe |
| `http://free-iphone-winner-claim-now.info` | 🚨 **PHISHING** | **98.0%** Risk |
| `http://security-alert-verify-account.com` | 🚨 **PHISHING** | **98.0%** Risk |

---

## 🛠️ Tech Stack & Tools
* **Programming:** Python 3, C++ (Arduino)
* **Libraries:** `scikit-learn`, `re`
* **Environments:** Google Colab, GitHub, Tinkercad Circuits

---

## 🎓 Verified IBM SkillsBuild Certifications
This project applies concepts earned through verified IBM credentials:
* **Cybersecurity Fundamentals** — [Verify Badge](https://credly.com)
* **Lab: Explore Machine Learning and Data Science in IBM watsonx**
* **Foundations of Artificial Intelligence & Applying Artificial Intelligence**
