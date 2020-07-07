from django.db import models


class Genres(models.Model):
    _id = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Genres"


class Movies(models.Model):

    title = models.CharField(max_length=50)
    numberInStock = models.PositiveIntegerField()
    dailyRentalRate = models.FloatField()
    movieId = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # # , db_column="name",
    @property
    def genreName(self):
        return self.genre.name

    class Meta:
        verbose_name_plural = "Movies"


# Movies( title= "Get Out",genre= Genres(pk=2),numberInStock= 8,dailyRentalRate= 3.5)
