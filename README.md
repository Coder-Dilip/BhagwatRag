
### Bhagavad Gita Knowledge Graph RAG Project

### Overview
The Bhagavad Gita Knowledge Graph Retrieval-Augmented Generation (RAG) Project is a unique system allowing users to ask deep, thoughtful questions about the timeless wisdom from the Bhagavad Gita. This project utilizes a knowledge graph, enabling users to receive insightful answers based on Sanatan teachings.

### Features
- **Question-Answering System**: Users can ask profound questions, and the system provides answers using a knowledge graph based on the Bhagavad Gita.
- **Knowledge Graph Integration**: Leverages structured data to provide accurate, context-rich answers from the Bhagavad Gita.

### Getting Started

### Prerequisites
Make sure you have:
- Python > 3.9
- Required Python dependencies (refer to `requirements.txt`)

### Configuration
Before running the project, set up your API configurations.

1. Go to the `settings.yml` file in the `ragtest` directory.
2. Enter your API configurations, including any keys and endpoint details.

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

To ask questions to the knowledge graph:

1. Ensure your configurations are set in `settings.yml`.
2. Run the `ask_graph.py` file:
   ```bash
   python ask_graph.py
   ```

3. You’ll be prompted to input your question, and the system will provide answers based on Sanatan wisdom from the Bhagavad Gita.

## Usage

After starting the project, type in any question about the Bhagavad Gita’s teachings. The system processes your question, retrieves relevant insights from the knowledge graph, and responds with a meaningful answer.

Example question:
```
Who am i?
```

## Contributing
Contributions to enhance this project are welcome. Please submit pull requests with a description of the changes you’ve made.
