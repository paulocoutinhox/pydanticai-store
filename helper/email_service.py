from typing import Any, Dict


class EmailService:
    @staticmethod
    def send_purchase_confirmation(order: Dict[str, Any]) -> bool:
        """
        Simulates sending a purchase confirmation email.

        TODO: To implement real email sending, you can:
        1. Configure an SMTP server (Gmail, Outlook, etc.)
        2. Use libraries like smtplib + email.mime
        3. Or use services like SendGrid, Mailgun, etc.
        4. Create HTML templates for prettier emails

        Example implementation with Gmail:
        ```
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        def send_real_email(to_email, subject, body):
            msg = MIMEMultipart()
            msg['From'] = 'your-email@gmail.com'
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('your-email@gmail.com', 'your-app-password')
            server.send_message(msg)
            server.quit()
        ```
        """
        try:
            # Simulation of sending - just displays in console
            print(f"📧 Email sent to {order['customer_email']}")
            print(f"   Subject: Purchase Confirmation - {order['book_title']}")
            print(f"   Order: {order['id']}")
            print(f"   Amount: $ {order['price']:.2f}")
            print(f"   Status: ✅ Email simulated successfully!")

            # TODO: Implement real sending here
            # send_real_email(
            #     to_email=order['customer_email'],
            #     subject=f"Purchase Confirmation - {order['book_title']}",
            #     body=f"Your order {order['id']} has been confirmed..."
            # )

            return True
        except Exception as e:
            print(f"❌ Error sending email: {e}")
            return False
