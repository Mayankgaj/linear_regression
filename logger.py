import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="debug.log",
    format="%(asctime)s %(levelname)s : %(message)s ",
    datefmt="%d-%m-%Y %H:%M:%S",
)

log = logging.getLogger()
log.setLevel(logging.DEBUG)