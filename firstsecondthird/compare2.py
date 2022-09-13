x = int(input("What's x? "))
y = int(input("What's y? "))

#(elif) I'll only keep making these questions if one of them isn't true yet. The options are mutually exclusive
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: #instead of elif x==y:
    print("x is equal to y")