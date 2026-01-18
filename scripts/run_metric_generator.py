import argparse

from metric_paper.metric_generator import build_equation


def _parse_args():
    parser = argparse.ArgumentParser(description="Build a metric equation.")
    parser.add_argument("--a", type=float, required=True, help="Linear coefficient")
    parser.add_argument("--b", type=float, required=True, help="Intercept")
    parser.add_argument("--variable", default="x", help="Variable name")
    return parser.parse_args()


def main():
    args = _parse_args()
    equation = build_equation(args.a, args.b, args.variable)
    print(equation)


if __name__ == "__main__":
    main()
