from django.db import models

# Create your models here.
## model that holds the infinitive of verbs and functions needed for the app
class Verb(models.Model):
    infinitive = models.Charfield(max_length=50, unique=True)
    regular_irregular = models.CharField(max_length=50)
    conjugation_type = models.CharField(max_length=50)

    def __str__(self):
        return self.infinitive


## model that holds the conjugated forms of verbs
class Conjugation(models.Model):
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE, related_name='conjugations')
    conjugation_code = models.CharField(max_length=50)
    tense = models.CharField(max_length=50)
    mood = models.CharField(max_length=50)
    person = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)  # This could represent singular/plural or other quantifiers
    form = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.form}"
    
