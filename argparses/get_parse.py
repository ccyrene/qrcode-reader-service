import argparse

def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Grpc port of the triton server, default is 8001",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="spawn n process for client",
    )

    return parser.parse_args()