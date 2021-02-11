import livingdoc2mongodb as Liv2Mong
import argparse
import logging
import sys
import time
logging.basicConfig(stream=sys.stdout, filemode='a', level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="MongoDB backend")
    parser.add_argument("-A", "--automate", help="automate server by time", nargs='+', type=int)
    parser.add_argument("-C", "--update", help="custum update", nargs='+', type=int)
    args = parser.parse_args()

    M2L = Liv2Mong.MongoLivingdocs()
    Mong = Liv2Mong.Mongo_2()

    if args.automate:

        """this is how we automate the procedure """

        logging.info("starting automation.... ")
        hiatus = args.automate[0]

        while True:
            logging.info("Updating MongoDB cluster0.".format(hiatus))
            starting_ind = M2L.update_articles()
            logging.info("Updating Django backend DB: Articles.".format(hiatus))
            Mong.update_articles(starting_ind)
            logging.info("going to sleep...\n hiatus: {0}".format(hiatus))
            time.sleep(hiatus)

    if args.update:

        logging.info("starting updating.... ")
        M2L.update_articles(args.update[0])
        Mong.update_articles(args.update[0])

if __name__ == "__main__":
    main()
