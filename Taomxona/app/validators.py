from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('Telefon raqami faqat raqamlar bo‘lishi kerak.')
    if len(value) != 10:
        raise ValidationError('Telefon raqami 10 ta raqamdan iborat bo‘lishi kerak.')