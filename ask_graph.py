import subprocess
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'

def run_graphrag_query(root_dir, method, query):
    try:
        result = subprocess.run(
            [
                "graphrag", "query",
                "--root", root_dir,
                "--method", method,
                "--query", query
            ],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

# Parameters for the query
root_directory = "./ragtest"
method_type = "global"
thoughtful_question=input("Enter your query: ")

# Run the graph rag function
geeta_answer_from_KG=run_graphrag_query(root_directory, method_type, thoughtful_question)
print("Knowledge graph answer:", geeta_answer_from_KG)