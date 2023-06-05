import os

host = 'http://www.usaco.org/'

curr_path = os.getcwd()
data_file = os.path.join(curr_path, 'data/usaco.json')
problems_root_path = os.path.join(curr_path, '../USACO')
template_path = os.path.join(problems_root_path, '_template.cpp')


def get_problem_path(contest, division):
    return os.path.join(problems_root_path, f'{contest}/{division}')
