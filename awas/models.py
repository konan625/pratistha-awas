from django.db import models

# class Reservation(models.Model):
#     persons_reserved = models.IntegerField(null=True, blank=True)
#     location= models.ForeignKey(Location, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = 'Reservation'
#         verbose_name_plural = 'Reservations'

#     def save(self, *args, **kwargs):
#         print(f"saving reservation {self.guest_set}")
#         super(Reservation, self).save(*args, **kwargs) 


class Location(models.Model):
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    transport = models.TextField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    lock_no = models.TextField(null=True, blank=True)
    awas_incharge = models.TextField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    checkin_time = models.TimeField(null=True, blank=True)
    checkout_time = models.TimeField(null=True, blank=True)
    map_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.description + self.address

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class Guest(models.Model):
    guest_name = models.TextField()
    city = models.TextField(null=True, blank=True)
    mobile_no = models.CharField(max_length=10)
    ext_reg_no = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    remark = models.TextField(null=True, blank=True)
    no_of_persons = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    departure_date = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    mandal = models.TextField(null=True, blank=True)
    # reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.guest_name

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'


class Cities(models.Model):
    city_code = models.CharField(max_length=10)
    city_name = models.CharField(max_length=100)
    city_name_i18n = models.TextField(blank=True, null=True)
    districts_id = models.IntegerField()
    states_id = models.IntegerField()
    status = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'

    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return


class Countries(models.Model):
    country_name = models.CharField(max_length=64)
    country_code = models.CharField(max_length=2)
    country_isd_code = models.CharField(max_length=7, blank=True, null=True)
    status = models.IntegerField()
    is_allowed_sms = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'countries'

    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return


class Districts(models.Model):
    state_code = models.CharField(max_length=10, blank=True, null=True)
    district_code = models.CharField(max_length=10, blank=True, null=True)
    district_name = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'

    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return


class States(models.Model):
    state_code = models.CharField(max_length=10, blank=True, null=True)
    state_name = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'
    
    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return


class UserRegistration(models.Model):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    salutation = models.CharField(max_length=5, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=5, blank=True, null=True)
    category_id = models.CharField(max_length=16, blank=True, null=True)
    profession_id = models.CharField(max_length=64, blank=True, null=True)
    is_doctor = models.CharField(max_length=5, blank=True, null=True, db_comment="['true' => '1', 'false' => '0'];")
    is_brahmchari = models.CharField(max_length=5, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    district_id = models.IntegerField(blank=True, null=True)
    district_name = models.CharField(max_length=100, blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    mandal = models.CharField(max_length=255, blank=True, null=True)
    mandal_id = models.IntegerField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    arrival_time = models.CharField(max_length=20, blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    departure_time = models.CharField(max_length=20, blank=True, null=True)
    arrival_date_awas = models.DateField(blank=True, null=True)
    arrival_time_awas = models.CharField(max_length=20, blank=True, null=True)
    departure_date_awas = models.DateField(blank=True, null=True)
    departure_time_awas = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    awas_required = models.CharField(max_length=5, blank=True, null=True)
    awas_type = models.CharField(max_length=50, blank=True, null=True)
    transport_mode = models.CharField(max_length=255, blank=True, null=True)
    food_preference_id = models.IntegerField(blank=True, null=True)
    is_vehicle = models.CharField(max_length=5, blank=True, null=True)
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)
    is_driver = models.CharField(max_length=5, blank=True, null=True)
    driver_first_name = models.CharField(max_length=50, blank=True, null=True)
    driver_middle_name = models.CharField(max_length=50, blank=True, null=True)
    driver_last_name = models.CharField(max_length=50, blank=True, null=True)
    driver_gender = models.CharField(max_length=15, blank=True, null=True)
    driver_birth_date = models.DateField(blank=True, null=True)
    awas_for_driver = models.CharField(max_length=5, blank=True, null=True)
    driver_mobile = models.CharField(max_length=20, blank=True, null=True)
    members_info = models.TextField(blank=True, null=True)
    user_photo = models.CharField(max_length=255, blank=True, null=True)
    driver_photo = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    is_profile_completed = models.IntegerField(blank=True, null=True)
    is_account_locked = models.IntegerField(blank=True, null=True)
    account_locked_comment = models.TextField(blank=True, null=True)
    account_locked_at = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=16, blank=True, null=True)
    awas_allocation_id = models.IntegerField(blank=True, null=True)
    bhojan_allocation_id = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    assign_band_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_registration'
    
    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return