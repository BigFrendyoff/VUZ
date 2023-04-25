import graphviz


# Функция перехода из комнаты в комнату
def go(room):
    def func(state):
        return dict(state, room=room)

    return func


# Структура игры. Комнаты и допустимые в них действия
game = {
    'room0': dict(
        left=go('room1'),
        up=go('room2'),
        right=go('room3')
    ),
    'room1': dict(
        up=go('room2'),
        right=go('room0')
    ),
    'room2': dict(
    ),
    'room3': dict(
        up=go('room4'),
        right=go('room5'),
    ),
    'room4': dict(
        down=go('room3'),
        right=go('room5')
    ),
    'room5': dict(
        up=go('room4'),
        left=go('room3')
    )
}


def add_path(from_node, where_node):
    direction = ""
    for key in game[where_node]:
        node = game[where_node][key](dict(room=where_node))
        if key != node:
            if get_current_room(node) == from_node:
                if key == "left":
                    direction = "right"
                elif key == "right":
                    direction = "left"
                elif key == "up":
                    direction = "down"
                elif key == "down":
                    direction = "up"
    if direction != "":
        game[from_node][direction] = go(where_node)
    else:
        game[from_node]['diag'] = go(where_node)


# Стартовое состояние
START_STATE = dict(room='room0')


def is_goal_state(state):
    '''
    Проверить, является ли состояние целевым.
    '''
    return state['room'] == 'room2'


def get_current_room(state):
    '''
    Выдать комнату, в которой находится игрок.
    '''
    return state['room']


def make_model(game, start):
    used_nodes = []
    graph = graphviz.Digraph()
    state = start
    for key_1 in game.keys():
        graph.node(key_1)
        used_nodes.append(key_1)
        for key_2 in game[key_1].keys():
            if key_2 != "action":
                state = game[key_1][key_2](state)
                node = get_current_room(state)
                if node not in used_nodes:
                    graph.node(node)
                    used_nodes.append(node)
                graph.edge(key_1, node)

    graph.render('game', format='png')


def find_dead_ends():
    dead_ends = []

    def dfs(state, visited):
        if (is_goal_state(state)):
            return True
        visited.append(get_current_room(state))
        for key in game[get_current_room(state)].keys():
            if key != "action":
                if get_current_room(game[get_current_room(state)][key](state)) not in visited:
                    if dfs(game[get_current_room(state)][key](state), visited):
                        return True

        return False

    for key in game.keys():
        if not dfs(dict(room=key), visited=[]):
            dead_ends.append(key)
    return dead_ends


state = game[get_current_room(START_STATE)]['right'](START_STATE)
if get_current_room(state) == 'room3':
    add_path("room3", "room0")

make_model(game, START_STATE)


print(find_dead_ends())
