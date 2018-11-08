import argparse
import hashlib
import os


def cli():
    _ALGORITHM_MAP = {
        'sha3_384': hashlib.sha3_384,
        'sha3_224': hashlib.sha3_224,
        'sha224': hashlib.sha224,
        'md5': hashlib.md5,
        'sha512': hashlib.sha512,
        'sha256': hashlib.sha256,
        'sha3_512': hashlib.sha3_512,
        'sha384': hashlib.sha384,
        'sha1': hashlib.sha1,
        'sha3_256': hashlib.sha3_256
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The file that you would like to be hashed")
    parser.add_argument("algorithm", help="The hash algorithm you would like to use")
    args = parser.parse_args()

    if os.path.exists(args.filename) and os.path.isfile(args.filename):
        if args.algorithm.lower() in _ALGORITHM_MAP:
            hash_function = _ALGORITHM_MAP[args.algorithm.lower()]()
            with open(args.filename, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_function.update(chunk)
            if args.algorithm.lower() in {'shake_128', 'shake_256'}:
                file_hash = hash_function.hexdigest(args.length)
            else:
                file_hash = hash_function.hexdigest()

            print(file_hash)

        else:
            print("Please provide a supported hash function.")
    else:
        print("Please provide a valid filename.")
