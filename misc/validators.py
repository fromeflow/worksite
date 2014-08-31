from django.core.validators import MinValueValidator, MaxValueValidator

work_year_validator = [MinValueValidator(1930), MaxValueValidator(2100)]
mark5_validator = [MinValueValidator(2), MaxValueValidator(5)]