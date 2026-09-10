class ConversationMemory:

    def __init__(self):
        self.history = []

    def save(self, query):
        self.history.append(query)

    def has_memory(self):
        return len(self.history) > 0

    def get_last_topic(self):

        if not self.history:
            return "No previous topic available."

        return self.history[-1]

    def get_recent(self, count=5):

        return self.history[-count:]