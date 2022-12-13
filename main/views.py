from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from itertools import chain
from .models import Quarterback, Runningback, Widereceiver, Tightend, Tackle, IOL, IDL, Cornerback, Linebacker, Edge, Safety, Prospect

def home(request):
    players = Prospect.objects.order_by('grade').reverse()
    # report = chain(Quarterback.objects.all() , Runningback.objects.all(), Widereceiver.objects.all())
    return render(request, 'main/home.html', {'players':players})

def descriptions(request):
    return render(request, 'main/descriptions.html')

def teamneeds(request, team):
    if team == "ravens":
        return render(request, 'main/ravens.html')
    elif team == "steelers":
        return render(request, 'main/steelers.html')
    elif team == "bengals":
        return render(request, 'main/bengals.html')
    elif team == "colts":
        return render(request, 'main/colts.html')
    elif team == "cowboys":
        return render(request, 'main/cowboys.html')
    elif team == "giants":
        return render(request, 'main/giants.html')
    elif team == "commanders":
        return render(request, 'main/commanders.html')
    elif team == "jaguars":
        return render(request, 'main/jaguars.html')
    elif team == "jets":
        return render(request, 'main/jets.html')

def position(request, pos):
    if pos == "QB":
        players = Quarterback.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "RB":
        players =Runningback.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "WR":
        players = Widereceiver.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "TE":
        players = Tightend.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "IOL":
        players = IOL.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "OT":
        players = Tackle.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "IDL":
        players = IDL.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "Edge":
        players = Edge.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "LB":
        players = Linebacker.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "CB":
        players = Cornerback.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})
    if pos == "S":
        players = Safety.objects.order_by('grade').reverse()
        return render(request, 'main/position.html', {'players':players, 'pos':pos})


def player(request, position, name, school, player_id):
    prospect = get_object_or_404(Prospect, pk=player_id)

    if position == "CB":
        traits = ["Size", "Speed", "Change of Direction", "Man Coverage", "Zone Coverage",
        "Press", "Ball Skills", "Transitions", "Run Defense", "Tackling", "Grade"]
        cbs = Cornerback.objects.all()
        for cb in cbs:
            if cb.prospect == prospect:
                player = cb
                field_names = Cornerback._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i],getattr(player, field.name)])
                    i += 1
                break

    elif position == "QB":
        traits = ["Arm Strength", "Size", "Short Accuracy", "Deep Accuracy", "Mobility",
        "Processor", "Decision Making", "Athleticism", "Mechanics", "Timing/Anticipation", "Ball Carrier",
        "Intangebles", "Grade",]
        qbs = Quarterback.objects.all()
        for qb in qbs:
            if qb.prospect == prospect:
                player = qb
                field_names = Quarterback._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "RB":
        traits = ["Size", "Vision", "Balance", "Elusiveness", "Speed", "Burst", 
        "Pass Blocking", "Fumble", "Change of Direction", "Grade"]
        rbs = Runningback.objects.all()
        for rb in rbs:
            if rb.prospect == prospect:
                player = rb
                field_names = Runningback._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "WR":
        traits = ["Size", "Speed", "Change of Direction", "Release", "Short Route Running", "Deep Route Running",
        "Hands", "Ball Skills", "Run After Catch", "Blocking", "Catch in Traffic", "Grade"]
        wr = Widereceiver.objects.all()
        for w in wr:
            if w.prospect == prospect:
                player = w
                field_names = Widereceiver._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "TE":
        traits = ["Size", "Speed", "Change of Direction", "Release", "Short Route Running", "Deep Route Running",
        "Hands", "Ball Skills", "Run After Catch", "Run Blocking", "Pass Blocking", "Catch in Traffic", "Grade"]
        te = Tightend.objects.all()
        for t in te:
            if t.prospect == prospect:
                player = t
                field_names = Tightend._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "IOL":
        traits = ["Size", "Pass Set", "Run Blocking", "Impact Blocking", "Move Blocking", "Strength", 
        "Athleticism", "Hands/Leverage", "Anchor", "Lean/Weight Distribution", "Grade"]
        iol = IOL.objects.all()
        for o in iol:
            if o.prospect == prospect:
                player = o
                field_names = IOL._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "OT":
        traits = ["Size", "Pass Set", "Run Blocking", "Impact Blocking", "Move Blocking", "Strength", 
        "Athleticism", "Hands/Leverage", "Anchor", "Kick Slide", "Lean/Weight Distribution", "Grade"]
        ot = Tackle.objects.all()
        for t in ot:
            if t.prospect == prospect:
                player = t
                field_names = Tackle._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "IDL":
        traits = ["Size", "Point of Attack", "Block Shed", "Strength", "Power Rush", "Finesse Rush", 
        "Getoff", "Bend", "Athleticism", "Hands/Leverage", "Motor", "Grade"]
        idl = IDL.objects.all()
        for d in idl:
            if d.prospect == prospect:
                player = d
                field_names = IDL._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "Edge":
        traits = ["Size", "Point of Attack", "Block Shed", "Speed Rush", "Power Rush", "Finesse Rush", 
        "Getoff", "Bend", "Athleticism", "Hands/Leverage", "Tackling", "Motor", "Strength", "Grade"]
        edge = Edge.objects.all()
        for e in edge:
            if e.prospect == prospect:
                player = e
                field_names = Edge._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i  += 1
                break

    elif position == "LB":
        traits = ["Size", "Speed", "Change of Direction", "Man Coverage", "Zone Coverage", 
        "Point of Attack", "Block Shed", "Strength", "Processor", "Tackling", "Blizing", "Grade"]
        lb = Linebacker.objects.all()
        for l in lb:
            if l.prospect == prospect:
                player = l
                field_names = Linebacker._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break

    elif position == "S":
        traits = ["Size", "Speed", "Change of Direction", "Man Coverage", "Zone Coverage",
        "Press", "Ball Skills", "Transitions", "Run Defense", "Tackling", "Range", "Grade"]
        s = Safety.objects.all()
        for saf in s:
            if saf.prospect == prospect:
                player = saf
                field_names = Safety._meta.get_fields()
                player_fields = []
                i = -4
                for field in field_names:
                    player_fields.append([traits[i] ,getattr(player, field.name)])
                    i += 1
                break


    return render(request, 'main/player.html', {'player':player, 'field_names':traits, 
    'player_fields': player_fields[4:]})