from datetime import datetime
from typing import Tuple
import logging

# ログ設定
logger = logging.getLogger(__name__)

def calculate_intervals_and_remainder(entered: datetime, left: datetime, interval_minutes: int = 30) -> Tuple[int, int]:
    """
    Calculate the number of intervals and the remainder between two datetime objects.
    
    :param entered: The start datetime object.
    :param left: The end datetime object.
    :param interval_minutes: The length of the interval in minutes. Must be greater than 0.
    :return: A tuple containing the number of intervals and the remainder in seconds.
    
    Example:
    >>> entered = datetime(2023, 10, 30, 17)
    >>> left = datetime(2023, 10, 30, 18, 31)
    >>> calculate_intervals_and_remainder(entered, left)
    (3, 60)
    """
    if interval_minutes <= 0:
        raise ValueError("interval_minutes must be greater than 0")

    logger.debug(f"Calculating intervals and remainder from {entered} to {left} with interval of {interval_minutes} minutes.")

    SECONDS_IN_INTERVAL = interval_minutes * 60

    total_seconds = int(left.timestamp() - entered.timestamp())
    intervals, remainder = divmod(total_seconds, SECONDS_IN_INTERVAL)

    logger.debug(f"Total seconds: {total_seconds}, Intervals: {intervals}, Remainder: {remainder}")

    return intervals, remainder

if __name__ == "__main__":
    from logger_config import configure_logger
    configure_logger()
    
    entered = datetime(2023, 10, 30, 17)
    left = datetime(2023, 10, 30, 18, 31)

    intervals, remainder = calculate_intervals_and_remainder(entered, left)

    print(f"Intervals: {intervals}")  # 30分単位の区間数
    print(f"Remainder: {remainder} seconds")  # 30分ちょっと（例えば30分10秒）のようなケースでもここであまりは取得できる

