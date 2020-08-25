import lexer

while True:
    output = input('command >> ')
    result, error = lexer.run('<stdin>', output)

    if error:
        print(error.as_string())
    else:
        print(result)
