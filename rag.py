import re


class SimpleRAG:

    def __init__(self):
        self.chunks = []

    def load(self, text):

        self.chunks = re.split(
            r"(?<=[.!?])\s+",
            text
        )

        self.chunks = [
            chunk.strip()
            for chunk in self.chunks
            if chunk.strip()
        ]

    def search(self, query, top_k=3):

        if not self.chunks:
            return []

        query_words = set(
            re.findall(
                r"\b[a-zA-Z]+\b",
                query.lower()
            )
        )

        scored_chunks = []

        for chunk in self.chunks:

            words = set(
                re.findall(
                    r"\b[a-zA-Z]+\b",
                    chunk.lower()
                )
            )

            score = len(
                query_words.intersection(words)
            )

            if score > 0:
                scored_chunks.append(
                    (score, chunk)
                )

        scored_chunks.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            chunk
            for score, chunk
            in scored_chunks[:top_k]
        ]