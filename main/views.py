from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from datetime import datetime
from .models import *

def home_view(request):
    today = datetime.today()
    context = {
        'today': today,
    }
    return render(request, 'home.html', context)

def talaba_view(request):
    form = TalabaForm
    if request.method == "POST":
        form = TalabaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Talaba.objects.create(
                ism = data.get('ism'),
                kurs = data.get('kurs'),
                guruh = data.get('guruh'),
                kitob_soni = data.get('kitob_soni'),
            )
        return redirect('talabalar')


    talabalar = Talaba.objects.all()
    guruhlar = [item['guruh'] for item in Talaba.objects.all().values('guruh')]
    guruhlar = sorted(list(set(guruhlar)))

    search = request.GET.get('search')
    kurs = request.GET.get('kurs')
    guruh = request.GET.get('guruh')

    if search is not None:
        talabalar = talabalar.filter(ism__icontains = search)
    if kurs is not None and kurs != '0':
        talabalar = talabalar.filter(kurs = kurs)
    if guruh is not None and guruh != '0':
        talabalar = talabalar.filter(guruh = guruh)

    context = {
        'talabalar': talabalar,
        'guruh': guruh,
        'kurs': kurs,
        'search': search,
        'guruhlar': guruhlar,
        'form': form,
    }
    return render(request, 'talabalar.html', context)

def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id = talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_details.html', context)

def talaba_update_view(request, pk):
    talaba = get_object_or_404(Talaba, id = pk)

    if request.method == 'POST':
        talaba.ism = request.POST.get('ism')
        talaba.guruh = request.POST.get('guruh')
        talaba.kurs = request.POST.get('kurs')
        talaba.kitob_soni = request.POST.get('kitob_soni')
        talaba.save()
        return redirect('talabalar')

    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_update.html', context)

def kutubxonachi_update_view(request, pk):
    kutubxonachi = get_object_or_404(Kutubxonachi, id = pk)
    ish_vaqtlari = Kutubxonachi.ISH_VAQTI_CHOICES

    if request.method == 'POST':
        kutubxonachi.ism = request.POST.get('ism')
        kutubxonachi.ish_vaqti = request.POST.get('ish_vaqti')
        kutubxonachi.save()
        return redirect('kutubxonachilar')

    context = {
        'kutubxonachi': kutubxonachi,
        'ish_vaqtlari': ish_vaqtlari,
    }
    return render(request, 'kutubxonachi_update.html', context)

def muallif_view(request):
    form = MuallifForm
    if request.method == "POST":
        form = MuallifForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        Muallif.objects.create(
            ism = data.get('ism'),
            t_sana = data.get('t_sana'),
            kitob_soni = data.get('kitob_soni'),
            jins = data.get('jins'),
            tirik = data.get('tirik'),
        )
        return redirect('mualliflar')

    muallif = Muallif.objects.all()
    tiriklar = [item['tirik'] for item in Muallif.objects.all().values('tirik')]
    tiriklar = sorted(list(set(tiriklar)))
    jinslar = [item['jins'] for item in Muallif.objects.all().values('jins')]
    jinslar = sorted(list(set(jinslar)))

    search = request.GET.get('search')
    tirik = request.GET.get('tirik')
    jins = request.GET.get('jins')

    if search is not None:
        muallif = muallif.filter(ism__icontains = search)
    if tirik is not None and tirik != '0':
        muallif = muallif.filter(tirik = tirik)
    if jins is not None and jins != '0':
        muallif = muallif.filter(jins = jins)

    context = {
        'muallif': muallif,
        'search': search,
        'tirik': tirik,
        'jins': jins,
        'jinslar': jinslar,
        'tiriklar': tiriklar,
        'form': form
    }
    return render(request, 'muallif.html', context)

def muallif_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id = muallif_id)
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_details.html', context)

def muallif_update_view(request, pk):
    muallif = get_object_or_404(Muallif, id = pk)

    if request.method == 'POST':
        muallif.ism = request.POST.get('ism')
        muallif.jins = request.POST.get('jins')
        muallif.t_sana = request.POST.get('t_sana')
        muallif.kitob_soni = request.POST.get('kitob_soni')
        if request.POST.get('tirik'):
            muallif.tirik = True
        else:
            muallif.tirik = False

        muallif.save()
        return redirect('mualliflar')

    context = {
        'muallif': muallif
    }
    return render(request, 'muallif_update.html', context)

def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    mualliflar = [Muallif.objects.get(id=id) for id in set(Kitob.objects.all().values_list('muallif', flat = True))]

    muallif = request.GET.get('muallif')

    if muallif is not None and muallif != '0':
        kitoblar = kitoblar.filter(muallif__id=muallif)

    context = {
        'kitoblar': kitoblar,
        'mualliflar': mualliflar
    }
    return render(request, 'kitoblar.html', context)

