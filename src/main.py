from scanner import barcode_scanner


def scanner_check() -> int:
    key = barcode_scanner()
    return key


def main() -> None:
    key = scanner_check()
    print(key)


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass
