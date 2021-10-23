def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)


def TaylorE(x, n):
  output = 1 + x
  for i in range(2,n+1):
    output += (1/factorial(i))*(x**2)
  return output


def main():
  print(
    TaylorE(1,10)
  )


if __name__ == '__main__':
  main()