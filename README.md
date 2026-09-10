# AI Learning & Study Assistant

## Project Overview

The **AI Learning & Study Assistant** is an Agentic AI-based application designed to help students with learning, revision, and study planning.

The system works as an intelligent study companion that can understand a student's request and select the appropriate learning task. It can use study materials, conversation memory, and learning-related tools to provide useful academic assistance.

## Problem Statement

Students often spend a lot of time searching through study notes, understanding difficult concepts, preparing study schedules, and creating practice questions.

The proposed system brings these learning activities together in a single AI-powered assistant that can provide more organized and personalized academic support.

## Objectives

* Develop an AI-based personal learning assistant.
* Answer questions using relevant study materials.
* Retrieve relevant information using RAG.
* Generate personalized study plans.
* Generate quizzes and practice questions.
* Maintain useful conversation context using memory.
* Demonstrate practical use of Agentic AI in education.

## Key Features

* Study-material based question answering
* Retrieval-Augmented Generation (RAG)
* Study-plan generation
* Quiz and practice-question generation
* Explanation of difficult concepts
* Conversation memory
* Agent-based task selection
* Interactive student-friendly interface

## Technologies Used

* Python
* Streamlit
* Agentic AI
* Retrieval-Augmented Generation (RAG)
* Memory
* VS Code
* GitHub

## Project Structure

```text
AI_Learning_Study_Assistant/
│
├── app.py
├── agent.py
├── rag.py
├── memory.py
├── tools.py
├── requirements.txt
│
└── data/
    └── python_notes.txt
```

## File Description

### app.py

Main application file that provides the user interface and runs the application.

### agent.py

Contains the agent logic used to understand student requests and determine the appropriate task.

### rag.py

Handles retrieval of relevant information from the available study material.

### memory.py

Maintains useful conversation context between interactions.

### tools.py

Contains learning-related helper functions and task capabilities.

### requirements.txt

Contains the Python packages required to run the project.

### data/python_notes.txt

Contains sample study material used as a knowledge source.

## How to Run

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## Example Tasks

The assistant can support requests such as:

```text
Explain a topic from my study material.
```

```text
Create a study plan for my subjects.
```

```text
Generate MCQs from this topic.
```

## Future Enhancements

* Voice-based interaction
* Student progress tracking
* Personalized learning recommendations
* Tamil-English and multilingual support
* Mobile application
* Teacher portal
* Smart study reminders
* Adaptive learning based on student performance

## Project Author

**Reeyaska.S**
B.Tech – Information Technology
Theni Kammavar Sangam College of Technology
Academic Year 2026

## Internship

**TNSDC – IBM Agentic AI Internship**
