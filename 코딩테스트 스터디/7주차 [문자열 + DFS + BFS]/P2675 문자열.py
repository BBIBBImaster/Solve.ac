import sys

def repeat_string(t, inputs):
    results = []
    for i in range(t):
        r, s = inputs[i].split() 
        r = int(r)
        repeated_string = ''
        for j in range(len(s)):
            repeated_string += s[j] * r
        results.append(repeated_string)
    return results

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input().strip())
    inputs = [input().strip() for _ in range(t)]
    output_results = repeat_string(t, inputs)
  
    for result in output_results:
        print(result)
