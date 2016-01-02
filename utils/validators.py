from django.core.validators import MinValueValidator, MaxValueValidator

year_validators = [MinValueValidator(1930), MaxValueValidator(2100)]
mark5_validators = [MinValueValidator(2), MaxValueValidator(5)]
level_validators = [MinValueValidator(1), MaxValueValidator(7)]