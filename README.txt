CHAT API DEMO — FICTIONAL DATA ONLY

Run on Ubuntu/Kali:
1. Extract the ZIP and open a terminal in this folder.
2. python3 -m venv .venv
3. source .venv/bin/activate
4. pip install -r requirements.txt
5. python api.py

Test:
http://127.0.0.1:5000/api/chats?phone=9000000001
http://127.0.0.1:5000/api/chats?phone=9000000002

Or:
curl "http://127.0.0.1:5000/api/chats?phone=9000000001"

Edit chats.txt to add fictional phone numbers and messages. The API reads
the TXT file on every request, so edits appear immediately.

This is a local educational simulation. It does not connect to WhatsApp
or retrieve anyone's private messages. It binds to 127.0.0.1 only.
