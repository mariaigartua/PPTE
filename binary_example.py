from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from binary_data import models
from binary_data.models import Hyperlink
from binary_data.models import Label


SITES_TO_PRINT = 10
HYPERLINKS_TO_PRINT = 20


def main():
    engine = create_engine('sqlite:///binary_data/policies.db')

    Session = sessionmaker(bind=engine)
    session = Session()

    sites = session.query(models.Site)
    for site in sites[:SITES_TO_PRINT]:
        print('Site URL:', site.url)
        print('Alexa Rank:', site.alexa_rank)

        for policy in site.policies:
            print('Policy URL:', policy.url)

            hyperlinks = policy.hyperlinks.filter(or_(
                Hyperlink.label == Label.Positive,
                Hyperlink.label == Label.Negative))
            for hyperlink in hyperlinks[:HYPERLINKS_TO_PRINT]:
                print('Hyperlink URL:', hyperlink.url)
                print('Sentence Text:', hyperlink.full_sentence_text)
                print('Opt-out:', (hyperlink.label == Label.Positive))

                print()


if __name__ == '__main__':
    main()
