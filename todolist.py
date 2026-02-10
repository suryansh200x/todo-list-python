tasks = []

def show_tasks():
    if not tasks:
        print("📭 Koi task nahi hai")
    else:
        print("\n📝 Aapke Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO DO LIST ---")
    print("1. Task Add karo")
    print("2. Task Dekho")
    print("3. Task Delete karo")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Task likho: ")
        tasks.append(task)
        print("✅ Task add ho gaya")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Delete karne ka task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("🗑️ Task delete ho gaya")
        else:
            print("❌ Galat number")

    elif choice == "4":
        print("👋 Bye!")
        break

    else:
        print("❌ Galat choice")
