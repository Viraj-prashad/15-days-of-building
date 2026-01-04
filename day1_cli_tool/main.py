def greet(name):
    return f"Hello, {name}. How are you today?"

def main():
    print("### Welcome to the Greeting Program ###")
    
    name = input("Please enter your name: ").strip()

    if not name:
        print("It seems you didn't enter a name. Please try again.")
        return
    
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()