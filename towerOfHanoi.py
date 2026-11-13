def hanoi_solver(number):
  string = ""
  rod_1 = list(range(number, 0, -1))
  rod_2 = []
  rod_3 = []

  def log_state():
    nonlocal string
    string += f"{rod_1} {rod_2} {rod_3}\n"

  def move(n, start, help, end):
    if n == 0:
      return
    # 1. Move n-1 disks from start to help
    move(n - 1, start, end, help)
    # 2. Move the nth disk from start to end
    end.append(start.pop())
    log_state()
    # 3. Move n-1 disks from help to end
    move(n - 1, help, start, end)

  log_state()
  move(number, rod_1, rod_2, rod_3)
  return string.strip("\n")

test = 3
print(hanoi_solver(test))

test_2 = 2
print(hanoi_solver(test_2))

test_3 = 5
print(hanoi_solver(test_3))
