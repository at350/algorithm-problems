from markdown_generator import *
from USACO_common import *


class USACOStat(MarkDownGenerator):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)
        self.stat = {division: default_stat for division in divisions}
        self.total = {division: 0 for division in divisions}

    def generate_division_statistics(self, division: str) -> str:
        return f'#### {division} Solved {self.stat[division]["AC"]}/{self.total[division]}\n'

    def generate_statistics(self) -> None:
        md_text = ""

        for contest, contest_data in self.data.items():
            md_text += f'# {contest}\n\n'
            md_text += '| Problem | Problem Title | Problem Link | Code | Status |\n'
            md_text += '|---------|---------------|--------------|------|--------|\n'
            for division, division_data in contest_data.items():
                for problem, problem_data in division_data.items():
                    with open(f'{get_problem_path(contest, division)}/{problem}.cpp', 'r') as f:
                        for line in f:
                            if line.startswith('// status:'):
                                status = line.split('// status:')[1].strip()
                                code_file = f'{contest}/{division}/{problem}.cpp'
                                md_text += f'| {division} {problem} | {problem_data["title"]} | [Link]({problem_data["link"]}) | [{code_file}]({code_file}) | {status} |\n'
                                self.stat[division][status] += 1
                                self.total[division] += 1

            md_text += '\n'

        with open(f'{problems_root_path}/README.md', 'w') as f:
            f.write('# USACO\n' +
                    ''.join(self.generate_division_statistics(division) for division in divisions) +
                    md_text)


if __name__ == '__main__':
    USACOStat(data_file).run()
