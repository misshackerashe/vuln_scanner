from scanner.core import start_scan

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Escáner básico de vulnerabilidades")
    parser.add_argument("target", help="IP o hostname del objetivo")
    args = parser.parse_args()

    start_scan(args.target)
