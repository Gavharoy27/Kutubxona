from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    guruh = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.PositiveSmallIntegerField(default=0)


    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return self.ism


class Kutubxonachi(models.Model):
    ISH_VAQTI_CHOICES = (
        ('08:00-13_00', '08:00-13_00'),
        ('13:00-18:00', '13:00-18:00'),
        ('18:00-23:00', '18:00-23:00')
    )
    ism = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=30, choices=ISH_VAQTI_CHOICES)


    class Meta:
        verbose_name = 'Kutubxonachi'
        verbose_name_plural = 'Kutubxonachilar'

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    JINS_CHOICES = (
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol')
    )
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=5, choices=JINS_CHOICES)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'

    def __str__(self):
        return self.nom


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateTimeField()
    qaytargan_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Recordlar'

    def __str__(self):
        return f"{self.talaba.ism} - {self.kitob.nom}"
