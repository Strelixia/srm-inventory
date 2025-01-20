from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_email(order, subject, template_name):
    buyer_email = order.buyer.email
    supplier_email = order.product.supplier.email
                         
    email_html_content = render_to_string(template_name, {
        'order': order,
        'seller_email': buyer_email
    })
    email = EmailMessage(
        subject = subject,
        body = email_html_content,
        from_email = buyer_email,
        to =  [buyer_email, supplier_email],
    )
    email.content_subtype = "html"
    email.send()