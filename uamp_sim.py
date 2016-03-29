import argparse
from controller import Controller


def parse_args():
    parser = argparse.ArgumentParser(description='Run uamp_sim')
    parser.add_argument('--trace', type=str, required=True,
                        help='User log trace file')
    parser.add_argument('--sim_config', type=str, required=True,
                        help='Sim Configuration File')
    return parser.parse_args()


def build_sim(args):
    controller = Controller()
    # TODO: Add simulator modules based on config file
    return controller

if __name__ == "__main__":
    args = parse_args()
    sim = build_sim(args)
    sim.run()

