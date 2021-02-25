from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

now = timezone.now()


def home(request):
    return render(request, 'inventorysystem/home.html',
                  {'inventorysystem': home})


@login_required
def inventory_list(request):
    inventory = Inventory.objects.filter(created_date__lte=timezone.now())
    return render(request, 'inventorysystem/inventory_list.html',
                  {'inventorys': inventory})


@login_required
def store_list(request):
    store = Store.objects.filter(created_date__lte=timezone.now())
    return render(request, 'inventorysystem/store_list.html',
                  {'stores': store})


@login_required
def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        # update
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.updated_date = timezone.now()
            inventory.save()
            inventory = Inventory.objects.filter(created_date__lte=timezone.now())
            return render(request, 'inventorysystem/inventory_list.html',
                          {'inventorys': inventory})
    else:
        # edit
        form = InventoryForm(instance=inventory)
    return render(request, 'inventorysystem/inventory_edit.html', {'form': form})


@login_required
def store_edit(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        # update
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.updated_date = timezone.now()
            store.save()
            store = Store.objects.filter(created_date__lte=timezone.now())
            return render(request, 'inventorysystem/store_list.html',
                          {'stores': store})
    else:
        # edit
        form = StoreForm(instance=store)
    return render(request, 'inventorysystem/store_edit.html', {'form': form})


@login_required
def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    store.delete()
    return redirect('inventorysystem:store_list')


@login_required
def inventory_delete(request, pk):
    inventory = get_object_or_404(Store, pk=pk)
    inventory.delete()
    return redirect('inventorysystem:inventory_list')


@login_required
def summary(request, pk):
    store = get_object_or_404(Store, pk=pk)
    stores = Store.objects.filter(created_date__lte=timezone.now())
    inventorys = Inventory.objects.filter(store=pk)
    return render(request, 'inventorysystem/summary.html', {'stores': stores,
                                                            'inventorys': inventorys, })


@login_required
def inventory_new(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.created_date = timezone.now()
            inventory.save()
            inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
            return render(request, 'inventorysystem/inventory_list.html',
                          {'inventorys': inventorys})
    else:
        form = InventoryForm()
        # print("Else")
    return render(request, 'inventorysystem/inventory_new.html', {'form': form})


@login_required
def store_new(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.created_date = timezone.now()
            store.save()
            stores = Store.objects.filter(created_date__lte=timezone.now())
            return render(request, 'inventorysystem/store_list.html',
                          {'stores': stores})
    else:
        form = StoreForm()
        # print("Else")
    return render(request, 'inventorysystem/store_new.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'inventorysystem/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'inventorysystem/register.html',
                  {'user_form': user_form})
