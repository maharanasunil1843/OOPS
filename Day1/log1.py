import logging

logging.basicConfig(filename="test2.log", level= logging.INFO, format="%(levelname)s %(name)s %(asctime)s %(message)s")

def divide(a,b):
    logging.info("the number entered by user is  %s and %s", a, b)
    try:
        logging.info("we are into the function")
        div = a/b
        logging.info("we have completed the division operation")
        logging.info("the result of the division is %s", div)
        return div
    except Exception as e:
        logging.exception(e)

divide(3,10)