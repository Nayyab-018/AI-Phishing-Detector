import re
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="AI Phishing URL Detector", page_icon="🛡️")

st.title("🛡️ Real-Time AI Phishing URL Detector")
st.write("Analyze suspicious links using **Lexical Feature Extraction** and **Random Forest**. Built by **Nayyab Faisal**.")

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        1 if url.startswith('https') else 0,
        1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,
        1 if any(word in url.lower() for word in ['login', 'verify', 'bank', 'free', 'update', 'secure']) else 0
    ]

@st.cache_resource
def get_trained_model():
    data = [
        ("https://google.com", 0),
        ("https://kaist.ac.kr", 0),
        ("https://github.com", 0),
        ("https://ibm.com", 0),
        ("https://postech.ac.kr", 0),
        ("https://unist.ac.kr", 0),
        ("https://ewha.ac.kr", 0),
        ("https://skku.edu", 0),
        ("https://python.org", 0),
        ("https://wikipedia.org", 0),
        ("https://stackoverflow.com", 0),
        ("https://coursera.org", 0),
        ("http://free-prize-update-login.com", 1),
        ("http://192.168.1", 1),
        ("http://paypal-account-verify-now@security.net", 1),
        ("http://login-update-your-bank-details.xyz", 1),
        ("http://secure-banking-verification-alert.com", 1),
        ("http://free-iphone-winner-claim-now.info", 1),
        ("http://45.33.22", 1),
        ("http://update-your-password-immediately.net", 1),
        ("http://apple-id-locked-verify-login.com", 1),
        ("http://bankofamerica-secure-login-update.xyz", 1),
        ("http://claim-free-reward@bit-promo.org", 1),
        ("http://103.21.244", 1)
    ]
    X = [extract_features(url) for url, label in data]
    y = [label for url, label in data]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    return clf

model = get_trained_model()

url_input = st.text_input("Enter a URL to inspect:", placeholder="e.g., http://secure-login-update-account.com")

if st.button("Analyze URL", type="primary") and url_input:
    features = extract_features(url_input)
    pred = model.predict([features])[0]
    prob = model.predict_proba([features])[0]

    if pred == 1:
        st.error(f"🚨 PHISHING DETECTED ({prob[1]*100:.1f}% Risk)")
    else:
        st.success(f"✅ SAFE URL ({prob[0]*100:.1f}% Confidence)")
