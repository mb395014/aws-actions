import argparse
import datetime
from dateutil import tz
from dateutil.tz import tzutc


import json
from RotateAccessKey import RotateAccessKey

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Rotates")

    parser.add_argument(
        "--access-key-id",
        help="sum the integers (default: find the max)",
    )
    parser.add_argument(
        "--access-secret-id",
        help="sum the integers (default: find the max)",
    )

    args = parser.parse_args()
    new_secret_access_key = RotateAccessKey(
        access_key_id=args.access_key_id, secret_access_key=args.access_secret_id
    ).rotate_access_keys()
    print(new_secret_access_key)
