class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for string in strs:
            encoded_list.append(f"{len(string)}#{string}")
        encoded_str = "".join(encoded_list)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        decoded_list = []

        while i < n:
            hash_idx = s.index("#", i, n)
            word_length = int(s[i:hash_idx])
            start = hash_idx + 1
            stop = start + word_length
            word = s[start : stop]

            decoded_list.append(word)
            i = stop
        
        return decoded_list