from django.db import models

# Wheel Fields
class WheelFields(models.Model):
    tread_diameter_new = models.CharField(max_length=100)
    last_shop_issue_size = models.CharField(max_length=100)
    condemning_dia = models.CharField(max_length=100)
    wheel_gauge = models.CharField(max_length=100)
    variation_same_axle = models.CharField(max_length=100)
    variation_same_bogie = models.CharField(max_length=100)
    variation_same_coach = models.CharField(max_length=100)
    wheel_profile = models.CharField(max_length=100)
    intermediate_wwp = models.CharField(max_length=100)
    bearing_seat_diameter = models.CharField(max_length=100)
    roller_bearing_outer_dia = models.CharField(max_length=100)
    roller_bearing_bore_dia = models.CharField(max_length=100)
    roller_bearing_width = models.CharField(max_length=100)
    axle_box_housing_bore_dia = models.CharField(max_length=100)
    wheel_disc_width = models.CharField(max_length=100)

    def __str__(self):
        return f"WheelFields #{self.id}"

class WheelSpecification(models.Model):
    class StatusChoices(models.TextChoices):
        SAVED = "Saved"
        SUBMITTED = "Submitted"

    form_number = models.CharField(max_length=50, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    fields = models.OneToOneField(WheelFields, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.SAVED)

    def __str__(self):
        return f"WheelSpecification - {self.form_number}"

    class Meta:
        ordering = ['-submitted_date']

# Bogie Models
class BogieDetails(models.Model):
    bogie_no = models.CharField(max_length=50)
    maker_year_built = models.CharField(max_length=100)
    incoming_div_and_date = models.CharField(max_length=100)
    deficit_components = models.CharField(max_length=255)
    date_of_ioh = models.DateField()

    def __str__(self):
        return f"{self.bogie_no} - {self.maker_year_built}"

class BogieChecksheetData(models.Model):
    bogie_frame_condition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolster_suspension_bracket = models.CharField(max_length=100)
    lower_spring_seat = models.CharField(max_length=100)
    axle_guide = models.CharField(max_length=100)

    def __str__(self):
        return f"BogieChecksheetData #{self.id}"

class BMBCChecksheet(models.Model):
    cylinder_body = models.CharField(max_length=100)
    piston_trunnion = models.CharField(max_length=100)
    adjusting_tube = models.CharField(max_length=100)
    plunger_spring = models.CharField(max_length=100)

    def __str__(self):
        return f"BMBCChecksheet #{self.id}"

class BogieChecksheet(models.Model):
    class StatusChoices(models.TextChoices):
        SAVED = "Saved"
        SUBMITTED = "Submitted"

    form_number = models.CharField(max_length=50, unique=True)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()
    bogie_details = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)
    bogie_checksheet = models.OneToOneField(BogieChecksheetData, on_delete=models.CASCADE)
    bmbc_checksheet = models.OneToOneField(BMBCChecksheet, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.SAVED)

    def __str__(self):
        return f"BogieChecksheet - {self.form_number}"

    class Meta:
        ordering = ['-inspection_date']
