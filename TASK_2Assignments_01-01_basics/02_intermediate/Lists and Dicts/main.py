# def access_element(lst, index):
#     try:
#         return lst[index]
#     except IndexError:
#         return "Index out of range."

# def modify_element(lst, index, new_value):
#     try:
#         lst[index] = new_value
#         return lst
#     except IndexError:
#         return "Index out of range."

# def slice_list(lst, start, end):
#     try:
#         return lst[start:end]
#     except IndexError:
#         return "Invalid indices."

# def index_game():
#     lst = [1, 2, 3, 4, 5]  # Example list
#     print("Current list:", lst)
#     print("Choose an operation: access, modify, slice")
#     operation = input("Enter operation: ")

#     if operation == "access":
#         index = int(input("Enter index to access: "))
#         print(access_element(lst, index))
#     elif operation == "modify":
#         index = int(input("Enter index to modify: "))
#         new_value = input("Enter new value: ")
#         print(modify_element(lst, index, new_value))
#     elif operation == "slice":
#         start = int(input("Enter start index: "))
#         end = int(input("Enter end index: "))
#         print(slice_list(lst, start, end))
#     else:
#         print("Invalid operation.")

# index_game()









# Practice of List 

def main():
    fruit_lst = ["Apple", "Banana", "Orange", "Mango", "Watermelon", "Pineapple", "Grapes", "Papaya"]

    list_length = len(fruit_lst)
    print (fruit_lst)
    
    fruit_lst.append("Kiwi")

    for fruits in fruit_lst:
        print(fruits)

if __name__ == "__main__":
    main()
    







