import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from metric_paper.metric_generator import eta_expression


def _parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Build symbolic eta equation from coefficients.")
    parser.add_argument("--theta", type=float, nargs=4, help="theta1 theta2 theta3 theta4")
    parser.add_argument("--lambda", dest="lam", type=float, nargs=4, help="lambda1 lambda2 lambda3 lambda4")
    return parser.parse_args()


def _prompt_list(label, meaning):
    print(f"{label} = {meaning}")
    print("Order: TP FN FP TN")
    while True:
        raw = input("Enter 4 numbers: ").strip()
        parts = raw.replace(",", " ").split()
        if len(parts) != 4:
            print("Please enter exactly 4 values.")
            continue
        try:
            return [float(x) for x in parts]
        except ValueError:
            print("Please enter numeric values.")


def main():
    args = _parse_args()
    theta = args.theta if args.theta else _prompt_list("theta", "[?1, ?2, ?3, ?4] value coefficients")
    lam = args.lam if args.lam else _prompt_list("lambda", "[?1, ?2, ?3, ?4] investment coefficients")
    eq = eta_expression(theta, lam)
    print("\nSymbolic metric:")
    print(f"eta = {eq.rhs}")


if __name__ == "__main__":
    main()
