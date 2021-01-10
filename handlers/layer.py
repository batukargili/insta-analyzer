from handlers.followers import get_user_followers, get_following_data
from utils.log import init_logger

logger = init_logger(__name__, testing_mode=False)


def n_layer_data_extraction(username, initial_username, session, layer_count):
    username = username
    following = []
    for layer in range(layer_count):
        if username == initial_username:
            logger.warning("Users Following list extracting from instagram")
            following = get_user_followers(session, username)
            get_following_data(username, following)

        else:
            logger.warning("Second Layer Following list extracting from instagram")
            for fl in following:
                following_second_layer = get_user_followers(session, fl)
                get_following_data(fl, following_second_layer)

        username = ""
