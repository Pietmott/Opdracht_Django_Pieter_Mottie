from django.shortcuts import render

def fuel_view(request):
    liters = None
    kost = None

    if request.method == "POST":
        afstand = float(request.POST.get("afstand"))
        verbruik = float(request.POST.get("verbruik"))
        prijs = float(request.POST.get("prijs"))

        liters = (afstand * verbruik) / 100
        kost = liters * prijs

    return render(request, "fuel_form.html", {
        "liters": liters,
        "kost": kost
    })