from django.shortcuts import render,redirect
from .models import Player
from .forms import player_form
from django.contrib import messages

# Create your views here.


def home(request):
    players = Player.objects.all()
    form = player_form()
    return render(request, "Home.html", {'players': players, 'form': form})

    # Add_Player
def add_player_function(request):
    form = player_form(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Player successfully added !')
        return redirect('home')
    else:
        messages.add_message(request, messages.ERROR, 'an error occurred when walking the player')
        return redirect('home')


    # Delete_Player
def delete_player_function(request, player_id):
    player=Player.objects.get(id=player_id)
    messages.add_message(request, messages.SUCCESS, 'Player successfully eliminated !' + player.name)
    player.delete()
    return redirect('home')

    # Update_Player
def update_player_function(request, player_id):
    player=Player.objects.get(id = player_id)
    form = player_form(request.POST, instance=player)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Successfully modified player !')
        return redirect('home')
    messages.add_message(request, messages.ERROR, 'an error occurred when modifying the player')
    return redirect('home')
