import pandas as pd #type:ignore
import time
import smtplib
from email.message import EmailMessage
from detect_anomalies import detect_anomalies  # Import anomaly detection function

def send_alert(anomalies):
    """Sends an email alert if anomalies are detected"""
    
    sender_email = "your_email@gmail.com"
    receiver_email = "admin@example.com"
    password = "your-email-password"

    message = EmailMessage()
    message["Subject"] = "🚨 API Anomalies Detected!"
    message["From"] = sender_email
    message["To"] = receiver_email
    message.set_content(f"Anomalies Detected:\n\n{anomalies.to_string()}")

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)
    
    print("📩 Alert Sent!")

def monitor_api_logs():
    """Fetches logs every 5 minutes & checks for anomalies"""

    while True:
        # Fetch latest logs (replace with actual DB/API call)
        df_logs = pd.read_csv("data/api_logs.csv")

        anomalies = detect_anomalies(df_logs)
        
        if not anomalies.empty:
            send_alert(anomalies)
        
        print("✅ Monitoring... No anomalies detected")
        
        time.sleep(300)  # Wait 5 minutes before checking again

# Run the monitoring script
if __name__ == "__main__":
    monitor_api_logs()
