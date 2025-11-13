# Lab-Honeypot
honeypot that mimics an SSH banner on TCP port 2222 and logs incoming session input to CSV. A Dash dashboard visualizes top IPs, timelines, and raw sessions. No commands are executed. For ethical use only run in isolated lab or with explicit permission do not expose publicly.
How to run

pip install -r requirements.txt

Run python honeypot.py in isolated VM (no internet exposure)

Open another terminal: python dashboard.py and visit http://127.0.0.1:8050

Important: Never run this exposed to the public internet. Use only on networks you control.
