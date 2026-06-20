def input_is_valid(msg, start=None, end=None):

    while True:

        try:
            value = int(input(msg))

            if start is not None and end is not None:

                if not (start <= value <= end):
                    print("Invalid range. Try again!")
                    continue

            return value

        except ValueError:
            print("Please enter numbers only!")