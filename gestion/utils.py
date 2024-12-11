from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_invoice_email(order, buyer_email):
    email_html_content =  render_to_string('invoice_mail.html', {
        'buyer_name': order.buyer.username,
        'order_id': order.id,
        
        'order_date': order.order_date,
        'seller_email': 'maguy.birikomo@gmail.com'
    })

    email = EmailMessage(
        subject = f"Facture pour votre commande",
        body = email_html_content,
        from_email = 'maguy.birikomo@gmail.com',
        to =  ['murairicedric@gmail.com'],
    )
    email.content_subtype = "html"
    email.send()
