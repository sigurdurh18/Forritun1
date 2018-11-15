def game_of_eights(user_list): 
    for i in range(len(user_list)):
        elem = user_list[i]
        if elem == 8 and i < len(user_list)-1 and user_list[i+1] == 8:
            return True 
    return False

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    try:
        a_list = [int(elements) for elements in a_list]
        result = game_of_eights(a_list)
        print(result)
    except ValueError: 
        print("Error. Please enter only integers.")

main()