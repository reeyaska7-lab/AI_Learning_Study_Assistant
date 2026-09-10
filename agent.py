from rag import SimpleRAG
from memory import ConversationMemory
from tools import create_study_plan, generate_quiz


class LearningAgent:

    def __init__(self):
        self.rag = SimpleRAG()
        self.memory = ConversationMemory()

    def load_document(self, text):
        self.rag.load(text)

    def handle(self, query):

        query_lower = query.lower()

        if "study plan" in query_lower:
            response = create_study_plan()

        elif "schedule" in query_lower:
            response = create_study_plan()

        elif "quiz" in query_lower:
            response = generate_quiz()

        elif "mcq" in query_lower:
            response = generate_quiz()

        elif "question" in query_lower:
            response = generate_quiz()

        else:

            results = self.rag.search(query)

            if results:

                response = (
                    "📚 **Answer from your study material:**\n\n"
                    + "\n\n".join(results)
                )

            elif self.memory.has_memory():

                response = (
                    "🧠 **From our previous conversation:**\n\n"
                    + self.memory.get_last_topic()
                )

            else:

                response = (
                    "I couldn't find relevant information.\n\n"
                    "Please upload your study material and "
                    "ask your question again."
                )

        self.memory.save(query)

        return response