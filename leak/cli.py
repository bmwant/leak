import argparse

from leak import main


def cli():
    parser = argparse.ArgumentParser(
        description="Show all releases for package and some info about it"
    )
    parser.add_argument("package_name", help="You should provide package name")
    args = parser.parse_args()
    main.main(package_name=args.package_name)


if __name__ == "__main__":
    cli()
