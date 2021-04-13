import sys

from orchestrator import Orchestrator

def main(filename):
    orchestrator = Orchestrator()
    orchestrator.parse_quake_log(filename)







if __name__ == '__main__':
    main(sys.argv[1])
