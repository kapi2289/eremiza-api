import related
from aenum import MultiValueEnum


class AlarmKind(MultiValueEnum):
    MOBILE = "Aplikacja mobilna", 0
    SWD = "SWD-ST", 1
    TGB = "TGB", 2
    COMBAT_TEST = "Gotowość bojowa", 3


class AlarmNotificationStatus(MultiValueEnum):
    NOTIFIED = "Brak", 0
    CONFIRMED = "Potwierdzony", 1
    DECLINED = "Odrzucony", 2
    DELIVERED = "Dostarczony", 3


class LocationAccuracy(MultiValueEnum):
    UNKNOWN = "Nieznana", 0
    COUNTRY = "Kraj", 1
    VOIVODESHIP = "Województwo", 2
    DISTRICT = "Powiat", 3
    MUNICIPALITY = "Gmina", 4
    LOCALITY = "Miejscowość", 5
    STREET = "Ulica", 6
    NEAREST_ADDRESS_POINT = "Najbliższy punkt adresowy", 7
    ADDRESS_POINT_OSM = "Punkt adresowy z OSM", 8
    ADDRESS_POINT_EMUIA = "Punkt adresowy z EMUiA", 9
    MANUAL = "Wpisane ręcznie", 10
    TERMINAL = "Ustawione przez urządzenie (terminal)", 11
    ADDRESS_POINT_SIWCPR = "Punkt adresowy z SI WCPR", 12


@related.immutable
class Alarm:
    ou_id = related.IntegerField(key="ouId", required=False)
    ou_name = related.StringField(key="ouName", required=False)
    bsis_name = related.StringField(key="bsisName", required=False)
    dispatched_bsis_name = related.StringField(key="dispatchedBsisName", required=False)
    kind = related.ChildField(AlarmKind, required=False)
    sub_kind = related.StringField(key="subKind", required=False)
    description = related.StringField(required=False)
    acquired = related.DateTimeField(key="aquired", required=False)
    expiration = related.DateTimeField(required=False)
    latitude = related.FloatField(required=False)
    longitude = related.FloatField(required=False)
    location_accuracy = related.ChildField(LocationAccuracy, key="locAccuracy", required=False)
    distance_to_fire_station = related.FloatField(key="distanceToFireStation", required=False)
    adm_territory = related.StringField(key="admTeryt", required=False)
    locality = related.StringField(required=False)
    street = related.StringField(required=False)
    address_point = related.StringField(key="addrPoint", required=False)
    apartment = related.StringField(required=False)
    notified = related.IntegerField(required=False)
    confirmed = related.IntegerField(required=False)
    declined = related.IntegerField(required=False)
    commanders = related.IntegerField(required=False)
    drivers = related.IntegerField(required=False)
    drivers_cat_c = related.IntegerField(key="driversCatC", required=False)
    firstAid = related.IntegerField(required=False)
    status = related.ChildField(AlarmNotificationStatus, required=False)
    modified = related.DateTimeField(required=False)
    rec_ver_no = related.IntegerField(key="recVerNo", required=False)
    deleted = related.BooleanField(required=False)
    swd_id = related.IntegerField(key="swdId", required=False)
    id = related.IntegerField(required=False)

    @property
    def address(self):
        result = ""
        if self.locality:
            result += self.locality.strip()
        if self.street:
            result += ", {}".format(self.street.strip())
        if self.address_point:
            result += " {}".format(self.address_point.strip())
            if self.apartment:
                result += "/{}".format(self.apartment.strip())
        return result
