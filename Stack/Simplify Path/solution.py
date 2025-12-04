class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split('/'):
            match directory:
                case '' | '.':
                    pass
                case '..':
                    if stack: stack.pop()
                case _:
                    stack.append(directory)
            
        return "/" + "/".join(stack)