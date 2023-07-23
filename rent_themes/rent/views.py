from django.shortcuts import render, redirect
from .models import *
from .dao import *

def index(request):
    return redirect('/listClient')

class ClientViews:
    def listClient(request):
        clients_list = ClienteDAO().listaClientes()
        context = {'clients_list': clients_list}
        return render(request, 'client/listClient.html', context)

    def formClient(request):
        return render(request, 'client/formClient.html')

    def saveClient(request):
        if request.method == 'POST':
            perfil = request.FILES.get('perfil')
            name = request.POST['name']
            email = request.POST['email']
            ddd1 = request.POST['ddd1']
            phone1 = request.POST['phone1']
            ddd2 = request.POST['ddd2']
            phone2 = request.POST['phone2']

            ClienteDAO().salvarCliente(perfil, name, email, ddd1, phone1, ddd2, phone2)
            return redirect('/listClient')

    def deleteClient(request, id):
        ClienteDAO().deletarCliente(id=id)
        return redirect('/listClient')

    def detailClient(request, id):
        client = ClienteDAO().detalharCliente(id=id)
        return render(request, 'client/formEditClient.html', {'client': client} )

    def updateClient(request, id):
        if request.method == 'POST':
            perfil = request.FILES.get('perfil')
            name = request.POST['name']
            email = request.POST['email']
            ddd1 = request.POST['ddd1']
            phone1 = request.POST['phone1']
            ddd2 = request.POST['ddd2']
            phone2 = request.POST['phone2']
            ClienteDAO().atualizarCliente(id, perfil, name, email, ddd1, phone1, ddd2, phone2)
            return redirect('/listClient')

class ThemeViews:
    def listTheme(request):
        themes_list = TemaDAO().listaTemas()
        context = {'theme_list': themes_list}
        return render(request, 'theme/listTheme.html', context)

    def formTheme(request):
        list_item = Item.objects.all()
        return render(request, 'theme/formTheme.html', {'list_item':list_item})

    def saveTheme(request):
        TemaDAO().salvaTema(photo = request.FILES.get('photo'), description=request.POST['description'], name=request.POST['name'],color=request.POST['color'], price=request.POST['price'], my_list=request.POST.getlist('item'))
        return redirect('/listTheme')
    
    def deleteTheme(request, id):
        TemaDAO().deletaTema(id)
        return redirect('/listTheme')

    def detailTheme(request, id):
        theme = Theme.objects.get(pk=id)
        return render(request, 'theme/formEditTheme.html', {'theme': theme} )

    def updateTheme(request, id):
        TemaDAO().atualizarTema(id=id, photo = request.FILES.get('photo'), name = request.POST['name'],description=request.POST['description'], color = request.POST['color'], price = request.POST['price'])
        return redirect('/listTheme')

class ItemViews:
    def listItem(request):
        item_list = ItemDAO().listaItem()
        context = {'item_list': item_list}
        return render(request, 'item/listItem.html', context)

    def formItem(request):
        return render(request, 'item/formItem.html')

    def saveItem(request):
        ItemDAO().salvarItem(name=request.POST['name'], description=request.POST['description'])
        return redirect('/listItem')

    def deleteItem(request, id):
        ItemDAO().deletarItem(id)
        return redirect('/listItem')
    
    def detailItem(request, id):
        item = ItemDAO().detalharItem(id)
        return render(request, 'item/formEditItem.html', {'item': item} )

    def updateItem(request, id):
        ItemDAO().atualizarItem(id=id, name=request.POST['name'], description=request.POST['description'])
        return redirect('/listItem')

class RentViews:
    def listRent(request):
        rent_list = AluguelDAO().listaAlugueis()
        context = {'rent_list': rent_list}
        return render(request, 'rent/listRent.html', context)

    def formRent(request):
        client_list = Client.objects.all()
        theme_list = Theme.objects.all()
        context = {'client_list': client_list, 'theme_list': theme_list}
        return render(request, 'rent/formRent.html', context)

    def saveRent(request):
        if request.method == 'POST':
            date = request.POST['date']
            start_hours = request.POST['start_hours']
            end_hours = request.POST['end_hours']
            client_id = request.POST['select_client']
            theme_id = request.POST['select_theme']
            address_data = {
                'street': request.POST['street'],
                'number': int(request.POST['number']),
                'complement': request.POST['complement'],
                'district': request.POST['district'],
                'city': request.POST['city'],
                'state': request.POST['state'],
            }

            AluguelDAO().salvaAluguel(date, start_hours, end_hours, client_id, theme_id, address_data)
            return redirect('/listRent')

    def deleteRent(request, id):
        AluguelDAO().deletaAluguel(id)
        return redirect('/listRent')

    def detailRent(request, id):
        rent = AluguelDAO().detalharAluguel(id)
        return render(request, 'rent/formEditRent.html', {'rent': rent})

    def updateRent(request, id):
        if request.method == 'POST':
            date = request.POST['date']
            start_hours = request.POST['start_hours']
            end_hours = request.POST['end_hours']
            address_data = {
                'street': request.POST['street'],
                'number': int(request.POST['number']),
                'complement': request.POST['complement'],
                'district': request.POST['district'],
                'city': request.POST['city'],
                'state': request.POST['state'],
            }

            AluguelDAO().atualizaAluguel(id, date, start_hours, end_hours, address_data)
            return redirect('/listRent')