import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your email credentials
sender_email = "twinkle127k@gmail.com"
receiver_email = "anant1042005@gmail.com"
password = ""

# Create a message object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email Subject"

# Add the email body
body = "This is a test email sent from Python."
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server (Gmail in this example)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Start TLS for security
    server.starttls()

    # Login to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")
