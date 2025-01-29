from django.contrib import admin
from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'guruh', 'kurs', 'kitob_soni')
    list_display_links = ('id', 'ism')
    list_filter = ('guruh', 'kurs')
    list_per_page = 50
    list_editable = ('kitob_soni',)
    search_fields = ('ism', 'guruh')
    search_help_text = "Ism va guruh bo'yicha qidiring!"


# class TalabaInline(admin.StackedInline):
#     model = Record
#     fk_name = Talaba
#     extra = 1
#
#
# class KitobInline(admin.StackedInline):
#     model = Record
#     fk_name = Kitob
#     extra = 1
#
#
# class KutubxonachiInline(admin.StackedInline):
#     model = Record
#     fk_name = Kutubxonachi
#     extra = 1


class RecordAdmin(admin.ModelAdmin):
    search_fields = ('talaba.ism', 'kitob.nom', 'kutubxonachi.ism')
    search_help_text = "Talaba va kitob bo'yicha qidiring!"
    date_hierarchy = 'olingan_sana'
    # inlines = [TalabaInline, KitobInline, KutubxonachiInline,]


class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'ish_vaqti')
    search_fields = ('ism',)
    search_help_text = "Ism bo'yicha qidiring!"
    list_filter = ('ish_vaqti',)


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 't_sana', 'jins', 'kitob_soni', 'tirik')
    list_display_links = ('id', 'ism')
    search_fields = ('ism',)
    list_filter = ('tirik',)
    list_editable = ('kitob_soni', 'tirik')


admin.site.register(Kitob)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Record, RecordAdmin)
