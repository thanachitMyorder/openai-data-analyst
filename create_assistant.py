from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


instructions = """You are an assistant running data analysis on CSV files.

You will use code interpreter to run the analysis.

However, instead of rendering the charts as images, you will generate a plotly figure and turn it into json.
You will create a file for each json that I can download through annotations.

You are also an expert Data Engineer at MyOrder company, You know everything about data engineering.

You are also a good communicator and can explain your work to a non-technical person.

You know that we use data tools mainly on GCP to create Data pipeline such as Pubsub, BigQuery, Google cloud storage, Dataflow, Looker studio and more.
"""

tools = [
    {"type": "code_interpreter"},
    {"type": "file_search"}
]

file = openai_client.files.create(
  file=open("tesla-stock-price.csv", "rb"),
  purpose='assistants'
)


assistant = openai_client.beta.assistants.create(
    model="gpt-4o-mini",
    name="Data Analysis Assistant",
    instructions=instructions,
    temperature=0.1,
    tools=tools,
    tool_resources={
        "code_interpreter": {
        "file_ids": [file.id]
        }
    }
)

print(f"Assistant created with id: {assistant.id}")