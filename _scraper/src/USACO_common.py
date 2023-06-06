import os

host = 'http://www.usaco.org/'
name = 'USACO'

curr_path = (os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
data_file = os.path.join(root_path, f'data/{name}.json')
problems_root_path = os.path.join(root_path, f'../{name}')
template_path = os.path.join(problems_root_path, '_template.cpp')

divisions = ['Bronze', 'Silver', 'Gold', 'Platinum']

def get_problem_path(contest, division):
    return os.path.join(problems_root_path, f'{contest}/{division}')
