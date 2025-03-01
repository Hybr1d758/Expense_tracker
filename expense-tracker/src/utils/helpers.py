def validate_amount(amount):
    if isinstance(amount, (int, float)) and amount >= 0:
        return True
    return False

def format_date(date):
    return date.strftime("%Y-%m-%d")

def parse_date(date_string):
    from datetime import datetime
    return datetime.strptime(date_string, "%Y-%m-%d")