class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_file_pair = {}

        for files in paths:
            contents = files.split()
            n = len(contents)
            if n <= 1:
                continue
            
            for i in range(1, n):
                file_, content = contents[i].split("(")
                if content not in content_file_pair:
                    content_file_pair[content] = []

                full_path = contents[0]+"/"+file_
                content_file_pair[content].append(full_path)
        
        res = []

        for files in content_file_pair.values():
            if len(files) > 1:
                res.append(files)

        return res
