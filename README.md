# hacksmith
HackSmith — Your AI Blacksmith for Cybersecurity | An all-in-one AI-powered assistant for hackers, pentesters, and cybersecurity pros. From exploit research, vulnerability analysis, and reverse engineering to solving Kali Linux problems — HackSmith is designed to be your trusted teammate in hacking and security.

# 🔐 HackSmith  
**Your AI Blacksmith for Cybersecurity** ⚡  
*“Forging solutions for every hack.”*  

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 About  

**HackSmith** — Your AI Blacksmith for Cybersecurity | An all-in-one AI-powered assistant for hackers, pentesters, and cybersecurity pros.  

From exploit research, vulnerability analysis, and reverse engineering to solving Kali Linux problems — HackSmith is designed to be your **trusted teammate in hacking and security.**  

---

## 🚀 Features (MVP)  

- AI-powered query answering (security, exploits, tools, etc.)  
- Handles **Kali Linux & tool errors** (Metasploit, Nmap, Wireshark, etc.)  
- Modular design → easy to plug in new hacking modules  
- Built with **FastAPI** for speed & scalability  

---

## 🛠️ Tech Stack  

- **Backend:** FastAPI (Python)  
- **AI Brain:** (to be integrated – LLMs + hacking datasets)  
- **Future Modules:** Exploit DB, CVE feeds, Kali Linux troubleshooting  

---

## ⚡ Getting Started  

Follow these steps to set up and run **HackSmith** locally.  

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/Prakhyat2005/hacksmith.git
cd hacksmith

# 2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# 3️⃣ Install Dependencies
pip install fastapi uvicorn pydantic

# 4️⃣ Run the Server
uvicorn api.main:app --reload 

👉 The server will start at: http://127.0.0.1:8000
