import argparse
import json

from pyvrl import Transform

def main(vrl_file: str, input_file: str) -> str:
    try:
        with open(vrl_file) as f:
            vrl = f.read()
            transform = Transform(vrl)
    except FileNotFoundError:
        print(f'could not open {vrl_file}')
        exit(1)
    except ValueError as e:
        print(f'{vrl_file} is not valid VRL program:\n{e}')
        exit(1)
    try:
        with open(input_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f'could not open {input_file}')
        exit(1)
    except json.JSONDecodeError:
        print(f'{input_file} is not valid JSON')
        exit(1)

    remapped = transform.remap({'message': data})

    return json.dumps(remapped)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='remaps JSON data using a VRL transform')
    parser.add_argument('vrl', type=str, help='VRL transform file')
    parser.add_argument('input', type=str, help='input JSON file')
    args = parser.parse_args()
    out = main(args.vrl, args.input)
    print(out)
