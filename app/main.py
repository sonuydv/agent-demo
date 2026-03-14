from agent import run_agent
from tools import write_log


question = input("Ask agent: ")
# write_log("\n###################################\n"+"Agent Asked : "+question)

response = run_agent(question)

print("\nAgent Response: #####################")
print(response)