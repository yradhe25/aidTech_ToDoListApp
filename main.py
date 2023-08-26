print("Welcome to the TODO app")
tasks=[]

try:
   with open("tasks.txt","r") as file:
      tasks=[line.strip() for line in file]
except FileNotFoundError:
    print("Task file not found. Creating a new task file.")
    with open("tasks.txt", "w") as file:
       pass

while(True):
   operation=input("What do you want to do?\n1. add a task\n2. remove a task\n3. view all tasks\n4. save tasks\nEnter your choice or -1 to quit : ")
   if operation=="1":
      add_task1=input("Enter the task : ")
      add_task=add_task1.lower()
      if add_task in tasks:
         print("Task ia already added!")
         break
      else:
         tasks.append(add_task)
         print("Task added successfully!")

   elif operation=="2":
      remove_task1=input("Which task do you want to remove? : ")
      remove_task=remove_task1.lower()
      if remove_task in tasks:
         tasks.remove(remove_task)
         print("Task removed successfully!")
      else:
         print("There is no such task!")

   elif operation=="3":
      for index,task in enumerate(tasks,1):
         print(f"{index}. {task}")

   elif operation == "4":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
            print("Tasks saved successfully!")

   elif operation=="-1":
      break

   else:
      while not(operation=="1" or operation=="2" or operation=="3"):
         print("Enter a valid choice!")
         break