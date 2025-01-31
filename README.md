# 🔥 DNS Spoofing Script  

## 📜 Description  
This Python script utilizes **NetfilterQueue** and **Scapy** to perform **DNS spoofing** on a network. The script intercepts DNS requests and sends back a fake DNS response, redirecting traffic to a malicious or custom IP address. This is useful for educational and penetration testing purposes to demonstrate how easily DNS can be hijacked on an unprotected network.  

⚠ **Disclaimer:** This tool is intended for **authorized security testing and educational purposes only**. Unauthorized use on networks you do not own or have explicit permission to test is **illegal** and may result in legal consequences.  

---

## 🚀 Features  
- Intercepts DNS requests using **NetfilterQueue**.
- Spoofs DNS responses with a custom IP address.
- Works with **Scapy** to modify DNS packets on-the-fly.
- Supports real-time packet modification.

---

## 🛠️ Prerequisites  
Before running the script, ensure you have:  
- **Python 3.x** installed  
- **Scapy** and **NetfilterQueue** libraries installed:
    ```bash
    pip install scapy netfilterqueue
    ```
- **Root/Administrator privileges** (for modifying iptables)  

---

## 🎯 Usage  

### 1. **Running the DNS Spoofing Script**  
To run the script, execute the following command:  
```bash
sudo python3 dns_spoofing.py
