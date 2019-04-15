"""
This template is written by @timgrossmann

What does this quickstart script aim to do?
- This script is automatically executed every 6h on my server via cron
"""

import random
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = '@leothelion_aus'
insta_password = '2g~@gJBind)gTTjH>M:]'

dont_likes = ['sex', 'nude', 'naked', 'sausage', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              ]

friends = ['list of friends I do not want to interact with']

like_tag_list = ['shihtzu', 'shihtzusgram', 'dogsofinstagram', 'dogstagram', 'shihtzuofinstagram', 'shihtzupuppies', 'shihtzusociety',
                 'shihtzugram', 'doggo', 'pupper', '#dogsofinstaworld', 'doggos', 'littleshihtzu', 'fluffypuppy',
                 'shihtzus', 'shihtzulovers', 'shihtzulife', 'shihtzumania', 'shihtzulove', 'doglovers', 'dogloversclub', 'doglover']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['cat', 'kitten']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=3000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)

    session.unfollow_users(amount=random.randint(75, 150),
                           InstapyFollowed=(True, "all"), style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)