def kitob_qoshish_view(request):
    form = KitobModelForm
    if request.method == 'POST':
        form = KitobModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('kitoblar')
    context = {
        'form': form
    }
    return render(request, 'kitob-qoshish.html', context)

def kitoblar_details_view(request, kitob_id):
    kitoblar = Kitob.objects.get(id = kitob_id)
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'kitoblar_details.html', context)

from datetime import datetime

def recordlar_view(request):
    form = RecordModelForm
    if request.method == 'POST':
        form = RecordModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recordlar')





    #     olingan_sana_str = request.POST.get('olingan_sana')
    #     qaytargan_sana_str = request.POST.get('qaytargan_sana')
    #
    #     if olingan_sana_str:
    #         olingan_sana = datetime.strptime(olingan_sana_str, '%Y-%m-%dT%H:%M')
    #     else:
    #         olingan_sana = None
    #
    #     if qaytargan_sana_str:
    #         qaytargan_sana = datetime.strptime(qaytargan_sana_str, '%Y-%m-%dT%H:%M')
    #     else:
    #         qaytargan_sana = None
    #
    #     if qaytardi is None or qaytardi == "":
    #         qaytardi = False
    #
    #     return redirect('recordlar')
    #
    recordlar = Record.objects.all()
    kitoblar = Kitob.objects.filter(id__in=recordlar.values_list('kitob', flat=True)).distinct()
    talabalar = Talaba.objects.filter(id__in=recordlar.values_list('talaba', flat=True)).distinct()
    kutubxonachilar = Kutubxonachi.objects.filter(id__in=recordlar.values_list('kutubxonachi', flat=True)).distinct()

    kitob = request.GET.get('kitob')
    talaba = request.GET.get('talaba')
    kutubxonachi = request.GET.get('kutubxonachi')

    if kitob is not None and kitob != '0':
        recordlar = recordlar.filter(kitob=kitob)
    if talaba is not None and talaba != '0':
        recordlar = recordlar.filter(talaba=talaba)
    if kutubxonachi is not None and kutubxonachi != '0':
        recordlar = recordlar.filter(kutubxonachi=kutubxonachi)

    context = {
        'recordlar': recordlar,
        'kitoblar':kitoblar,
        'kitob':kitob,
        'talabalar':talabalar,
        'talaba':talaba,
        'kutubxonachi': kutubxonachi,
        'kutubxonachilar': kutubxonachilar,
        'form': form
    }
    return render(request, 'recordlar.html', context)

def recordlar_details_view(request, record_id):
    recordlar = Record.objects.get(id = record_id)
    context = {
        'recordlar': recordlar,
    }
    return render(request, 'recordlar_details.html', context)

def kutubxonachilar_view(request):
    kutubxonachilar = Kutubxonachi.objects.all()
    form = KutubxonachiForm
    if request.method == 'POST':
        form = KutubxonachiForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Kutubxonachi.objects.create(
                ism=data.get('ism'),
                ish_vaqti=data.get('ish_vaqti'),
            )
    context = {
        'kutubxonachilar': kutubxonachilar,
        'form': form,
    }
    return render(request, 'kutubxonachilar.html', context)



def kutubxonachilar_details_view(request, kutubxonachi_id):
    kutubxonachilar = Kutubxonachi.objects.get(id = kutubxonachi_id)
    context = {
        'kutubxonachilar': kutubxonachilar,
    }
    return render(request, 'kutubxonachilar_details.html', context)

def bitiruvchilar_view(request):
    bitiruvchilar = Talaba.objects.filter(kurs = 1)
    context = {
        'bitiruvchilar': bitiruvchilar
    }
    return render(request, 'bitiruvchilar.html', context)

def kitoblilar_view(request):
    kitoblilar = Talaba.objects.filter(kitob_soni__gt=0)
    context = {
        'kitoblilar': kitoblilar
    }
    return render(request, 'kitoblilar.html', context)

def a_lilar_view(request):
    a_lilar = Talaba.objects.filter(ism__icontains = 'a')
    context = {
        'a_lilar': a_lilar
    }
    return render(request, 'a_lilar.html', context)

def erkak_mualliflar_view(request):
    erkak_mualliflar = Muallif.objects.filter(jins = 'erkak')
    context = {
        'erkak_mualliflar': erkak_mualliflar
    }
    return render(request, 'erkak_mualliflar.html', context)

def tanlangan_id_view(request):
    tanlangan_id = Talaba.objects.all()
    context = {
        'tanlangan_id': tanlangan_id
    }
    return render(request, 'tanlangan_id.html', context)

def muallif_mal_view(request):
    muallif_mal = Muallif.objects.all()
    context = {
        'muallif_mal': muallif_mal
    }
    return render(request, 'muallif_mal.html', context)

def tanlangan_kitob_view(request):
    tanlangan_kitob = Kitob.objects.all()
    context = {
        'tanlangan_kitob': tanlangan_kitob
    }
    return render(request, 'tanlangan_kitob.html', context)

