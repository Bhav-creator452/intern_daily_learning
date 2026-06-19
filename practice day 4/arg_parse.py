import argparse
parser=argparse.ArgumentParser(
    prog="Argument parsing",
    description="building CLI in python using argparse",
    epilog="Text at the bottom"
)

#positional arguments
# parser.add_argument("Number1" , help="First Number")
# parser.add_argument("Number2" , help="Second Number")
# parser.add_argument("Operation", help="Operations to be performed", choices=["add","subtract","Multiply"])

# args=parser.parse_args()

# print(args.Number1)
# print(args.Number2)
# print(args.Operation)

# n1=int(args.Number1)
# n2=int(args.Number2)
# result=None
# if args.Operation=="add":
#     result=n1+n2
# elif args.Operation=="subtract":
#     result=n1-n2
# elif args.operation=="multiply":
#     result=n1*n2
# print(result)

#optional arguments in argparse are passed using --argument_name
#-- specifies that it is an optional argument , it won't affect the program if skipped 

parser.add_argument("--Number1" , help="First Number")
parser.add_argument("--Number2" , help="Second Number")
parser.add_argument("--Operation", help="Operations to be performed", 
                    choices=["add","subtract","Multiply"])
args=parser.parse_args()

print(args.Number1)
print(args.Number2)
print(args.Operation)

n1=int(args.Number1)
n2=int(args.Number2)
result=None
if args.Operation=="add":
    result=n1+n2
elif args.Operation=="subtract":
    result=n1-n2
elif args.operation=="multiply":
    result=n1*n2
else:
    print("unsupported operation")

print(result)