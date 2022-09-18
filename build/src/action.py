import os


def do_action(args):
    print(args)
    print("list workspace files")
    for item in os.listdir("/github/workspace"):
        print(item)
    return {"example_output": "hello world"}
