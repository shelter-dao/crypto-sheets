import logging
import time

from google.oauth2 import service_account
from googleapiclient import discovery, errors

from .clients import FTX_US


GCP_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
GCP_SERVICE_ACCOUNT_CREDENTIALS = "service-account.json"
SHEET_ID = "1nH82URxwnH_ay8dFWBJITxV1GiJ8h4yOTqtPgUhfJ1Q"
SHEET_RANGE = "Sheet1"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


def get_gcp_creds():
    creds = service_account.Credentials.from_service_account_file(
        GCP_SERVICE_ACCOUNT_CREDENTIALS, scopes=GCP_SCOPES
    )

    return creds


def main():
    with discovery.build(
        "sheets",
        "v4",
        credentials=get_gcp_creds(),
        cache_discovery=False,
    ).spreadsheets() as sheets:
        ftx_us = FTX_US()

        while True:
            price = ftx_us.fetch_price(ticker="BTC/USD")
            logging.info(f"BTC/USD: {price}")

            values = [
                ["BTC/USD", price],
            ]

            sheet_id = SHEET_ID
            range = SHEET_RANGE
            value_input_option = "RAW"
            body = {"values": values}

            request = sheets.values().update(
                spreadsheetId=sheet_id,
                range=range,
                valueInputOption=value_input_option,
                body=body,
            )

            try:
                response = request.execute()
                logging.info("Sheet updated. Sleeping...")
                time.sleep(1.5)
            except errors.HttpError as e:
                logging.error("Bad request. Trying again. Sleeping...")
                time.sleep(60)


if __name__ == "__main__":
    main()
