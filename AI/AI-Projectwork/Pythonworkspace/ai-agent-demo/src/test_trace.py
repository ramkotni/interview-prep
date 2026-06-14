from langsmith import traceable

@traceable
def hello():
    return "trace test"

print(hello())