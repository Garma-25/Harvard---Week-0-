def main():
    user_input = input('Digite algum texto com emoticons :), :( : ')
    converted_text = user_input.replace(':)', '🙂').replace(':(', '🙁')
    print(converted_text)

if __name__ == "__main__":
    main()
