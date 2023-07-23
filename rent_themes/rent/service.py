from decimal import Decimal
from datetime import datetime
from .models import Rent, Theme

class CalculaAluguel:
    def calcDesconto(self, client_id, theme_id, date):
        price_theme = Theme.objects.get(pk=theme_id).price
        date = datetime.strptime(date, "%Y-%m-%d")

        if date.weekday() >= 0 and date.weekday() <= 3:
            return price_theme - (price_theme * Decimal('0.40'))
        elif Rent.objects.filter(client_id=client_id).exists():
            return price_theme - (price_theme * Decimal('0.10')) 
        else:
            return price_theme
