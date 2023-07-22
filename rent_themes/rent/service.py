from .dao import *
from datetime import datetime
from .models import Rent, Theme

class CalculaAluguel:
    def calcDesconto(self,client_id, theme_id, date):
        price_theme = TemaDAO().detalharTema(theme_id).price
        date = datetime.strptime(date, "%Y-%m-%d")

        if date.weekday() >= 0 and date.weekday() <= 3:
            return (price_theme - (price_theme*0.40))
        elif Rent.objects.filter(client_id=client_id):
            return (price_theme - (price_theme*0.10))
        else:
            return price_theme


