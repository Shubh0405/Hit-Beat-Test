from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    profile_pic = models.URLField(max_length=200)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class BeatSound(models.Model):
    title = models.CharField(max_length=250, unique=True,primary_key=True)
    beat_image = models.ImageField(upload_to='beat_images')
    beat_file = models.FileField(upload_to ='beat_files')

    def __str__(self):
        return self.title

class UserSound(models.Model):
    user = models.ForeignKey(UserData,on_delete=models.CASCADE,related_name="user_sound")
    beat_audio = models.ForeignKey(BeatSound,on_delete=models.CASCADE)
    user_audio = models.FileField(upload_to ='user_audios')
    user_score = models.FloatField()

    def __str__(self):
        return self.user.name + ' try ' + self.beat_audio.title

class UserFavourite(models.Model):
    user = models.ForeignKey(UserData,on_delete=models.CASCADE,related_name="user_favourite")
    beat = models.ForeignKey(BeatSound,on_delete=models.CASCADE,related_name="beat_favourite")

    class Meta:
        unique_together = ('user','beat')

    def __str__(self):
        return self.beat + ' starred by ' + self.user
