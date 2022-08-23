

def get_food_params(name):
    return food_params[name]


food_params = {
    "2a2f_p": {
        "n_agents": 2,
        "n_foods": 2,
        "initial_stock": [5, 5],
        "requests": [
            [2, 3],
            [3, 2],
        ],
    },
    "2a2f_c1": {
        "n_agents": 2,
        "n_foods": 2,
        "initial_stock": [5, 5],
        "requests": [
            [3, 10],
            [3, 10],
        ],
    },
    "2a2f_c2": {
        "n_agents": 2,
        "n_foods": 2,
        "initial_stock": [10, 5],
        "requests": [
            [7, 2],
            [5, 5],
        ],
    },
    "2a2f_c3": {
        "n_agents": 2,
        "n_foods": 2,
        "initial_stock": [5, 5],
        "requests": [
            [3, 5],
            [5, 3],
        ],
    },
    "2a3f_p": {
        "n_agents": 2,
        "n_foods": 3,
        "initial_stock": [10, 10, 10],
        "requests": [
            [5, 3, 9],
            [5, 7, 1],
        ],
    },
    "2a3f_p2": {
        "n_agents": 2,
        "n_foods": 3,
        "initial_stock": [4, 4, 4],
        "requests": [
            [2, 2, 2],
            [2, 2, 2],
        ],
    },
    "2a3f_c1": {
        "n_agents": 2,
        "n_foods": 3,
        "initial_stock": [10, 10, 10],
        "requests": [
            [6, 8, 10],
            [6, 8, 10],
        ],
    },
    "3a2f_p1": {
        "n_agents": 3,
        "n_foods": 2,
        "initial_stock": [6, 6],
        "requests": [
            [2, 2],
            [2, 2],
            [2, 2],
        ],
    },
    "3a3f_p1": {
        "n_agents": 3,
        "n_foods": 3,
        "initial_stock": [6, 6, 6],
        "requests": [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2],
        ],
    },
    "3a3f_c1": {
        "n_agents": 3,
        "n_foods": 3,
        "initial_stock": [4, 4, 4],
        "requests": [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2],
        ],
    },
    "3a3f_c2": {
        "n_agents": 3,
        "n_foods": 3,
        "initial_stock": [10, 10, 10],
        "requests": [
            [10, 10, 1],
            [4, 5, 4],
            [2, 6, 8],
        ],
    },
    "3a3f_c3": {
        "n_agents": 3,
        "n_foods": 3,
        "initial_stock": [10, 10, 10],
        "requests": [
            [10, 10, 0],
            [10, 5, 4],
            [10, 6, 8],
        ],
    },
    "3a3f_c4": {
        "n_agents": 3,
        "n_foods": 3,
        "initial_stock": [3, 3, 3],
        "requests": [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2],
        ],
    },
    "4a4f_p1": {
        "n_agents": 4,
        "n_foods": 4,
        "initial_stock": [8, 8, 8, 8],
        "requests": [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
        ],
    },
    "5a5f_p1": {
        "n_agents": 5,
        "n_foods": 5,
        "initial_stock": [10, 10, 10, 10, 10],
        "requests": [
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
        ],
    },
    "5a5f_c1": {
        "n_agents": 5,
        "n_foods": 5,
        "initial_stock": [5, 5, 5, 5, 5],
        "requests": [
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
        ],
    },
    "5a5f_c2": {
        "n_agents": 5,
        "n_foods": 5,
        "initial_stock": [5, 5, 5, 5, 5],
        "requests": [
            [5, 1, 1, 1, 1],
            [1, 5, 1, 1, 1],
            [1, 1, 5, 1, 1],
            [1, 1, 1, 5, 1],
            [1, 1, 1, 1, 5],
        ],
    },
    "10a10f_c1": {
        "n_agents": 10,
        "n_foods": 10,
        "initial_stock": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "requests": [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ],
    },
    "10a10f_c2": {
        "n_agents": 10,
        "n_foods": 10,
        "initial_stock": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "requests": [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ],
    },
}
