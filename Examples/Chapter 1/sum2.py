# Input example

# input()->A function that accepts inout from the user. Takes an optional string argument

print("Type integers, each followed by Enter; or ^D or ^Z to finish")

total=0
count=0

while True: ##Use ctrl+D in PyCharm to finish, in console use ctrl+D
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("count=", count, "total= ", total, "mean =", total/count)
