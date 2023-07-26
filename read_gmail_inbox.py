import imaplib
import email

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(decode=True).decode()

def get_latest_inbox_message():
    gmail_username = "something@gmail.com"
    gmail_password = "app_passowrd"

    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        # Login to the Gmail account
        mail.login(gmail_username, gmail_password)

        # Select the 'inbox' mailbox
        mail.select('inbox')

        # Search for all emails in the 'inbox'
        status, messages = mail.search(None, 'ALL')

        # Get the latest message ID (the last one in the list)
        latest_message_id = messages[0].split()[-1]

        # Fetch the latest message
        status, msg_data = mail.fetch(latest_message_id, '(RFC822)')

        # Parse the email message using the email library
        msg = email.message_from_bytes(msg_data[0][1])

        # Extract message details
        from_email = msg["From"]
        subject = msg["Subject"]
        body = get_body(msg)

        # Output message details, fetch relevant info
        print("From:", from_email)
        print("Subject:", subject)
        print("Body:")
        Body = body.split()
        for token in Body:
            if token.startswith("eyJ"):
                print(token)

    finally:
        # Logout and close the connection
        mail.logout()

if __name__ == "__main__":
    get_latest_inbox_message()

