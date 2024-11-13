print()
todo_list = []
while True:
  if len(todo_list) == 0:
    print("Your To-Do list is empty\n")

  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  print()
  print("Options: ")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit\n")

  choice = input()
  if choice == "1":
    print()
    new_task = input("Enter the task to add: ")
    todo_list.append(new_task)
    print("Task added.")

  elif choice == "2":
    list_length = len(todo_list)
    if list_length == 0:
      print("No task to remove")
    else:
      task_to_remove = input("Enter task no. to remove: ")
      remove_task_no = int(task_to_remove) - 1
      if remove_task_no <= list_length:
        todo_list.pop(remove_task_no) 
        print("Task removed.")

  
  elif choice == "3":
    print("Close program.")
    break