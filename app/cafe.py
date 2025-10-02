import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:  # type: ignore
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", False):  # type: ignore
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