def tirik_m_view(request):
    tirik_m = Muallif.objects.filter(tirik = True)
    context = {
        'tirik_m': tirik_m
    }
    return render(request, 'tirik_m.html', context)

def max_sahifa_view(request):
    max_sahifa = Kitob.objects.order_by('-sahifa')[:3]
    context = {
        'max_sahifa': max_sahifa
    }
    return render(request, 'max_sahifa.html', context)

def max_kitobli_view(request):
    max_kitobli = Muallif.objects.order_by('-kitob_soni')[:3]
    context = {
        'max_kitobli': max_kitobli
    }
    return render(request, 'max_kitobli.html', context)

def record_sana_view(request):
    record_sana = Record.objects.order_by('-olingan_sana')[:3]
    context = {
        'record_sana': record_sana
    }
    return render(request, 'record_sana.html', context)

def tirik_kitob_view(request):
    tirik_kitob = Kitob.objects.filter(muallif__tirik = True)
    context = {
        'tirik_kitob': tirik_kitob
    }
    return render(request, 'tirik_kitob.html', context)

def fantastik_view(request):
    fantastik = Kitob.objects.filter(janr = 'Fantastika')
    context = {
        'fantastik': fantastik
    }
    return render(request, 'fantastik.html', context)

def katta_yosh_view(request):
    katta_yosh = Muallif.objects.order_by('t_sana')[:3]
    context = {
        'katta_yosh': katta_yosh
    }
    return render(request, 'katta_yosh.html', context)

def ten_view(request):
    ten = Kitob.objects.filter(muallif__kitob_soni__lte=10)
    context = {
        'ten': ten
    }
    return render(request, 'ten.html', context)

def tan_rec_view(request):
    tan_rec = Record.objects.all()
    context = {
        'tan_rec': tan_rec
    }
    return render(request, 'tan_rec.html', context)

def bitiruvchi_rec_view(request):
    bitiruvchi_rec = Record.objects.filter(talaba__kurs = 4)
    context = {
        'bitiruvchi_rec': bitiruvchi_rec
    }
    return render(request, 'bitiruvchi_rec.html', context)

def talaba_delete_view(request, pk):
    talaba = Talaba.objects.get(id = pk)
    talaba.delete()
    return redirect('talabalar')

def muallif_dc_view(request, pk):
    muallif = Muallif.objects.get(id = pk)
    context = {
        'muallif': muallif
    }
    return render(request, 'muallif_dc.html', context)

def muallif_delete_view(reuqest, pk):
    muallif = Muallif.objects.get(id = pk)
    muallif.delete()
    return redirect('mualliflar')

def kitob_dc_view(request, pk):
    kitob = Kitob.objects.get(id = pk)
    context = {
        'kitob': kitob
    }
    return render(request, 'kitob_dc.html', context)

def kitob_d_view(request, pk):
    kitob = Kitob.objects.get(id = pk)
    kitob.delete()
    return redirect('kitoblar')

def record_dc_view(request, pk):
    record = Record.objects.get(id = pk)
    context = {
        'record': record
    }
    return render(request, 'record_dc.html', context)

def record_d_view(request, pk):
    record = Record.objects.get(id = pk)
    record.delete()
    return redirect('recordlar')

def kitob_update_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)

    if request.method == 'POST':
        muallif = get_object_or_404(Muallif, id=request.POST.get('muallif_id'))
        kitob.nom = request.POST.get('nom')
        kitob.janr = request.POST.get('janr')
        kitob.sahifa = request.POST.get('sahifa')
        kitob.muallif = muallif
        kitob.save()
        return redirect('kitoblar')

    mualliflar = set(Muallif.objects.all().order_by('ism'))
    context = {
        'kitob': kitob,
        'mualliflar': mualliflar,
    }
    return render(request, 'kitob_update.html', context)



def record_update_view(request, pk):
    record = get_object_or_404(Record, id=pk)

    if request.method == 'POST':
        qaytardi = request.POST.get('qaytardi')
        if qaytardi == 'on':
            qaytardi = True
        else:
            qaytardi = False

        Record.objects.filter(id=pk).update(
        talaba = get_object_or_404(Talaba, id=request.POST.get('talaba_id')),
        kitob = get_object_or_404(Kitob, id=request.POST.get('kitob_id')),
        kutubxonachi = get_object_or_404(Kutubxonachi, id=request.POST.get('kutubxonachi_id')),
        olingan_sana = request.POST.get('olingan_sana'),
        qaytardi = qaytardi,
        )
        return redirect('recordlar')

    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = Kutubxonachi.objects.all()

    context = {
        'record': record,
        'talabalar': talabalar,
        'kitoblar': kitoblar,
        'kutubxonachilar': kutubxonachilar,
    }
    return render(request, 'record_update.html', context)
















