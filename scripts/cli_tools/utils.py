import click
import time
import typing


def sleep(progress_bar: click.progressbar, time_sleep: typing.Union[int, float], step: int = 25):
    progress_bar.update(step)
    time.sleep(time_sleep)
