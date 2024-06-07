from typing import List


class ReplaceWords:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        sorted_root = sorted(dictionary, key=lambda x: (len(x), x))

        for i, word in enumerate(words):
            for root in sorted_root:
                if word.startswith(root):
                    words[i] = root
                    break

        return ' '.join(words)

