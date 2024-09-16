import os
import subprocess
from rich import print
from rich.console import Console

def get_commits(git_folder_path):
    os.chdir(git_folder_path)
    command = ['git', 'log', '--pretty=format:%H']
    output = subprocess.check_output(command, text=True)
    commit_hashes = output.strip().split('\n')
    return commit_hashes
def format_hash(hash_value):
    formatted_hashes = [hash_value[i:i+6] for i in range(0, len(hash_value), 6)]
    return formatted_hashes
def colorize_hashes(formatted_hashes):
    console = Console()
    for full_hash in formatted_hashes:
        line = ""
        for hash_part in full_hash:
            if len(hash_part) == 6:
                line += f"[on #{hash_part}]{hash_part}[/]"
        console.print(line)
        
if __name__ == "__main__":
    git_folder_path = input('path> ')
    commit_hashes = get_commits(git_folder_path)
    formatted_hashes = [format_hash(h) for h in commit_hashes]
    colorize_hashes(formatted_hashes)