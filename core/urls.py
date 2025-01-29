from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('talabalar/', talaba_view, name = 'talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('mualliflar/', muallif_view, name = 'mualliflar'),
    path('mualliflar/<int:muallif_id>/', muallif_details_view),
    path('kitoblar/', kitoblar_view, name = 'kitoblar'),
    path('kitoblar/<int:record_id>/', recordlar_details_view),
    path('recordlar/', recordlar_view, name = 'recordlar'),
    path('recordlar/<int:record_id>/', recordlar_details_view),
    path('kutubxonachilar/', kutubxonachilar_view, name = 'kutubxonachilar'),
    path('kutubxonachilar/<int:kutubxonachi_id>/',kutubxonachilar_details_view),
    path('bitiruvchilar/', bitiruvchilar_view),
    path('kitoblilar/', kitoblilar_view),
    path('a_lilar/', a_lilar_view),
    path('tanlangan_id/', tanlangan_id_view),
    path('erkak_mualliflar/', erkak_mualliflar_view),
    path('muallif_mal/', muallif_mal_view),
    path('tanlangan_kitob/', tanlangan_kitob_view),
    path('tirik_m/', tirik_m_view),
    path('max_sahifa/', max_sahifa_view),
    path('max_kitobli/', max_kitobli_view),
    path('record_sana/', record_sana_view),
    path('tirik_kitob/', tirik_kitob_view),
    path('fantastik/', fantastik_view),
    path('katta_yosh/', katta_yosh_view),
    path('ten/', ten_view),
    path('tan_rec/', tan_rec_view),
    path('bitiruvchi_rec/', bitiruvchi_rec_view),
    path('talabalar/<int:pk>/delete/', talaba_delete_view),
    path('talabalar/<int:pk>/update/', talaba_update_view),
    path('mualliflar/<int:pk>/update/', muallif_update_view),
    path('muallif/<int:pk>/delete_confirm/', muallif_dc_view),
    path('muallif/<int:pk>/delete/', muallif_delete_view),
    path('kitob/<int:pk>/delete_confirm/', kitob_dc_view),
    path('kitob/<int:pk>/delete/', kitob_d_view),
    path('record/<int:pk>/delete_confirm/', record_dc_view),
    path('record/<int:pk>/delete/', record_d_view),
    path('kitob-qoshish/', kitob_qoshish_view),
    path('kitoblar/<int:pk>/update/', kitob_update_view),
    path('kutubxonachilar/<int:pk>/update/', kutubxonachi_update_view),
    path('record/<int:pk>/update/', record_update_view),
]









