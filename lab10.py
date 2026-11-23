# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    # Restate: The problem is evaluate a post fix math expression where operands come before operators
    # Example: ["4", "13", "5", "/", "+"] -> pushes 4,13,5 -> pop 5&3, computes int(13/5)=2, pushes 2 -> pops 2&4, computes 2+4=6
    # Approach: Use a stack to stoer numbers. When hitting an operator pop the top two operandsand apply the operation, push the result back.
    # Return the sole remaining value.
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    operators = {"+","-","*","/"}
    for token in tokens:
        if token in operators:
            b=stack.pop()
            a=stack.pop()
            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "*":
                 stack.append(a*b)
            elif token == "/":
                stack.append(int(a/b))
        else:
            stack.append(int(token))
    return stack[0]

def decode_string(s):
    # Outline:
    #   ...
    # Restate: Expand the patterns of k[encoded] where brackets can contain nested patterns.
    # Example: 3[a2[c]] makes it so at the first '[' saves ("",3) at next '[' it saves ("a",2), at first']' it pops (2,"a") = "a" + 2*"c" = 
    # "acc" at last ']' it pops("",3) = "" + 3*"acc" = "accaccacc"
    # Approach: Track current_str and current_num. On '[' push both to a stakc and reset them. On ']' pop (prev_str,repeat_count) and update 
    # current_str = prev_str + current_str * repeat_count
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_str = ""
    current_num = 0
    for ch in s:
        if ch.isdigit():
            current_num = current_num *10 + int(ch)
        elif ch == "[":
            stack.append((current_str,current_num))
            current_str = ""
            current_num = 0
        elif ch == "]":
            prev_str,repeat_count = stack.pop()
            current_str = prev_str + current_str * repeat_count
        else:
            current_str += ch
    return current_str

def daily_temperatures(temps):
    # Outline:
    #   ...
    # Restate: For each i in indek, find the distance j-i to the next index j>1 where temps[j] >temps[i].
    # Example: [73, 74, 75, 71, 69, 72, 76, 73], 74 solves 73(1 day), 75 resolves 74 (1 day); 71 and 69 wait until 72 and 75 waits until 76(4 days)
    # Approach: Maintain a monotonic decreasing stackof indices whose warmer day hasn't been found yet. Whent he warmer temperatuer arrives, at index i pop all the 
    # colder indicesprev_i from the stackand do i - prev_iin the array.
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    result = [0] *len(temps)
    stack = []
    for i,temp in enumerate(temps):
        while stack  and temp > temps[stack[-1]]:
            prev_i = stack.pop()
            result[prev_i] = i = prev_i
            stack.append(i)
    return result



def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # Restate: Count connected components of 1 in a 2-D grid
    # Example: ["11000","11000","00100","00011"]  -> top-left 2x2 block(1), center single cell,  bottom-right 1x2 block(3) = 3
    # Approach: Iterate through every cell. When an unvisited 1 in encountered, increment island count and run BFS all connected as visited so they aren't counted again.
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                visited.add((r, c))
                stack = [(r, c)]  # Regular list instead of deque
                while stack:
                    curr_r, curr_c = stack.pop()  # Pop from the end
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            grid[nr][nc] == "1" and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            stack.append((nr, nc))
    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"])) 
    print(eval_rpn(["2", "1", "+", "3", "*"]))      
    print(decode_string("3[a2[c]]"))                    
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  
    print(num_islands(["11000", "11000", "00100", "00011"]))


if __name__ == "__main__":
    main()
