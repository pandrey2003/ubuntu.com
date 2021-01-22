#! /usr/bin/env python3

import sys
from datetime import datetime

sys.path.insert(0, "")

# Start of script
from webapp.security.database import db_session  # noqa
from webapp.security.models import Release  # noqa


def load_releases():
    releases = [
        Release(
            codename="warty",
            version="4.10",
            name="Warty Warthog",
            development=False,
            lts=False,
            release_date=datetime.strptime("2004-10-20", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2004-10-20", "%Y-%m-%d"),
            support_expires=datetime.strptime("2004-10-20", "%Y-%m-%d"),
        ),
        Release(
            codename="hoary",
            version="5.04",
            name="Hoary Hedgehog",
            development=False,
            lts=False,
            release_date=datetime.strptime("2005-04-08", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2005-04-08", "%Y-%m-%d"),
            support_expires=datetime.strptime("2005-04-08", "%Y-%m-%d"),
        ),
        Release(
            codename="breezy",
            version="5.10",
            name="Breezy Badger",
            development=False,
            lts=False,
            release_date=datetime.strptime("2005-10-13", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2005-10-13", "%Y-%m-%d"),
            support_expires=datetime.strptime("2005-10-13", "%Y-%m-%d"),
        ),
        Release(
            codename="dapper",
            version="6.06",
            name="Dapper Drake",
            development=False,
            lts=True,
            release_date=datetime.strptime("2006-06-01", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2006-06-01", "%Y-%m-%d"),
            support_expires=datetime.strptime("2006-06-01", "%Y-%m-%d"),
        ),
        Release(
            codename="edgy",
            version="6.10",
            name="Edgy Eft",
            development=False,
            lts=False,
            release_date=datetime.strptime("2006-10-26", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2006-10-26", "%Y-%m-%d"),
            support_expires=datetime.strptime("2006-10-26", "%Y-%m-%d"),
        ),
        Release(
            codename="feisty",
            version="7.04",
            name="Feisty Fawn",
            development=False,
            lts=False,
            release_date=datetime.strptime("2007-04-19", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2007-04-19", "%Y-%m-%d"),
            support_expires=datetime.strptime("2007-04-19", "%Y-%m-%d"),
        ),
        Release(
            codename="gutsy",
            version="7.10",
            name="Gutsy Gibbon",
            development=False,
            lts=False,
            release_date=datetime.strptime("2007-10-18", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2007-10-18", "%Y-%m-%d"),
            support_expires=datetime.strptime("2007-10-18", "%Y-%m-%d"),
        ),
        Release(
            codename="hardy",
            version="8.04",
            name="Hardy Heron",
            development=False,
            lts=True,
            release_date=datetime.strptime("2008-04-24", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2008-04-24", "%Y-%m-%d"),
            support_expires=datetime.strptime("2008-04-24", "%Y-%m-%d"),
        ),
        Release(
            codename="intrepid",
            version="8.10",
            name="Intrepid Ibex",
            development=False,
            lts=False,
            release_date=datetime.strptime("2008-10-30", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2008-10-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2008-10-30", "%Y-%m-%d"),
        ),
        Release(
            codename="jaunty",
            version="9.04",
            name="Jaunty Jackalope",
            development=False,
            lts=False,
            release_date=datetime.strptime("2009-04-23", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2008-10-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2008-10-30", "%Y-%m-%d"),
        ),
        Release(
            codename="karmic",
            version="9.10",
            name="Karmic Koala",
            development=False,
            lts=False,
            release_date=datetime.strptime("2009-10-29", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2009-10-29", "%Y-%m-%d"),
            support_expires=datetime.strptime("2009-10-29", "%Y-%m-%d"),
        ),
        Release(
            codename="lucid",
            version="10.04",
            name="Lucid Lynx",
            development=False,
            lts=True,
            release_date=datetime.strptime("2010-04-29", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2010-04-29", "%Y-%m-%d"),
            support_expires=datetime.strptime("2010-04-29", "%Y-%m-%d"),
        ),
        Release(
            codename="maverick",
            version="10.10",
            name="Maverick Meerkat",
            development=False,
            lts=False,
            release_date=datetime.strptime("2010-10-10", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2010-10-10", "%Y-%m-%d"),
            support_expires=datetime.strptime("2010-10-10", "%Y-%m-%d"),
        ),
        Release(
            codename="natty",
            version="11.04",
            name="Natty Narwhal",
            development=False,
            lts=False,
            release_date=datetime.strptime("2011-04-28", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2011-04-28", "%Y-%m-%d"),
            support_expires=datetime.strptime("2011-04-28", "%Y-%m-%d"),
        ),
        Release(
            codename="oneiric",
            version="11.10",
            name="Oneiric Ocelot",
            development=False,
            lts=False,
            release_date=datetime.strptime("2011-10-13", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2011-10-13", "%Y-%m-%d"),
            support_expires=datetime.strptime("2011-10-13", "%Y-%m-%d"),
        ),
        Release(
            codename="precise",
            version="12.04",
            name="Precise Pangolin",
            development=False,
            lts=True,
            release_date=datetime.strptime("2012-04-26", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2019-04-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2012-04-26", "%Y-%m-%d"),
        ),
        Release(
            codename="quantal",
            version="12.10",
            name="Quantal Quetzal",
            development=False,
            lts=False,
            release_date=datetime.strptime("2012-10-18", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2012-10-18", "%Y-%m-%d"),
            support_expires=datetime.strptime("2012-10-18", "%Y-%m-%d"),
        ),
        Release(
            codename="raring",
            version="13.04",
            name="Raring Ringtail",
            development=False,
            lts=False,
            release_date=datetime.strptime("2013-04-25", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2013-04-25", "%Y-%m-%d"),
            support_expires=datetime.strptime("2013-04-25", "%Y-%m-%d"),
        ),
        Release(
            codename="saucy",
            version="13.10",
            name="Saucy Salamander",
            development=False,
            lts=False,
            release_date=datetime.strptime("2013-10-17", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2013-10-17", "%Y-%m-%d"),
            support_expires=datetime.strptime("2013-10-17", "%Y-%m-%d"),
        ),
        Release(
            codename="trusty",
            version="14.04",
            name="Trusty Tahr",
            development=False,
            lts=True,
            release_date=datetime.strptime("2014-04-17", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2022-04-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2019-04-30", "%Y-%m-%d"),
        ),
        Release(
            codename="utopic",
            version="14.10",
            name="Utopic Unicorn",
            development=False,
            lts=False,
            release_date=datetime.strptime("2014-10-23", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2014-10-23", "%Y-%m-%d"),
            support_expires=datetime.strptime("2014-10-23", "%Y-%m-%d"),
        ),
        Release(
            codename="vivid",
            version="15.04",
            name="Vivid Vervet",
            development=False,
            lts=False,
            release_date=datetime.strptime("2015-04-23", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2015-04-23", "%Y-%m-%d"),
            support_expires=datetime.strptime("2015-04-23", "%Y-%m-%d"),
        ),
        Release(
            codename="wily",
            version="15.10",
            name="Wily Werewolf",
            development=False,
            lts=False,
            release_date=datetime.strptime("2015-10-22", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2015-10-22", "%Y-%m-%d"),
            support_expires=datetime.strptime("2015-10-22", "%Y-%m-%d"),
        ),
        Release(
            codename="xenial",
            version="16.04",
            name="Xenial Xerus",
            development=False,
            lts=True,
            release_date=datetime.strptime("2016-04-21", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2024-04-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2021-04-30", "%Y-%m-%d"),
        ),
        Release(
            codename="yakkety",
            version="16.10",
            name="Yakkety Yak",
            development=False,
            lts=False,
            release_date=datetime.strptime("2016-10-13", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2016-10-13", "%Y-%m-%d"),
            support_expires=datetime.strptime("2016-10-13", "%Y-%m-%d"),
        ),
        Release(
            codename="zesty",
            version="17.04",
            name="Zesty Zapus",
            development=False,
            lts=False,
            release_date=datetime.strptime("2017-04-13", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2017-04-13", "%Y-%m-%d"),
            support_expires=datetime.strptime("2017-04-13", "%Y-%m-%d"),
        ),
        Release(
            codename="artful",
            version="17.10",
            name="Artful Aardvark",
            development=False,
            lts=False,
            release_date=datetime.strptime("2017-10-19", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2017-10-19", "%Y-%m-%d"),
            support_expires=datetime.strptime("2017-10-19", "%Y-%m-%d"),
        ),
        Release(
            codename="bionic",
            version="18.04",
            name="Bionic Beaver",
            development=False,
            lts=True,
            release_date=datetime.strptime("2018-04-26", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2028-04-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2023-04-30", "%Y-%m-%d"),
        ),
        Release(
            codename="cosmic",
            version="18.10",
            name="Cosmic Cuttlefish",
            development=False,
            lts=False,
            release_date=datetime.strptime("2018-10-18", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2018-10-18", "%Y-%m-%d"),
            support_expires=datetime.strptime("2018-10-18", "%Y-%m-%d"),
        ),
        Release(
            codename="disco",
            version="19.04",
            name="Disco Dingo",
            development=False,
            lts=False,
            release_date=datetime.strptime("2019-04-18", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2019-04-18", "%Y-%m-%d"),
            support_expires=datetime.strptime("2019-04-18", "%Y-%m-%d"),
        ),
        Release(
            codename="eoan",
            version="19.10",
            name="Eoan Ermine",
            development=False,
            lts=False,
            release_date=datetime.strptime("2019-10-17", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2020-07-31", "%Y-%m-%d"),
            support_expires=datetime.strptime("2019-10-17", "%Y-%m-%d"),
        ),
        Release(
            codename="focal",
            version="20.04",
            name="Focal Fossa",
            development=False,
            lts=True,
            release_date=datetime.strptime("2020-04-23", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2030-04-30", "%Y-%m-%d"),
            support_expires=datetime.strptime("2025-04-30", "%Y-%m-%d"),
        ),
        Release(
            codename="groovy",
            version="20.10",
            name="Groovy Gorilla",
            development=True,
            lts=False,
            release_date=datetime.strptime("2020-10-20", "%Y-%m-%d"),
            esm_expires=datetime.strptime("2021-07-31", "%Y-%m-%d"),
            support_expires=datetime.strptime("2021-07-31", "%Y-%m-%d"),
        ),
        Release(codename="upstream", name="Upstream"),
    ]

    for release in releases:
        exists = db_session.query(Release).get(release.codename)

        if not exists:
            db_session.add(release)

    db_session.commit()


if __name__ == "__main__":
    load_releases()
