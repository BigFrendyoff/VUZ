import random

import graphviz

game = {}

# START_STATE = dict(
#     player='alice',
#     alice_room='west room',
#     bob_room='east room',
#     red_key='east room',
#     blue_key='west room',
#     green_key='east room',
#     goal=False
# )

# START_STATE = dict(
#     player='alice',
#     alice_room='west room',
#     bob_room='west room',
#     red_key='east room',
#     blue_key='west room',
#     green_key='east room',
#     goal=False
# )

# START_STATE = dict(
#     player='alice',
#     alice_room='west room',
#     bob_room='east room',
#     red_key='east room',
#     blue_key='west room',
#     green_key='west room',
#     goal=False
# )
start_room = ['west room', 'east room']

START_STATE = dict(
    player='alice',
    alice_room=start_room[random.randint(0, 1)],
    bob_room=start_room[random.randint(0, 1)],
    red_key=start_room[random.randint(0, 1)],
    blue_key=start_room[random.randint(0, 1)],
    green_key=start_room[random.randint(0, 1)],
    goal=False
)
used_states = [START_STATE]
used_names = [0]


def variator(state, graph, n=0):
    global used_states
    global used_names
    player = {'alice': 'bob',
              'bob': 'alice'}
    player_room = {'alice': 'alice_room',
                   'bob': 'bob_room'}
    current_n = n
    extension = {}
    result = {}
    if state['alice_room'] == state['bob_room']:
        if state['red_key'] == state['player']:
            state_copy = state.copy()
            state_copy['red_key'] = player[state['player']]
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['green_key'] == state['player']:
            state_copy = state.copy()
            state_copy['green_key'] = player[state['player']]
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['blue_key'] == state['player']:
            state_copy = state.copy()
            state_copy['blue_key'] = player[state['player']]
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
    if state[player_room[state['player']]] == 'west room':
        if state['red_key'] == 'west room':
            state_copy = state.copy()
            state_copy['red_key'] = state['player']
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['blue_key'] == 'west room':
            state_copy = state.copy()
            state_copy['blue_key'] = state['player']
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['green_key'] == 'west room':
            state_copy = state.copy()
            state_copy['green_key'] = state['player']
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['red_key'] == state['player']:
            state_copy = state.copy()
            state_copy[player_room[state['player']]] = 'red room'
            if state_copy['bob_room'] == 'blue room' and state_copy['alice_room'] == 'red room':
                state_copy['goal'] = True
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['green_key'] == state['player']:
            state_copy = state.copy()
            state_copy[player_room[state['player']]] = 'east room'
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
    if state[player_room[state['player']]] == 'east room':
        if state['red_key'] == 'east room':
            state_copy = state.copy()
            state_copy['red_key'] = state['player']
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['blue_key'] == 'east room':
            state_copy = state.copy()
            state_copy['blue_key'] = state['player']
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['green_key'] == 'east room':
            state_copy = state.copy()
            state_copy['green_key'] = state['player']
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['blue_key'] == state['player']:
            state_copy = state.copy()
            state_copy[player_room[state['player']]] = 'blue room'
            if state_copy['bob_room'] == 'blue room' and state_copy['alice_room'] == 'red room':
                state_copy['goal'] = True
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
        if state['green_key'] == state['player']:
            state_copy = state.copy()
            state_copy[player_room[state['player']]] = 'west room'
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
    if state[player_room[state['player']]] == 'blue room':
        if state['blue_key'] == 'alice' and state['player'] == 'alice':
            state_copy = state.copy()
            state_copy['alice_room'] = 'east room'
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy
    if state[player_room[state['player']]] == 'red room':
        if state['red_key'] == 'bob' and state['player'] == 'bob':
            state_copy = state.copy()
            state_copy['bob_room'] = 'west room'
            if state_copy not in used_states:
                n = used_names[-1] + 1
                extension[n] = state_copy
                used_names.append(n)
                used_states.append(state_copy)
            elif state_copy != state:
                extension[used_names[used_states.index(state_copy)]] = state_copy

    if state not in used_states:
        n = used_names[-1] + 1
        extension[n] = state
        used_names.append(n)
        used_states.append(state)
    elif current_n != 0:
        extension[used_names[used_states.index(state)]] = state

    graph[current_n] = extension

    for key in extension:
        if key not in list(graph.keys()):
            state_copy = extension[key].copy()
            state_copy['player'] = player[state['player']]
            graph = graph | variator(state_copy, graph, key)

    return graph


def find_goal_states(graph):
    goal_states = []
    for key_1 in graph.keys():
        for key_2 in graph[key_1].keys():
            if graph[key_1][key_2]['goal']:
                if key_2 not in goal_states:
                    goal_states.append(key_2)
    return goal_states


def find_dead_ends(graph, goal_states):
    dead_ends = []

    def dfs(state, visited):
        if state in goal_states:
            return True
        visited.append(state)
        for key in graph[state].keys():
            if key not in visited:
                if dfs(key, visited):
                    return True
        return False

    for key in graph.keys():
        if not dfs(key, visited=[]):
            dead_ends.append(key)
    return dead_ends


def make_model(game, start, goal_states, dead_ends):
    used_nodes = []
    graph = graphviz.Digraph()
    for key_1 in game.keys():
        if key_1 == start:
            graph.node(f'n{key_1}', style="filled", fillcolor="dodgerblue", shape="circle")
        elif key_1 in dead_ends:
            graph.node(f'n{key_1}', style="filled", fillcolor="red", shape="circle")
        elif key_1 in goal_states:
            graph.node(f'n{key_1}', style="filled", fillcolor="green", shape="circle")
        else:
            graph.node(f'n{key_1}', style="filled", fillcolor="white", shape="circle")
        used_nodes.append(key_1)
        for key_2 in game[key_1].keys():
            node = key_2
            if node not in used_nodes:
                if node in dead_ends:
                    graph.node(f'n{node}', style="filled", fillcolor="red", shape="circle")
                elif node in goal_states:
                    graph.node(f'n{node}', style="filled", fillcolor="green", shape="circle")
                else:
                    graph.node(f'n{node}', style="filled", fillcolor="white", shape="circle")
                used_nodes.append(node)
            graph.edge(f'n{key_1}', f'n{node}')

    graph.render('tttm_2_random', format='png')


print(START_STATE)

result = variator(START_STATE, game)
print(sorted(list(result.keys())))
print(len(list(result.keys())))
goal_states = find_goal_states(result)
print(goal_states)
dead_ends = find_dead_ends(result, goal_states)
make_model(result, 0, goal_states, dead_ends)
