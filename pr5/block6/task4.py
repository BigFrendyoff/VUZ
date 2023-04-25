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

game_extension = {
    'room6': dict(
        down=go('room7'),
        left=go('room8')
    ),
    'room7': dict(
        up=go('room6'),
        down=go('room8')
    ),
    'room8': dict(
        up=go('room7'),
        diag_up=go('room6'),
        down=go('room9'),
    ),
    'room9': dict(
        down=go('room10'),
        right=go('room11'),
    ),
    'room10': dict(
    ),
    'room11': dict(
        up=go('room8'),
        left=go('room9'),
        down=go('room10')
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
    goal_states = ['room2', 'room10']

    return state['room'] in goal_states


def get_current_room(state):
    '''
    Выдать комнату, в которой находится игрок.
    '''
    return state['room']


def find_dead_ends():
    dead_ends = []

    def dfs(state, visited):
        if (is_goal_state(state)):
            return True
        visited.append(get_current_room(state))
        for key in game[get_current_room(state)].keys():
            if get_current_room(game[get_current_room(state)][key](state)) not in visited:
                if dfs(game[get_current_room(state)][key](state), visited):
                    return True

        return False

    for key in game.keys():
        if not dfs(dict(room=key), visited=[]):
            dead_ends.append(key)
    return dead_ends


def make_model(game, start):
    used_nodes = []
    dead_ends = find_dead_ends()
    graph = graphviz.Digraph()
    state = start
    for key_1 in game.keys():
        if key_1 == start['room']:
            graph.node(f'n{key_1[4:]}', style="filled", fillcolor="dodgerblue", shape="circle")
        elif key_1 in dead_ends:
            graph.node(f'n{key_1[4:]}', style="filled", fillcolor="red", shape="circle")
        elif is_goal_state(dict(room=key_1)):
            graph.node(f'n{key_1[4:]}', style="filled", fillcolor="green", shape="circle")
        else:
            graph.node(f'n{key_1[4:]}', style="filled", fillcolor="white", shape="circle")
        used_nodes.append(key_1)
        for key_2 in game[key_1].keys():
            state = game[key_1][key_2](state)
            node = get_current_room(state)
            if node not in used_nodes:
                if node in dead_ends:
                    graph.node(f'n{node[4:]}', style="filled", fillcolor="red", shape="circle")
                elif is_goal_state(dict(room=node)):
                    graph.node(f'n{node[4:]}', style="filled", fillcolor="green", shape="circle")
                else:
                    graph.node(f'n{node[4:]}', style="filled", fillcolor="white", shape="circle")
                used_nodes.append(node)
            graph.edge(f'n{key_1[4:]}', f'n{node[4:]}')

    graph.render('game2', format='png')


state = START_STATE
state = game[get_current_room(state)]['right'](state)
state = game[get_current_room(state)]['right'](state)
if get_current_room(state) == 'room5':
    game = game | game_extension
    add_path('room5', 'room6')

make_model(game, START_STATE)

# help(graphviz.Digraph.node)
