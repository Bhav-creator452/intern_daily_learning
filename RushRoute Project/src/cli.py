import json
import logging

from validator import validate_delivery, ValidationError
from scorer import late_risk_label

logging.basicConfig(level=logging.INFO)


def process_file(filename):

    with open(filename, "r") as file:
        deliveries = json.load(file)

    success = 0
    failed = 0

    for index, delivery in enumerate(deliveries, start=1):

        try:
            validate_delivery(delivery)

            risk = late_risk_label(
                delivery["distance_km"],
                delivery["active_orders"],
                delivery["weather"],
                delivery["pickup_hour"]
            )

            logging.info(
                f"Record {index}: Risk = {risk}"
            )

            success += 1

        except ValidationError as error:

            logging.error(
                f"Record {index}: {error}"
            )

            failed += 1

    logging.info(
        f"Processed: {success} successful, {failed} failed."
    )

    return failed