import argparse
from metric_paper.metric_generator import eta_expression


def _parse_args():
    parser = argparse.ArgumentParser(description="Build symbolic eta equation from coefficients.")
    parser.add_argument("--theta", type=float, nargs=4, required=True, help="theta1 theta2 theta3 theta4")
    parser.add_argument("--lambda", dest="lam", type=float, nargs=4, required=True, help="lambda1 lambda2 lambda3 lambda4")
    return parser.parse_args()


def main():
    args = _parse_args()
    eq = eta_expression(args.theta, args.lam)
    print(eq)


if __name__ == "__main__":
    main()
