from app.cafe import Cafe, Visitor
from app.errors \
    import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError


def go_to_cafe(friends: list[Visitor], cafe: "Cafe") -> str:
    masks_to_buy = 0

    for fried in friends:
        try:
            cafe.visit_cafe(fried)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
