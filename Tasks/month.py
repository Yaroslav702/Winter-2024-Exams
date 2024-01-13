# Get month number

MONTHS = [
  'jan',
  'feb',
  'mar',
  'apr',
  'may',
  'jun',
  'jul',
  'aug',
  'sep',
  'oct',
  'nov',
  'dec'
]

def get_month_number(month_name: str) -> int:
    month_prefix = month_name.lower()[:3]

    return MONTHS.index(month_prefix) + 1 if month_prefix in MONTHS else -1