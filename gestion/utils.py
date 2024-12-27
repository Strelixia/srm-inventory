from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_invoice_email(order, buyer_email, supplier_email):
    email_html_content =  render_to_string('invoice_email.html', {
        'order': order,
        'seller_email': 'maguy.birikomo@gmail.com'
    })
    email = EmailMessage(
        subject = f"Facture pour votre commande",
        body = email_html_content,
        from_email = 'maguy.birikomo@gmail.com',
        to =  [buyer_email, supplier_email],
    )
    email.content_subtype = "html"
    email.send()


def send_delivery_email (order, buyer_email, supplier_email):
    email_html_content = render_to_string('delivery_email.html', {
        'order': order,
        'seller_email': 'maguy.birikomo@gmail.com'
    })
    email = EmailMessage(
        subject = f"Livraison des marchandises",
        body = email_html_content,
        from_email = 'maguy.birikomo@gmail.com',
        to =  [buyer_email, supplier_email],
    )
    email.content_subtype = "html"
    email.send()


