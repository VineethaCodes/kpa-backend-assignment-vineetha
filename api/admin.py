from django.contrib import admin
from .models import (
    BogieChecksheet,
    BogieChecksheetData,
    BogieDetails,
    BMBCChecksheet,
    WheelSpecification,
    WheelFields
)

admin.site.register(BogieChecksheet)
admin.site.register(BogieChecksheetData)
admin.site.register(BogieDetails)
admin.site.register(BMBCChecksheet)
admin.site.register(WheelSpecification)
admin.site.register(WheelFields)
