from handlers.session import sign_in
from handlers.layer import n_layer_data_extraction

if __name__ == '__main__':
    session = sign_in()
    # TODO:  Take Center User's username and password from terminal !!!!
    # 488 -> 52sn

    initial_username = input("username: ")
    username = initial_username
    layer_count = int(input("Layer count: "))
    n_layer_data_extraction(username, initial_username, session, layer_count)



