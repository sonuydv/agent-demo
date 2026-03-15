from db.sqlite_db import init_db


# Init sqlite db
init_db()


# Run after sqlite init
from agents.alex.agent import run_agent


# question = input("Ask agent: ")
# write_log("\n###################################\n"+"Agent Asked : "+question)

# response = run_agent(question)

# print("\nAgent Response: #####################")
# print(response)