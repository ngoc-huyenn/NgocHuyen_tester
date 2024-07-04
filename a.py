import re
from imap_tools import MailBox, AND

email_name='ngochuyenxu2905@gmail.com'
email_password='acdeydciopkdrqnw'

def get_code(email_name,email_password):
  verification_code = ""
  def extract_verification_code(text):
    match = re.search(r'\b\d{6}\b', text)
    return match.group() if match else None
  with MailBox("imap.gmail.com").login(email_name, email_password, "INBOX") as mailbox:
    # Search for emails from Facebook
    emails = mailbox.fetch(criteria=AND(from_="security@facebookmail.com"), limit=1, reverse=True, mark_seen=False)
    
    for msg in emails:
        
        # Extract the verification code from the email body
        verification_code = extract_verification_code(msg.subject)
        if verification_code:
            print(f"Verification code: {verification_code}")
            return verification_code
        else:
            print("Not found.")
  return verification_code

get_code(email_name,email_password)