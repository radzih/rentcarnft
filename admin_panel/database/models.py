from django.db import models


def _create_photo_path(self, filename):
    '''Create a path for the photo'''
    uploaded_file_extension = filename.split('.')[-1]
    return f'./images/{self.address}_{self.token_id}.{uploaded_file_extension}'

class CarModel(models.Model):
    '''Model that represents a car model'''
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class NFTCar(models.Model):
    '''Model that represents a NFT'''
    owner_addr = models.CharField(max_length=255, default=None)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    token_id = models.CharField(max_length=255)
    owned = models.BooleanField(default=False)
    part = models.IntegerField()
    secret_code = models.CharField(max_length=200)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=_create_photo_path)
    rent_days = models.IntegerField(default=0)
    earned_money = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    paid_out = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    
    def __str__(self) -> str:
        '''Returns the string representation of the model'''
        return self.name
        
class User(models.Model):
    '''Model that represents bot user'''
    
    class Languages(models.TextChoices):
        '''Languages that bot can use'''
        EN = 'en'
        IT = 'it'
        RU = 'ru'
        
    
    telegram_id = models.BigIntegerField(unique=True)
    owned_cars = models.ManyToManyField(NFTCar, blank=True)
    last_request = models.DateTimeField(auto_now_add=True) 
    language = models.CharField(
        max_length=2, choices=Languages.choices, default=Languages.EN)
     
    def __str__(self) -> str:
        '''Returns the string representation of the model'''
        return str(self.telegram_id)
    