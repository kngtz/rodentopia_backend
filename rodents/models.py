from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Cage(models.Model):
    STOCK = 'Stock'
    BREEDING = 'Breeding'
    EXPERIMENTAL = 'Experimental'
    CAGE_TYPE_CHOICES = [
        (STOCK, 'STOCK'),
        (BREEDING, 'BREEDING'),
        (EXPERIMENTAL, 'EXPERIMENTAL'),
    ]
    SBIC = 'Singapore Bioimaging Consortium'
    BTI = 'Bioprocessing Technology Institute'
    RI_CHOICES = [
        (SBIC, 'SBIC'),
        (BTI, 'BTI'),
    ]
    TOMMY_TAN = 'TOMMY TAN'
    LIM_XIU_XIU = 'LIM XIU XIU'
    EXPERIMENTAL = 'E'
    PI_CHOICES = [
        (TOMMY_TAN, 'TOMMY TAN'),
        (LIM_XIU_XIU, 'LIM XIU XIU'),
    ]
    D1 = 'Department 1'
    D2 = 'Department 2'
    FACILITY_CHOICES = [
        (D1, 'D1'),
        (D2, 'D2'),

    ]
    ROOM1 = 'ROOM 1'
    ROOM2 = 'ROOM 2'
    ROOM3 = 'ROOM 3'
    ROOM4 = 'ROOM 4'
    ROOM5 = 'ROOM 5'
    ROOM_CHOICES = [
        (ROOM1, 'ROOM 1'),
        (ROOM2, 'ROOM 2'),
        (ROOM3, 'ROOM 3'),
        (ROOM4, 'ROOM 4'),
        (ROOM5, 'ROOM 5'),
    ]
    RACK1 = 'RACK 1'
    RACK2 = 'RACK 2'
    RACK3 = 'RACK 3'
    RACK4 = 'RACK 4'
    RACK5 = 'RACK 5'
    RACK_CHOICES = [
        (RACK1, 'RACK 1'),
        (RACK2, 'RACK 2'),
        (RACK3, 'RACK 3'),
        (RACK4, 'RACK 4'),
        (RACK5, 'RACK 5'),
    ]
    COLUMN1 = 'A'
    COLUMN2 = 'B'
    COLUMN3 = 'C'
    COLUMN4 = 'D'
    COLUMN5 = 'E'
    COLUMN6 = 'F'
    COLUMN7 = 'G'
    COLUMN_CHOICES = [
        (COLUMN1, 'A'),
        (COLUMN2, 'B'),
        (COLUMN3, 'C'),
        (COLUMN4, 'D'),
        (COLUMN5, 'E'),
        (COLUMN6, 'F'),
        (COLUMN7, 'G'),
    ]
    ROW1 = '1'
    ROW2 = '2'
    ROW3 = '3'
    ROW4 = '4'
    ROW5 = '5'
    ROW6 = '6'
    ROW7 = '7'
    ROW_CHOICES = [
        (ROW1, '1'),
        (ROW2, '2'),
        (ROW3, '3'),
        (ROW4, '4'),
        (ROW5, '5'),
        (ROW6, '6'),
        (ROW7, '7'),
    ]

    ri = models.CharField(
        max_length=100,
        choices=RI_CHOICES,
        default=SBIC,
    )
    pi = models.CharField(
        max_length=100,
        choices=PI_CHOICES,
        default=TOMMY_TAN,
    )
    researcher = models.CharField(max_length=100)
    cage_type = models.CharField(
        max_length=15,
        choices=CAGE_TYPE_CHOICES,
        default=STOCK,
    )

    facility = models.CharField(
        max_length=20,
        choices=FACILITY_CHOICES,
        default=D1,
    )

    room = models.CharField(
        max_length=20,
        choices=ROOM_CHOICES,
        default=D1,
    )

    rack = models.CharField(
        max_length=20,
        choices=RACK_CHOICES,
        default=RACK1,
    )

    column = models.CharField(
        max_length=20,
        choices=COLUMN_CHOICES,
        default=COLUMN1,
    )

    row = models.CharField(
        max_length=20,
        choices=ROW_CHOICES,
        default=ROW1,
    )

    def __str__(self):
        return '{}, {}, {}, {}{}'.format(self.facility, self.room, self.rack, self.column, self.row)
