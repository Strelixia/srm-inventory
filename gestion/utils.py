from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_invoice_email(order, buyer_email):
    email_html_content =  render_to_string('invoice_mail.html', {
        'order': order,
        'seller_email': 'maguy.birikomo@gmail.com'
    })

    email = EmailMessage(
        subject = f"Facture pour votre commande",
        body = email_html_content,
        from_email = 'maguy.birikomo@gmail.com',
        to =  [buyer_email],
    )
    email.content_subtype = "html"
    email.send()
