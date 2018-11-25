import webbrowser


def main():
    print("Openning Favorite Sites")

    with open("sites.txt") as fobj:
        try:
            for num, url in enumerate(fobj):
                url = url.rstrip("\n")
                webbrowser.open(url)
        except Exception as e:
            print(e)

    print("\nEnjoy!")


if __name__ == '__main__':
    main()
