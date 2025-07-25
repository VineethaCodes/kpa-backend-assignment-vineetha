from rest_framework import serializers
from .models import (
    WheelSpecification, WheelFields,
    BogieChecksheet, BogieDetails, BogieChecksheetData, BMBCChecksheet
)

# =========================
#  WHEEL SERIALIZERS
# =========================

class WheelFieldsSerializer(serializers.ModelSerializer):
    # Map camelCase JSON fields to snake_case model fields using `source`
    treadDiameterNew = serializers.CharField(source='tread_diameter_new')
    lastShopIssueSize = serializers.CharField(source='last_shop_issue_size')
    condemningDia = serializers.CharField(source='condemning_dia')
    wheelGauge = serializers.CharField(source='wheel_gauge')
    variationSameAxle = serializers.CharField(source='variation_same_axle')
    variationSameBogie = serializers.CharField(source='variation_same_bogie')
    variationSameCoach = serializers.CharField(source='variation_same_coach')
    wheelProfile = serializers.CharField(source='wheel_profile')
    intermediateWWP = serializers.CharField(source='intermediate_wwp')
    bearingSeatDiameter = serializers.CharField(source='bearing_seat_diameter')
    rollerBearingOuterDia = serializers.CharField(source='roller_bearing_outer_dia')
    rollerBearingBoreDia = serializers.CharField(source='roller_bearing_bore_dia')
    rollerBearingWidth = serializers.CharField(source='roller_bearing_width')
    axleBoxHousingBoreDia = serializers.CharField(source='axle_box_housing_bore_dia')
    wheelDiscWidth = serializers.CharField(source='wheel_disc_width')

    class Meta:
        model = WheelFields
        fields = [
            'treadDiameterNew', 'lastShopIssueSize', 'condemningDia',
            'wheelGauge', 'variationSameAxle', 'variationSameBogie',
            'variationSameCoach', 'wheelProfile', 'intermediateWWP',
            'bearingSeatDiameter', 'rollerBearingOuterDia', 'rollerBearingBoreDia',
            'rollerBearingWidth', 'axleBoxHousingBoreDia', 'wheelDiscWidth'
        ]


class WheelSpecificationSerializer(serializers.ModelSerializer):
    # Top-level fields from the incoming JSON
    formNumber = serializers.CharField(source='form_number')
    submittedBy = serializers.CharField(source='submitted_by')
    submittedDate = serializers.DateField(source='submitted_date')
    fields = WheelFieldsSerializer()

    class Meta:
        model = WheelSpecification
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'fields']
        extra_kwargs = {
            'fields': {'required': True}
        }

    def create(self, validated_data):
        # Extract nested fields and create related objects
        fields_data = validated_data.pop('fields')
        wheel_fields = WheelFields.objects.create(**fields_data)
        wheel_spec = WheelSpecification.objects.create(fields=wheel_fields, **validated_data)
        return wheel_spec


# =========================
#  BOGIE SERIALIZERS
# =========================

class BogieDetailsSerializer(serializers.ModelSerializer):
    bogieNo = serializers.CharField(source='bogie_no')
    makerYearBuilt = serializers.CharField(source='maker_year_built')
    incomingDivAndDate = serializers.CharField(source='incoming_div_and_date')
    deficitComponents = serializers.CharField(source='deficit_components')
    dateOfIOH = serializers.DateField(source='date_of_ioh')

    class Meta:
        model = BogieDetails
        fields = ['bogieNo', 'makerYearBuilt', 'incomingDivAndDate', 'deficitComponents', 'dateOfIOH']


class BogieChecksheetDataSerializer(serializers.ModelSerializer):
    bogieFrameCondition = serializers.CharField(source='bogie_frame_condition')
    bolster = serializers.CharField()  # Same field name = no source needed
    bolsterSuspensionBracket = serializers.CharField(source='bolster_suspension_bracket')
    lowerSpringSeat = serializers.CharField(source='lower_spring_seat')
    axleGuide = serializers.CharField(source='axle_guide')

    class Meta:
        model = BogieChecksheetData
        fields = ['bogieFrameCondition', 'bolster', 'bolsterSuspensionBracket', 'lowerSpringSeat', 'axleGuide']


class BMBCChecksheetSerializer(serializers.ModelSerializer):
    cylinderBody = serializers.CharField(source='cylinder_body')
    pistonTrunnion = serializers.CharField(source='piston_trunnion')
    adjustingTube = serializers.CharField(source='adjusting_tube')
    plungerSpring = serializers.CharField(source='plunger_spring')

    class Meta:
        model = BMBCChecksheet
        fields = ['cylinderBody', 'pistonTrunnion', 'adjustingTube', 'plungerSpring']


class BogieChecksheetSerializer(serializers.ModelSerializer):
    formNumber = serializers.CharField(source='form_number')
    inspectionBy = serializers.CharField(source='inspection_by')
    inspectionDate = serializers.DateField(source='inspection_date')
    bogieDetails = BogieDetailsSerializer()
    bogieChecksheet = BogieChecksheetDataSerializer()
    bmbcChecksheet = BMBCChecksheetSerializer()

    class Meta:
        model = BogieChecksheet
        fields = [
            'formNumber', 'inspectionBy', 'inspectionDate',
            'bogieDetails', 'bogieChecksheet', 'bmbcChecksheet'
        ]

    def create(self, validated_data):
        # Extract nested data and create corresponding objects
        bogie_details_data = validated_data.pop('bogieDetails')
        bogie_checksheet_data = validated_data.pop('bogieChecksheet')
        bmbc_data = validated_data.pop('bmbcChecksheet')

        bogie_details = BogieDetails.objects.create(**bogie_details_data)
        bogie_checksheet = BogieChecksheetData.objects.create(**bogie_checksheet_data)
        bmbc_checksheet = BMBCChecksheet.objects.create(**bmbc_data)

        return BogieChecksheet.objects.create(
            bogie_details=bogie_details,
            bogie_checksheet=bogie_checksheet,
            bmbc_checksheet=bmbc_checksheet,
            **validated_data
        )
