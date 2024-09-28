from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
COUNTRY_CHOICES = [
    ('United States', 'United States'),
    ('Canada', 'Canada'),
    ('Mexico', 'Mexico'),
    ('United Kingdom', 'United Kingdom'),
    ('Germany', 'Germany'),
    ('France', 'France'),
    ('Italy', 'Italy'),
    ('Spain', 'Spain'),
    ('Netherlands', 'Netherlands'),
    ('Belgium', 'Belgium'),
    ('Austria', 'Austria'),
    ('Switzerland', 'Switzerland'),
    ('Sweden', 'Sweden'),
    ('Denmark', 'Denmark'),
    ('Norway', 'Norway'),
    ('Finland', 'Finland'),
    ('Ireland', 'Ireland'),
    ('Portugal', 'Portugal'),
    ('Greece', 'Greece'),
    ('Poland', 'Poland'),
    ('Czech Republic', 'Czech Republic'),
    ('Hungary', 'Hungary'),
    ('Romania', 'Romania'),
    ('Russia', 'Russia'),
    ('Australia', 'Australia'),
    ('New Zealand', 'New Zealand'),
    ('Japan', 'Japan'),
    ('South Korea', 'South Korea'),
    ('China', 'China'),
    ('Hong Kong', 'Hong Kong'),
    ('Taiwan', 'Taiwan'),
    ('Singapore', 'Singapore'),
    ('Malaysia', 'Malaysia'),
    ('Thailand', 'Thailand'),
    ('Indonesia', 'Indonesia'),
    ('Philippines', 'Philippines'),
    ('Vietnam', 'Vietnam'),
    ('India', 'India'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Turkey', 'Turkey'),
    ('South Africa', 'South Africa'),
    ('Brazil', 'Brazil'),
    ('Argentina', 'Argentina'),
    ('Chile', 'Chile'),
    ('Colombia', 'Colombia'),
    ('Peru', 'Peru'),
    ('Israel', 'Israel'),
    ('Egypt', 'Egypt'),
]

CITY_CHOICES = {
    'United States': [
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Chicago', 'Chicago'),
        # Thêm các thành phố khác của Mỹ
    ],
    'Canada': [
        ('Toronto', 'Toronto'),
        ('Vancouver', 'Vancouver'),
        ('Montreal', 'Montreal'),
        # Thêm các thành phố khác của Canada
    ],
    'Mexico': [
        ('Mexico City', 'Mexico City'),
        ('Guadalajara', 'Guadalajara'),
        ('Monterrey', 'Monterrey'),
        # Thêm các thành phố khác của Mexico
    ],
    'United Kingdom': [
        ('London', 'London'),
        ('Manchester', 'Manchester'),
        ('Birmingham', 'Birmingham'),
        # Thêm các thành phố khác của Vương Quốc Anh
    ],
    'Germany': [
        ('Berlin', 'Berlin'),
        ('Munich', 'Munich'),
        ('Hamburg', 'Hamburg'),
        # Thêm các thành phố khác của Đức
    ],
    'France': [
        ('Paris', 'Paris'),
        ('Marseille', 'Marseille'),
        ('Lyon', 'Lyon'),
        # Thêm các thành phố khác của Pháp
    ],
    'Italy': [
        ('Rome', 'Rome'),
        ('Milan', 'Milan'),
        ('Naples', 'Naples'),
        # Thêm các thành phố khác của Ý
    ],
    'Spain': [
        ('Madrid', 'Madrid'),
        ('Barcelona', 'Barcelona'),
        ('Valencia', 'Valencia'),
        # Thêm các thành phố khác của Tây Ban Nha
    ],
    # Tiếp tục thêm các lựa chọn thành phố cho các quốc gia khác...
}

VILLAGE_CHOICES = {
    'New York': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của New York
    ],
    'Los Angeles': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Los Angeles
    ],
    'Toronto': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Toronto
    ],
    'Vancouver': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Vancouver
    ],
    'Mexico City': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Mexico City
    ],
    'London': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của London
    ],
    'Berlin': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Berlin
    ],
    'Paris': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Paris
    ],
    'Rome': [
        ('Village1', 'Village 1'),
        ('Village2', 'Village 2'),
        # Thêm các làng khác của Rome
    ],
    # Tiếp tục thêm các lựa chọn làng cho các thành phố khác...
}



class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, phone_number=None, password=None, country=None, city=None, village=None, address=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            country=country,        # Thêm country
            city=city,              # Thêm city
            village=village,        # Thêm village
            address=address         # Thêm address
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, phone_number=None, password=None, country=None, city=None, village=None, address=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            country=country,        # Thêm country
            city=city,              # Thêm city
            village=village,        # Thêm village
            address=address         # Thêm address
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='Vietnam')
    city = models.CharField(max_length=50, blank=True, null=True)
    village = models.CharField(max_length=50, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True