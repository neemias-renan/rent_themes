from .models import *
from .service import CalculaAluguel

class ClienteDAO:
    def listaClientes(self):
        return Client.objects.all()

    def salvarCliente(self, perfil, name, email,ddd1,number1, ddd2, number2):
        c = Client(perfil=perfil,name=name,email=email)
        c.save()

        if ddd1 != "" and number1 != "":
            t1 = Phone(ddd=ddd1, number=number1, client=c)
            t1.save()

        if ddd2 != "" and number2 != "":
            t2 = Phone(ddd=ddd2, number=number2, client=c)
            t2.save()

    def deletarCliente(self, id):
        c = Client.objects.get(pk=id)
        c.delete()
    
    def detalharCliente(self, id):
        return Client.objects.get(pk=id)
    
    def atualizarCliente(self, id, perfil, name, email, ddd1,number1, ddd2, number2):
        c = Client.objects.get(pk=id)
        c.name = name
        c.email = email
        if perfil != None:
            c.perfil = perfil
        c.save()
        phones = Phone.objects.filter(client=c)

        if ddd1 != "" and number1 != "":
            if(phones.first()):
                t1 = phones.first()
                t1.ddd = ddd1
                t1.number = number1
                t1.save()
            else: 
                t1 = Phone(ddd=ddd1, number=number1, client=c)
                t1.save()
                      
        if ddd2 != "" and number2 != "":
            if(phones.last() and phones.count()>1):
                t2 = phones.last()
                t2.ddd = ddd2
                t2.number = number2
                t2.save()
            else: 
                t2 = Phone(ddd=ddd2, number=number2, client=c)
                t2.save()    

class AluguelDAO:    
    def listaAlugueis(self):
        return Rent.objects.all()
    
    def salvaAluguel(self, date, start_hours, end_hours, client_id, theme_id, address_data):
        address = Address.objects.create(**address_data)
        total_price = CalculaAluguel().calcDesconto(client_id, theme_id, date)
        Rent.objects.create(date=date, start_hours=start_hours, end_hours=end_hours,client_id=client_id, theme_id=theme_id, address=address,total_price=total_price)
    
    def deletaAluguel(self, id):
        rent = Rent.objects.get(pk=id)
        rent.delete()

    def detalharAluguel(self, id):
        return Rent.objects.get(pk=id)
    
    def atualizaAluguel(self, id, date, start_hours, end_hours, address_data):
        rent = self.detalharAluguel(id)
        rent.date = date
        rent.start_hours = start_hours
        rent.end_hours = end_hours

        addr = rent.address
        if not addr:
            addr = Address.objects.create(**address_data)
        else:
            for key, value in address_data.items():
                setattr(addr, key, value)
            addr.save()

        rent.address = addr
        rent.save()
        return rent

class TemaDAO:
    def listaTemas(self):
        return Theme.objects.all()
    
    def salvaTema(self ,photo,description, name, color, price, my_list):
        t = Theme(photo=photo,name=name,color=color, price=price, description=description)
        t.save()

        my_list = my_list

        for i in my_list:
            item = Item.objects.get(id=i)
            t.itens.add(item)
        t.save()

    def deletaTema(self, id):
        t = self.detalharTema(id)
        t.delete()
    
    def detalharTema(self, id):
        return Theme.objects.get(pk=id)

    def atualizarTema(self,photo, description, id, name, color, price):
        t = self.detalharTema(id)
        t.name = name
        t.color = color
        t.price = price
        if photo != None:
            t.photo = photo
        t.description = description
        t.save()

class ItemDAO:
    def listaItem(self):
        return Item.objects.all()
    
    def salvarItem(self, name, description):
        i = Item(name = name, description=description)
        i.save()

    def deletarItem(self, id):
        t = self.detalharItem(id)
        t.delete()
    
    def detalharItem(self, id):
        return Item.objects.get(pk=id)

    def atualizarItem(self,id, name, description):
        i = self.detalharItem(id)
        i.name = name
        i.description = description
        i.save()