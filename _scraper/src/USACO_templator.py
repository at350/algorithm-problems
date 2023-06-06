from pathlib import Path
from templator import *
from USACO_common import *


def get_file_io(io_file: str) -> str:
    if io_file == 'stdio' or io_file == 'interactive':
        return ''
    return f'freopen("{io_file}.in", "r", stdin);\n{" "*4}freopen("{io_file}.out", "w", stdout);\n'


class USACOTemplator(Templator):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)

    def generate_templates(self) -> None:
        for contest, contest_data in self.data.items():
            for division, division_data in contest_data.items():
                for problem, problem_data in division_data.items():
                    whole_title = problem_data['whole_title']

                    problem_path = Path(get_problem_path(contest, division))
                    if not problem_path.exists():
                        os.makedirs(problem_path)

                    with open(f'{problem_path}/{problem}.cpp', 'w') as f:
                        first_line, second_line = whole_title.split(' \n ')
                        f.write(f'// {first_line}\n')
                        f.write(f'// {second_line}\n')
                        f.write(f'// link: {problem_data["link"]}\n')
                        f.write('// status: unsolved \n')
                        f.write('// tag: \n')
                        f.write('\n')

                        with open(template_path, 'r') as template:
                            f.write(template.read().replace('"__IO_PLACEHOLDER__";\n', get_file_io(problem_data['io_file'])))

                    print(f'Generated template for, {first_line}, {second_line}')


if __name__ == '__main__':
    USACOTemplator(data_file).run()
