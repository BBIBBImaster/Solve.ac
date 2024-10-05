import sys

def find_max(customer_list) :
  customer_count = []
  customer_count.append(customer_list[0][1])
  
  for i in range(9) :
    customer_count.append(
      customer_count[i] + ( customer_list[i+1][1] - customer_list[i+1][0] )
    )
    
  return max(customer_count)

if __name__ == "__main__" :
  input = sys.stdin.readline
  customer_list = []

  for _ in range(10) :
    cin, cout = map(int, input().split())
    customer_list.append((cin, cout))

  print(find_max(customer_list))