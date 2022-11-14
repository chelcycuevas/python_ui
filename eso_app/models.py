from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.

class Gear(models.Model):
    SLOT = (
        ('HEAD', 'Head'),
        ('SHOULDERS', 'Shoulders'),
        ('CHEST', 'Chest'),
        ('HANDS', 'Hands'),
        ('BELT', 'Belt'),
        ('SHOES', 'Shoes'),
        ('PANTS', 'Pants'),
        ('NECKLACE', 'Necklace'),
        ('RING1', 'Ring 1'),
        ('RING2', 'Ring 2'),
        ('W1', 'Frontbar Weapon'),
        ('W2', 'Backbar Weapon')
    )
    slot = models.CharField(max_length=500, choices=SLOT, default="")
    set = models.TextField(max_length=500, default="")
    WEIGHT = (
        ('L', 'Light'),
        ('M', 'Medium'),
        ('H', 'Heavy')
    )
    weight = models.CharField(max_length=100, choices=WEIGHT, default="")
    trait = models.CharField(max_length=100, default="")
    enchantment = models.CharField(max_length=100, default="")


class Classes(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class-detail', args=[str(self.id)])


class Skills(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    clazz = models.ForeignKey(Classes, db_column='class', on_delete=models.CASCADE, verbose_name="class")
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['clazz']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skill-detail', args=[str(self.id)])


class BuildEditor(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000, verbose_name='Description', blank=True, default="")
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=20, choices=GENDERS, blank=True)
    ALLIANCES = (
        ('ALDMERI', 'Aldmeri Dominion'),
        ('DAGGERFALL', 'Daggerfall Covenant'),
        ('EBONHEART', 'Ebonheart Pact')
    )
    alliance = models.CharField(max_length=50, choices=ALLIANCES)
    RACES = (
        ('BRETON', 'Breton'),
        ('KHAJIT', 'Khajit'),
        ('ORC', 'Orc'),
        ('HIGH_ELF', 'High Elf'),
        ('DARK_ELF', 'Dark Elf'),
        ('WOOD_ELF', 'Wood Elf'),
        ('ARGONIAN', 'Argonian'),
        ('REDGUARD', 'Redguard'),
        ('NORD', 'Nord'),
        ('IMPERIAL', 'Imperial')
    )
    race = models.CharField(max_length=30, choices=RACES)
    CLASSES = (
        ('DK', 'Dragonknight'),
        ('TP', 'Templar'),
        ('WD', 'Warden'),
        ('SC', 'Sorcerer'),
        ('NC', 'Necromancer'),
        ('NB', 'Nightblade')
    )
    clazz = models.CharField(max_length=30, choices=CLASSES, db_column='class', verbose_name='class')
    head = models.CharField(max_length=100, blank=True, default="")
    shoulders = models.CharField(max_length=100, blank=True, default="")
    chest = models.CharField(max_length=100, blank=True, default="")
    legs = models.CharField(max_length=100, blank=True, default="")
    hands = models.CharField(max_length=100, blank=True, default="")
    waist = models.CharField(max_length=100, blank=True, default="")
    feet = models.CharField(max_length=100, blank=True, default="")
    necklace = models.CharField(max_length=100, blank=True, default="")
    ring_one = models.CharField(max_length=100, blank=True, default="")
    ring_two = models.CharField(max_length=100, blank=True, default="")
    frontbar_weapon = models.CharField(max_length=100, blank=True, default="")
    frontbar_skill_one = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    frontbar_skill_two = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    frontbar_skill_three = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    frontbar_skill_four = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    frontbar_skill_five = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    frontbar_ultimate = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    backbar_weapon = models.CharField(max_length=100, blank=True, default="")
    backbar_skill_one = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    backbar_skill_two = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    backbar_skill_three = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    backbar_skill_four = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    backbar_skill_five = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    backbar_ultimate = models.ForeignKey(Skills, on_delete=models.CASCADE, blank=True, default="", related_name='+')
    ROLES = (
        ('T', 'Tank'),
        ('D', 'Damage Dealer'),
        ('H', 'Healer')
    )
    role = models.CharField(max_length=50, choices=ROLES)
    PLAY_STYLE = (
        ('PVP', 'PVP'),
        ('PVE', 'PVE')
    )
    playstyle = models.CharField(max_length=10, choices=PLAY_STYLE, verbose_name='Play Style')
    CURSES = (
        ('V', 'Vampire'),
        ('W', 'Werewolf')
    )
    curse = models.CharField(max_length=50, choices=CURSES, blank=True, default="", help_text="Optional")
    MUNDUS_STONES = (
        ('APPRENTICE', 'The Apprentice'),
        ('ATRONACH', 'The Atronach'),
        ('LADY', 'The Lady'),
        ('LORD', 'The Lord'),
        ('LOVER', 'The Lover'),
        ('MAGE', 'The Mage'),
        ('RITUAL', 'The Ritual'),
        ('SERPENT', 'The Serpent'),
        ('SHADOW', 'The Shadow'),
        ('STEED', 'The Steed'),
        ('THIEF', 'The Thief'),
        ('TOWER', 'The Tower'),
        ('WARRIOR', 'The Warrior')
    )
    mundus = models.CharField(max_length=100, choices=MUNDUS_STONES)
    attributes_health = models.IntegerField(default=0, validators=[MaxValueValidator(64), MinValueValidator(0)],
                                            verbose_name="Health")
    attributes_magicka = models.IntegerField(default=0, validators=[MaxValueValidator(64), MinValueValidator(0)],
                                             verbose_name="Magicka")
    attributes_stamina = models.IntegerField(default=0, validators=[MaxValueValidator(64), MinValueValidator(0)],
                                             verbose_name="Stamina")
    house = models.CharField(max_length=500)
    mount = models.CharField(max_length=500)
    video = models.URLField(default="", blank=True)
    image = models.ImageField(upload_to='images/% Y/% m/% d/', default="default.jpg", blank=True)

    class Meta:
        ordering = ['-name']

    # map this value to the url for the detail view
    def get_absolute_url(self):
        return reverse('build-detail', args=[str(self.id)])


class Alliances(models.Model):
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    motto = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description', default="")
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('alliance-detail', args=[str(self.id)])


class Zones(models.Model):
    name = models.CharField(max_length=200)
    alliance = models.ForeignKey(Alliances, on_delete=models.CASCADE, blank=True)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zone-detail', args=[str(self.id)])


class Races(models.Model):
    name = models.CharField(max_length=100)
    alliance = models.ForeignKey(Alliances, on_delete=models.CASCADE, blank=True, null=True, default="")
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zone-detail', args=[str(self.id)])


class DLCs(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['release_date']

    def __str__(self):
        return self.name


class Trials(models.Model):
    name = models.CharField(max_length=100)
    dlc = models.ForeignKey(DLCs, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Dungeons(models.Model):
    name = models.CharField(max_length=200)
    dlc = models.ForeignKey(DLCs, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Arenas(models.Model):
    name = models.CharField(max_length=200)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Mythics(models.Model):
    name = models.CharField(max_length=200)
    dlc = models.ForeignKey(DLCs, on_delete=models.CASCADE)
    items = models.CharField(max_length=200)
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class MonsterSets(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=10)
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    image_url = models.URLField(default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Characters(models.Model):
    name = models.CharField(max_length=200)
    alliance = models.ForeignKey(Alliances, on_delete=models.CASCADE)
    clazz = models.ForeignKey(Classes, db_column='class', on_delete=models.CASCADE, verbose_name="class")
    race = models.ForeignKey(Races, on_delete=models.CASCADE)
