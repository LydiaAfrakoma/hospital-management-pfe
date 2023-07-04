from django.core.mail import send_mail

send_mail(
    'Test Email',
    'This is a test email.',
    'from@gmail.com',  # Sender's email address
    ['afrakomalydia08@gmail.com'],  # Recipient's email address
    fail_silently=False,
)
